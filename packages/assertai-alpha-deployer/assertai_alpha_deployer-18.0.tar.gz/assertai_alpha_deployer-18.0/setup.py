from setuptools import setup

setup(
    name='assertai_alpha_deployer',
    version='18.0',
    packages=['assertai_alpha_deployer'],
    install_requires=[
        'psutil',
    ],
    entry_points={
        'console_scripts': [
            'assertai-alpha-deployer=assertai_alpha_deployer.__main__:main',
        ],
    },
    author='Rajesh Roy',
    author_email='rajeshroy402@gmail.com',
    description='A package to deploy python codes on bare-metal',
    long_description='A longer description of your package, can be the content of your README file',
    url='https://www.linkedin.com/in/rajeshroy402',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
