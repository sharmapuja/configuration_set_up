from setuptools import setup,find_packages

with open('README.md') as file:
    long_description = file.read()

setup(
    name='configuration_setup',
    version='1.0.0',
    packages=find_packages(),
    long_description=long_description,
    python_requires='>3.8',
    url='https://github.com/sharmapuja/configuration_set_up',
    license='',
    author='sharmapuja',
    author_email='sharmapuja689@gmail.com',
    description='Configuration File Parser and Env set Up',
    install_requires=["atomicwrites==1.4.0", "attrs==21.2.0", "colorama==0.4.4", "coverage==6.1", "iniconfig==1.1.1",
                      "packaging==21.2", "pluggy==1.0.0", "py==1.10.0", "pyparsing==2.4.7", "pytest==6.2.5",
                      "pytest-mock==3.6.1", "PyYAML==6.0", "toml==0.10.2"]
)
