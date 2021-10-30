"""Unit test for test_config_setup.py module.

@file test_config_setup.py
@author Puja Sharma
@date 30th October 2021

About; -
--------
    This python module is responsible for testing config_setup.py module

Uses; -
-------

Reference; -
------------

"""

import argparse
import os

import pytest

from src.config_setup import ConfigSetUp, dir_path
from tests.config.sample_dictionary import flattened_dict, test_config_dict

write_env = 'src.config_setup.ConfigSetUp.write_env'
get_ext = 'src.config_setup.ConfigSetUp.get_ext'
read_yaml = 'src.config_setup.ConfigSetUp.read_yaml'


@pytest.fixture()
def temp_path_valid():
    return os.path.join(os.getcwd(), 'src', 'configurations', 'sample.conf')


@pytest.fixture()
def temp_path_invalid():
    return os.path.join(os.getcwd(), 'invalid')


@pytest.fixture()
def get_file_path(file_name):
    return os.path.join(os.getcwd(), 'tests', 'config', file_name)


@pytest.fixture()
def config_setup():
    return ConfigSetUp(flattened_dict)


def test_dir_path_invalid(temp_path_invalid):
    """Test method for dir_path to validate exception is raised when path is valid"""

    with pytest.raises(argparse.ArgumentTypeError):
        dir_path(temp_path_invalid)


def test_dir_path_valid(temp_path_valid):
    """ Test method to validate if given file path is valid """
    path = dir_path(temp_path_valid)
    print(path)
    assert path == temp_path_valid


class TestConfigSetUp:
    """ Test class for ConfigSetUp """

    @pytest.mark.parametrize('file_name', ["sample2.yaml"])
    def test_read_yaml(self, get_file_path):
        """
        Test dictionary generation from yaml file
        :param get_file_path: pytest fixture to get file_path

        """
        config_dict = ConfigSetUp.read_yaml(get_file_path)
        assert type(config_dict) is dict

    @pytest.mark.parametrize('file_name', ["sample1.conf", "sample3.cfg"])
    def test_read_config(self, get_file_path):
        """
        Test dictionary generation from conf
        :param get_file_path: pytest fixture to get file_path

        """
        config_dict = ConfigSetUp.read_config(get_file_path)
        assert type(config_dict) is dict

    def test_get_ext(self):
        """
        Test file extension and filename generation

        """
        test_file = "testfile.txt"
        file_name, file_ext = ConfigSetUp.get_ext(test_file)
        assert file_ext == '.txt'
        assert file_name == 'testfile'

    def test_create_env_file(self, config_setup):
        """
        Test .env created
        :param config_setup: ConfigSetUp object
        """
        assert config_setup.create_env_file()

    def test_create_json_file(self, config_setup):
        """
        Test .json created
        :param config_setup: ConfigSetUp object
        """

        assert config_setup.create_json_file()

    def test_write_env1(self, mocker, config_setup):
        """
        Test .env file is created on output_format = env
        :param mocker: pytest mocker
        :param config_setup: ConfigSetUp object

        """

        mocker.patch(write_env, return_value=".env created")
        response = config_setup.write_env(output_format="env")
        assert response == ".env created"

    def test_write_env2(self, mocker, config_setup):
        """
        Test .json file is created on output_format = json
        :param mocker: pytest mocker
        :param config_setup: ConfigSetUp object
        """
        mocker.patch(write_env, return_value=".json created")
        response = config_setup.write_env(output_format="env")
        assert response == ".json created"

    def test_write_env3(self, config_setup):
        """
        Test ValueError raised on passing output_format other than env and json
        :param config_setup: ConfigSetUp object
        """

        with pytest.raises(ValueError):
            config_setup.write_env(output_format="yaml")

    def test_set_env(self, config_setup):
        """
        Test Configuration set in os environment
        :param config_setup: ConfigSetUp object
        """

        config_setup.set_env()
        for key in flattened_dict.keys():
            assert key in os.environ

    def test_read1(self, mocker, config_setup, temp_path_valid):
        """
        Test .yaml file is read and flattened dict is generated
        :param mocker: pytest mocker
        :param config_setup: ConfigSetUp object
        :param temp_path_valid: valid file path

        """
        filename = "config_yaml1"
        file_ext1 = ".yaml"

        mocker.patch(get_ext, return_value=(filename, file_ext1))
        mocker.patch(read_yaml, return_value=test_config_dict)

        response = config_setup.read(temp_path_valid)
        assert response == filename

    def test_read2(self, mocker, config_setup, temp_path_valid):
        """
        Test .yml file is read and flattened dict is generated
        :param mocker: pytest mocker
        :param config_setup: ConfigSetUp object
        :param temp_path_valid: valid file path

        """
        filename = "config_yaml2"
        file_ext2 = ".yml"

        mocker.patch(get_ext, return_value=(filename, file_ext2))
        mocker.patch(read_yaml, return_value=test_config_dict)

        response = config_setup.read(temp_path_valid)
        assert response == filename

    def test_read3(self, mocker, config_setup, temp_path_valid):
        """
        Test .conf file is read and flattened dict is generated
        :param mocker: pytest mocker
        :param config_setup: ConfigSetUp object
        :param temp_path_valid: valid file path

        """
        filename = "config_conf1"
        file_ext2 = ".conf"

        mocker.patch(get_ext, return_value=(filename, file_ext2))
        mocker.patch(read_yaml, return_value=test_config_dict)

        response = config_setup.read(temp_path_valid)
        assert response == filename

    def test_read4(self, mocker, config_setup, temp_path_valid):
        """
        Test .cfg file is read and flattened dict is generated
        :param mocker: pytest mocker
        :param config_setup: ConfigSetUp object
        :param temp_path_valid: valid file path

        """
        filename = "config_conf2"
        file_ext2 = ".cfg"

        mocker.patch(get_ext, return_value=(filename, file_ext2))
        mocker.patch(read_yaml, return_value=test_config_dict)

        response = config_setup.read(temp_path_valid)
        assert response == filename

    def test_read5(self, mocker, config_setup, temp_path_valid):
        """ Test ValueError raised on passing output_format other than env and json
        :param mocker: pytest mocker
        :param config_setup: ConfigSetUp object
        :param temp_path_valid: valid file path

        """

        filename = "config_txt"
        file_ext2 = ".txt"

        mocker.patch(get_ext, return_value=(filename, file_ext2))

        with pytest.raises(ValueError):
            config_setup.read(temp_path_valid)
