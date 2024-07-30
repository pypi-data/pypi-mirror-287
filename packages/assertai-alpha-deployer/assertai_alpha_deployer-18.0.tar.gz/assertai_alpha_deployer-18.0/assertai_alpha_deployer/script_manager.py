import os
import sys
import time
import psutil
import datetime
import argparse
import getpass

class ScriptRunner:
    def __init__(self, user):
        self.user = user
        self.code_name = None

    def create_bash(self, path, command, code_name):
        expanded_path = os.path.expanduser(path)
        if not os.path.exists(expanded_path):
            print(f"Error: Path '{expanded_path}' does not exist. Exiting.")
            sys.exit(1)
        if not command:
            print(f"Error: Command is empty. Exiting.")
            sys.exit(1)

        if 'python' in command:
            script_file = command.split()[1]
            if script_file.endswith('.py'):
                script_file_path = os.path.join(expanded_path, script_file)
                if not os.path.exists(script_file_path):
                    print(f"Error: Script '{script_file_path}' does not exist. Exiting.")
                    sys.exit(1)
        os.system(f"cd {expanded_path} && {command}")
        script_dir = f'/home/{self.user}/scripts'
        if not os.path.exists(script_dir):
            os.makedirs(script_dir)
        script_file = os.path.join(script_dir, f"run_{code_name}.sh")
        with open(script_file, 'w') as f:
            f.write(f"#!/bin/bash\ncd {expanded_path}\n{command}")
        self.code_name = code_name
        return script_file

    def restart_process(self, start_time, end_time, process_name, script_file):
        start_time = datetime.datetime.strptime(start_time, '%H:%M:%S').time()
        end_time = datetime.datetime.strptime(end_time, '%H:%M:%S').time()
        while True:
            try:
                ds = []
                for proc in psutil.process_iter(['pid', 'cmdline']):
                    if 'python3' in proc.info['cmdline'] and process_name in proc.info['cmdline']:
                        ds.append(proc.info['pid'])
                current_time = datetime.datetime.now().time()
                if start_time <= current_time <= end_time:
                    if not ds:
                        print(f"Opening {process_name} at {current_time.strftime('%H:%M:%S')}")
                        os.system(f"bash {script_file}")
                else:
                    if ds:
                        print(f"Closing {process_name} at {current_time.strftime('%H:%M:%S')}")
                        for pid in ds:
                            os.system(f"sudo kill -15 {pid}")
                time.sleep(5)
            except KeyboardInterrupt:
                break

    def generate_restart_code(self, start_time, end_time, process_name, script_file):
        print("Generating restart code...")
        restart_code = f"""
import os
import time
import psutil
import datetime

def restart_process(start_time, end_time, process_name, script_file):
    while True:
        try:
            ds = []
            for proc in psutil.process_iter(['pid', 'cmdline']):
                if 'python3' in proc.info['cmdline'] and process_name in proc.info['cmdline']:
                    ds.append(proc.info['pid'])
            current_time = datetime.datetime.now().time()
            if start_time <= current_time <= end_time:
                if not ds:
                    print(f"Opening {{process_name}} at {{current_time.strftime('%H:%M:%S')}}")
                    os.system(f'bash {{script_file}}')
            else:
                if ds:
                    print(f"Closing {{process_name}} at {{current_time.strftime('%H:%M:%S')}}")
                    for pid in ds:
                        os.system(f'sudo kill -15 {{pid}}')
            time.sleep(5)
        except KeyboardInterrupt:
            break

if __name__ == '__main__':
    restart_process(datetime.datetime.strptime('{start_time}', '%H:%M:%S').time(),
                    datetime.datetime.strptime('{end_time}', '%H:%M:%S').time(),
                    '{process_name}', '{script_file}')
"""
        try:
            script_dir = f'/home/{self.user}/scripts'
            if not os.path.exists(script_dir):
                os.makedirs(script_dir)
            target_file = os.path.join(script_dir, f'restart_{self.code_name}.py')
            with open(target_file, 'w') as f:
                f.write(restart_code)
            print(f"Restart code generated at {target_file}")
        except Exception as e:
            print(f"Error generating restart code: {e}")

    def create_service(self):
        print("Creating service file...")
        service_content = f"""[Unit]
Description=Restart Code Service for {self.code_name}
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/{self.user}/scripts/restart_{self.code_name}.py
Restart=always
User={self.user}

[Install]
WantedBy=multi-user.target
"""
        try:
            service_path = f"/etc/systemd/system/restart_{self.code_name}.service"
            with open(service_path, 'w') as f:
                f.write(service_content)
            print(f"Service file created at {service_path}")
            os.system("sudo systemctl daemon-reload")
            os.system(f"sudo systemctl enable restart_{self.code_name}.service")
            os.system(f"sudo systemctl start restart_{self.code_name}.service")
            print(f"Service restart_{self.code_name}.service has been enabled and started.")
        except Exception as e:
            print(f"Error creating service file: {e}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--user", help="Specify the user for script paths", default=getpass.getuser())
    parser.add_argument("--path", required=True, help="Path to the script to run")
    parser.add_argument("--python_command", required=True, help="Full Python command to run")
    parser.add_argument("--code_name", required=True, help="Name of the script to create")
    parser.add_argument("--process_name", required=True, help="Name of the process to restart")
    parser.add_argument("--start_time", required=True, help="Start time for the process to run")
    parser.add_argument("--end_time", required=True, help="End time for the process to run")
    args = parser.parse_args()

    runner = ScriptRunner(user=args.user)
    script_file = runner.create_bash(args.path, args.python_command, args.code_name)
    runner.generate_restart_code(args.start_time, args.end_time, args.process_name, script_file)
    runner.restart_process(args.start_time, args.end_time, args.process_name, script_file)
    runner.create_service()

if __name__ == "__main__":
    main()