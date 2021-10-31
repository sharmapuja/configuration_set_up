# Intro

This is the module for reading configuration files like yaml,conf and cfg and generate flattened dictionary out of it.
After generating flattened dictionary it can also set the configurations in os or write them in .env or .json file

## Development Supported OS
Ubuntu Desktop 20.04 LTS

## Source code directory and file structure
src : All source code applications.

tests: All test files for source code applications


## How to Use - Development Environment
1. Configuration & Installation: 
   
    a. Clone Repository
        https://github.com/sharmapuja/configuration_set_up.git

    b. Create virtual environment
        Go to root directory 'configuration_setup'.
   
        pytho3 -m "venv" venv

    c. Activate virtual environment
   
        source venv/bin/activate

    d. Install required python packages
   
        pip install -r requirements.txt

    e. Start the Flask development web server
   
        python src\config_setup.py
                    or
        python src\config_setup.py --path "file_path"

    f. Running the automated unit tests
   
        pytest -v 


