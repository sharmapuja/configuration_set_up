#! /usr/bin/python3.8

""" Configuration file Set up.

@file config_setup.py
@author Puja Sharma
@date 29th October 2021

About; -
--------
    This python module is responsible for parsing configuration files : .cfg,.conf and .yaml file
    It reads the file as dictionary and generate flat dictionary out of it and write the configuration in
    .env , .json or set the environment variables

Uses; -
-------

Reference; -
------------

"""

import argparse
import configparser
import json
import os
import sys

import yaml

sys.path.append(os.path.abspath(os.path.join('src')))
from utils import flatten_dict


def dir_path(path):
    """
    Validates file path

    :param path: file path
    :return: file path
    """
    if os.path.isfile(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")


class ConfigSetUp:
    """
    Parse Configuration files to flattened dictionary.
    And write the same in .env , .json
    Or set the configurations in os environment
    """

    def __init__(self, flattened_dict=None):
        self._flattened_dict = flattened_dict

    @staticmethod
    def read_yaml(file):
        """
        Read .yaml/.yml file into dictionary

        :param file: path to yaml file
        :return: Nested Dictionary
        :rtype: Dict
        """
        with open(file, 'r') as file_out:
            config_dict = yaml.safe_load(file_out)

        # print(config_dict)
        return config_dict

    @staticmethod
    def read_config(file):
        """
        Read .conf,.cfg,.ini file into dictionary

        :param file: path to .conf/.cfg file
        :return: Nested Dictionary
        :rtype: Dict
        """

        config = configparser.ConfigParser()
        config.read(file)

        dictionary = {}
        for section in config.sections():
            dictionary[section] = {}
            for option in config.options(section):
                dictionary[section][option] = config.get(section, option)

        return dictionary

    @staticmethod
    def get_ext(file):
        """
        Get file extension

        :param file: Path to config file
        :return: filename and file extension
        :rtype:str
        """
        file_name, file_extension = os.path.splitext(file)
        return file_name, file_extension

    def create_env_file(self):
        """
        Create .env file and write variables in it
        :return: boolean
        """
        with open(".env", "w") as env_file:
            for key, val in self._flattened_dict.items():
                env_file.write(f'{key}={str(val)}' + "\n")
        return True

    def create_json_file(self):
        """
        Create .json file and write environment variables in it
        :return:boolean
        """
        with open("env.json", 'w') as file_out:
            json_dumps_str = json.dumps(self._flattened_dict, indent=4)
            print(json_dumps_str, file=file_out)
        return True

    def write_env(self, output_format):
        """
        Write the configurations of flattened dict in .env or .json
        depending on output format

        :param output_format: format for writing the configuration in respective file
        :return: None

        """

        if output_format == "env":
            return self.create_env_file()
        elif output_format == "json":
            return self.create_json_file()
        else:
            raise ValueError("Output Format for Environment file is incorrect")

    def set_env(self):
        """
        Set Configurations in os Environment
        :return: None
        """
        for key, val in self._flattened_dict.items():
            os.environ[key] = str(val)

    def read(self, file):
        """
        Read configuration file as nested dictionary  and generate flattened dict
        :param file: Path to config file
        :return: filename
        :rtype:str
        """
        file_name, file_ext = self.get_ext(file)

        if file_ext == ".yml" or file_ext == ".yaml":
            config_dict = self.read_yaml(file)
        elif file_ext == ".conf" or file_ext == ".cfg":
            config_dict = self.read_config(file)
        else:
            raise ValueError("Given File cannot be parsed by the Parser")

        self._flattened_dict = flatten_dict(config_dict)

        return file_name


if __name__ == '__main__':
    file_path = os.path.join('src', 'configurations', 'sample.yaml')
    config_obj = ConfigSetUp()
    try:
        if len(sys.argv) == 1:
            configuration_dict = config_obj.read(file_path)
        else:
            parser = argparse.ArgumentParser()
            parser.add_argument('--path', type=dir_path, help='enter the path for query_log directory')
            args = vars(parser.parse_args())
            config_obj.read(args['path'])

        config_obj.write_env("json")
        config_obj.write_env("env")
        # or
        # config_obj.set_env()

    except ValueError as error:
        print(error)


