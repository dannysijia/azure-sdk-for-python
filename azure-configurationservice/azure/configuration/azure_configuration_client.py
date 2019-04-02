# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------

import datetime

from msrest.pipeline.requests import PipelineRequestsHTTPSender, RequestsPatchSession
from msrest.pipeline import Request, Pipeline
from msrest.universal_http.requests import RequestsHTTPSender

from . import _generated
from ._generated.models import ConfigurationSettingPaged, ConfigurationSetting

from .azure_configuration_requests import AzConfigRequestsCredentialsPolicy
from .azure_configuration_client_validation import *
from .utils import get_endpoint_from_connection_string


class AzureConfigurationClient(object):
    """Represents an azconfig client

    :ivar config: Configuration for client.
    :vartype config: AzureConfigurationClient

    :param connection_string: Credentials needed for the client to connect to Azure.
    :type connection_string: str
    """

    def __init__(self, connection_string):

        base_url = "https://" + get_endpoint_from_connection_string(connection_string)
        self._client = _generated.AzureConfigurationClientImp(
            connection_string, base_url
        )
        self._client._client.config.pipeline = self._create_azconfig_pipeline()

    def _create_azconfig_pipeline(self):
        policies = [
            self._client.config.user_agent_policy,  # UserAgent policy
            RequestsPatchSession(),  # Support deprecated operation config at the session level
            self._client.config.http_logger_policy,  # HTTP request/response log
            AzConfigRequestsCredentialsPolicy(self._client.config),
        ]

        return Pipeline(
            policies,
            PipelineRequestsHTTPSender(
                RequestsHTTPSender(self._client.config)
            ),  # Send HTTP request using requests
        )

    def list_configuration_settings(
        self, labels=None, keys=None, accept_date_time=None, fields=None, **kwargs
    ):
        # type: (list, list, datetime, list, dict) -> ConfigurationSettingPaged

        """List configuration settings.

        List the configuration settings in the configuration store, optionally filtered by
        label.

        :param labels: Filter returned values based on their label. '*' can be
         used as wildcard in the beginning or end of the filter
        :type labels: list[str]
        :param keys: Filter returned values based on their keys. '*' can be
         used as wildcard in the beginning or end of the filter
        :type keys: list[str]
        :param accept_date_time: Obtain representation of the result related
         to past time.
        :type accept_date_time: datetime
        :param fields: Specify which fields to return
        :type fields: list[str]
        :param dict kwargs: if headers key exists, it will be added to the request
        :return: An iterator like instance of ConfigurationSetting
        :rtype:
         ~azconfig.models.ConfigurationSettingPaged[~azconfig.models.ConfigurationSetting]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        return self._client.list_configuration_settings(
            label=labels,
            key=keys,
            fields=fields,
            accept_date_time=accept_date_time,
            custom_headers=kwargs.get("headers"),
        )

    def get_configuration_setting(
        self, key, label=None, accept_date_time=None, **kwargs
    ):
        # type: (str, str, datetime, dict) -> ConfigurationSetting

        """Get a ConfigurationSetting.

        Get the ConfigurationSetting for the given key and label.

        :param key: string
        :type key: str
        :param label: Label of key to retreive
        :type label: str
        :param accept_date_time: Obtain representation of the result related
         to past time.
        :type accept_date_time: datetime
        :param dict kwargs: if headers key exists, it will be added to the request
        :return: ConfigurationSetting
        :rtype: ~azure.configurationservice.models.ConfigurationSetting
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        validate_get_configuration_setting(key)
        return self._client.get_configuration_setting(
            key=key,
            label=label,
            accept_date_time=accept_date_time,
            custom_headers=kwargs.get("headers"),
        )

    def add_configuration_setting(self, configuration_setting, **kwargs):
        # type: (ConfigurationSetting, dict) -> ConfigurationSetting

        """Create a ConfigurationSetting.

        Create a ConfigurationSetting.

        :param configuration_setting:
        :type configuration_setting: ~azure.configurationservice.models.ConfigurationSetting
        :param dict kwargs: if headers key exists, it will be added to the request
        :return: ConfigurationSetting
        :rtype: ~azure.configurationservice.models.ConfigurationSetting
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        custom_headers = validate_add_configuration_setting(
            configuration_setting, **kwargs
        )
        return self._client.create_or_update_configuration_setting(
            configuration_setting=configuration_setting,
            key=configuration_setting.key,
            label=configuration_setting.label,
            custom_headers=custom_headers,
        )

    def update_configuration_setting(
        self,
        key,
        value=None,
        content_type=None,
        tags=None,
        label=None,
        etag=None,
        **kwargs
    ):
        # type: (str, str, str, dict, str, str, dict) -> ConfigurationSetting

        """Update a ConfigurationSetting.

        Update a ConfigurationSetting.

        :param key: string
        :type key: str
        :param value:
        :type value: str
        :param content_type:
        :type content_type: str
        :param tags:
        :type tags: dict
        :param label:
        :type label: str
        :param etag:
        :type etag: str
        :param dict kwargs: if headers key exists, it will be added to the request
        :return: ConfigurationSetting
        :rtype: ~azure.configurationservice.models.ConfigurationSetting
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """

        custom_headers = validate_update_configuration_setting(key, etag, **kwargs)

        current_configuration_setting = self._client.get_configuration_setting(
            key, label
        )
        if value is not None:
            current_configuration_setting.value = value
        if content_type is not None:
            current_configuration_setting.content_type = content_type
        if tags is not None:
            current_configuration_setting.tags = tags
        return self._client.create_or_update_configuration_setting(
            configuration_setting=current_configuration_setting,
            key=key,
            label=label,
            custom_headers=custom_headers,
        )

    def set_configuration_setting(self, configuration_setting, **kwargs):
        # type: (ConfigurationSetting, dict) -> ConfigurationSetting

        """Set a KeyValue.

        Create or update a ConfigurationSetting.

        :param configuration_setting:
        :type configuration_setting: ~azure.configurationservice.models.KeyValue
        :param key: string
        :type key: str
        :param label:
        :type label: str
        :param dict kwargs: if headers key exists, it will be added to the request
        :return: ConfigurationSetting
        :rtype: ~azure.configurationservice.models.ConfigurationSetting
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        custom_headers = validate_set_configuration_setting(
            configuration_setting, **kwargs
        )
        return self._client.create_or_update_configuration_setting(
            configuration_setting=configuration_setting,
            key=configuration_setting.key,
            label=configuration_setting.label,
            custom_headers=custom_headers,
        )

    def delete_configuration_setting(self, key, label=None, etag=None, **kwargs):
        # type: (str, str, str, dict) -> ConfigurationSetting

        """Delete a ConfigurationSetting.

        :param key: string
        :type key: str
        :param label:
        :type label: str
        :param etag:
        :type etag: str
        :param dict kwargs: if headers key exists, it will be added to the request
        :return: ConfigurationSetting
        :rtype: ~azure.configurationservice.models.ConfigurationSetting
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        custom_headers = validate_delete_configuration_setting(key, etag, **kwargs)
        return self._client.delete_configuration_setting(
            key=key, label=label, custom_headers=custom_headers
        )

    def lock_configuration_setting(self, key, label=None, **kwargs):
        # type: (str, str, dict) -> ConfigurationSetting

        """ Lock a ConfigurationSetting

        :param key:
        :type key: str
        :param label:
        :type label: str
        :param dict kwargs: if headers key exists, it will be added to the request
        :return: ConfigurationSetting
        :rtype: ~azure.configurationservice.models.ConfigurationSetting
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        validate_lock_configuration_setting(key)
        return self._client.lock_configuration_setting(
            key=key, label=label, custom_headers=kwargs.get("headers")
        )

    def unlock_configuration_setting(self, key, label=None, **kwargs):
        # type: (str, str, dict) -> ConfigurationSetting

        """ Unlock a ConfigurationSetting

        :param key:
        :type key: str
        :param label:
        :type label: str
        :param dict kwargs: if headers key exists, it will be added to the request
        :return: ConfigurationSetting
        :rtype: ~azure.configurationservice.models.ConfigurationSetting
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        validate_unlock_configuration_setting(key)
        return self._client.unlock_configuration_setting(
            key=key, label=label, custom_headers=kwargs.get("headers")
        )

    def list_revisions(
        self, labels=None, keys=None, accept_date_time=None, fields=None, **kwargs
    ):
        # type: (list, list, datetime, list, dict) -> ConfigurationSettingPaged

        """

        :param labels: Filter returned values based on their label. '*' can be
         used as wildcard in the beginning or end of the filter
        :type labels: list[str]
        :param keys: Filter returned values based on their keys. '*' can be
         used as wildcard in the beginning or end of the filter
        :type keys: list[str]
        :param accept_date_time: Obtain representation of the result related
         to past time.
        :type accept_date_time: datetime
        :param fields: Specify which fields to return
        :type fields: list[str]
        :param dict kwargs: if headers key exists, it will be added to the request
        :return: An iterator like instance of ConfigurationSetting
        :rtype:
         ~azconfig.models.ConfigurationSettingPaged[~azconfig.models.ConfigurationSetting]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        return self._client.list_revisions(
            label=labels,
            key=keys,
            fields=fields,
            accept_date_time=accept_date_time,
            custom_headers=kwargs.get("headers"),
        )
