from setuptools import setup, find_packages

setup(
    name='coreframe',
    version='0.1.0',
    description='A simple backend framework built using python',
    author="Adewunmi Oladele",
    author_email="rkutalian@gmail.com",
    entry_points={
        'console_scripts': [
            # When the user types 'coreframe' on terminal, it runs the function coreframe from the command.py file
            'coreframe=command:coreframe',
        ],
    },
)