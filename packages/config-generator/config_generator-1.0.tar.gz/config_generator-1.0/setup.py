from setuptools import setup, find_packages

setup(
    name = 'config-generator',
    version = 'v1.0',
    packages = find_packages(),
    install_requires = [
        'pydantic>=2.8'
    ]   
)