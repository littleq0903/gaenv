from setuptools import setup, find_packages

setup(
    name='gaenv',
    version='0.0.1',
    description='A script to make your virtual environment GAE-compatible',
    long_description=open('README.md').read(),
    keywords='virtualenv',
    author='Colin Su',
    author_email='littleq0903@gmail.com',
    license='MIT',
    entry_points={
        'console_scripts': [
            'gaenv=gaenv:cmd_main'
        ]
    },
    require=[
        'clime'
    ])



