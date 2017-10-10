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


class LocalDataVolume(Model):
    """Represents mapping of host directories to directories in the container.

    :param host_path: The path on the host that is to be mounted as a
     directory in the container.
    :type host_path: str
    :param local_path: The container local path where the host directory is
     mounted.
    :type local_path: str
    """

    _validation = {
        'host_path': {'required': True},
        'local_path': {'required': True},
    }

    _attribute_map = {
        'host_path': {'key': 'hostPath', 'type': 'str'},
        'local_path': {'key': 'localPath', 'type': 'str'},
    }

    def __init__(self, host_path, local_path):
        self.host_path = host_path
        self.local_path = local_path
