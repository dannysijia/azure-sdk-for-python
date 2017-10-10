# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Caffe2Settings(Model):
    """Specifies the settings for Caffe2 job.

    :param python_script_file_path: The path and file name of the python
     script to execute the job.
    :type python_script_file_path: str
    :param python_interpreter_path: The path to python interpreter.
    :type python_interpreter_path: str
    :param command_line_args: Command line arguments that needs to be passed
     to the python script.
    :type command_line_args: str
    """

    _validation = {
        'python_script_file_path': {'required': True},
    }

    _attribute_map = {
        'python_script_file_path': {'key': 'pythonScriptFilePath', 'type': 'str'},
        'python_interpreter_path': {'key': 'pythonInterpreterPath', 'type': 'str'},
        'command_line_args': {'key': 'commandLineArgs', 'type': 'str'},
    }

    def __init__(self, python_script_file_path, python_interpreter_path=None, command_line_args=None):
        self.python_script_file_path = python_script_file_path
        self.python_interpreter_path = python_interpreter_path
        self.command_line_args = command_line_args
