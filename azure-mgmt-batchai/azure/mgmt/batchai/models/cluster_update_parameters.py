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


class ClusterUpdateParameters(Model):
    """Parameters supplied to the Update operation.

    :param tags: The user specified tags associated with the Cluster.
    :type tags: dict
    :param scale_settings: Desired scale for the cluster.
    :type scale_settings: :class:`ScaleSettings
     <azure.mgmt.batchai.models.ScaleSettings>`
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'scale_settings': {'key': 'properties.scaleSettings', 'type': 'ScaleSettings'},
    }

    def __init__(self, tags=None, scale_settings=None):
        self.tags = tags
        self.scale_settings = scale_settings
