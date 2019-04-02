from .._generated.aio import AzureConfigurationClientImp
from ..azure_configuration_requests import AzConfigRequestsCredentialsPolicy


from ..azure_configuration_requests import AzConfigRequestsCredentialsPolicy
from msrest.pipeline.requests import RequestsPatchSession

from msrest.pipeline import Request, Pipeline

from msrest.universal_http.async_requests import AsyncRequestsHTTPSender
from msrest.pipeline.async_requests import (
    AsyncPipelineRequestsHTTPSender
)
from ..azure_configuration_client_validation import *

from ..utils import get_endpoint_from_connection_string


class AzureConfigurationClientAsync(object):
    """Represents an azconfig client

    :ivar config: Configuration for client.
    :vartype config: AzureConfigurationClientConfiguration

    :param connection_string: Credentials needed for the client to connect to Azure.
    :type connection_string: str
    """

    def __init__(
            self, connection_string):

        base_url = "https://" + get_endpoint_from_connection_string(connection_string)
        self._client = AzureConfigurationClientImp(connection_string, base_url)
        self._client._client.config.pipeline = self._create_azconfig_pipeline()
    
    def _create_azconfig_pipeline(self):
        policies = [
            self._client.config.user_agent_policy,  # UserAgent policy
            RequestsPatchSession(),         # Support deprecated operation config at the session level
            self._client.config.http_logger_policy,  # HTTP request/response log
            AzConfigRequestsCredentialsPolicy(self._client.config)
        ]

        return Pipeline(
            policies,
            AsyncPipelineRequestsHTTPSender(
                AsyncRequestsHTTPSender(self._client.config)  # Send HTTP request using requests
            )
        )

    def list_configuration_settings(
            self, labels=None, keys=None, accept_date_time=None, fields=None, **kwargs):
        """List key values.

        List the key values in the configuration store, optionally filtered by
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
        :return: An iterator like instance of KeyValue
        :rtype:
         ~azure.configurationservice.models.KeyValuePaged[~azure.configurationservice.models.KeyValue]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        return self._client.list_configuration_settings(label=labels, key=keys, accept_date_time=accept_date_time, fields=fields, custom_headers=kwargs.get("headers"))
    
    async def get_configuration_setting(
            self, key, label=None, accept_date_time=None, **kwargs):
        """Get a KeyValue.

        Get the KeyValue for the given key and label.

        :param key: string
        :type key: str
        :param label: Label of key to retreive
        :type label: str
        :param accept_date_time: Obtain representation of the result related
         to past time.
        :type accept_date_time: datetime
        :param dict kwargs: if headers key exists, it will be added to the request
        :return: KeyValue
        :rtype: ~azure.configurationservice.models.KeyValue
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        custom_headers = validate_get_configuration_setting(key)
        return await self._client.get_configuration_setting(key=key, label=label, accept_date_time=accept_date_time, custom_headers=kwargs.get("headers"))

    async def add_configuration_setting(
            self, configuration_setting, **kwargs):
        """Create a KeyValue.

        Create a KeyValue.

        :param configuration_setting:
        :type configuration_setting: ~azure.configurationservice.models.KeyValue
        :param dict kwargs: if headers key exists, it will be added to the request
        :return: KeyValue
        :rtype: ~azure.configurationservice.models.KeyValue
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        custom_headers = validate_add_configuration_setting(configuration_setting, **kwargs)
        key = configuration_setting.key
        return await self._client.create_or_update_configuration_setting(configuration_setting=configuration_setting, key=key, label=configuration_setting.label, custom_headers=custom_headers)
    
    async def update_configuration_setting(
            self, key, value=None, content_type=None, tags=None, label=None, etag=None, **kwargs):
        """Update a KeyValue.

        Update a KeyValue.

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
        :return: KeyValue
        :rtype: ~azure.configurationservice.models.KeyValue
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        custom_headers = validate_update_configuration_setting(key, etag, **kwargs)
        current_configuration_setting = await self._client.get_configuration_setting(key, label)
        if value is not None:
            current_configuration_setting.value = value
        if content_type is not None:
            current_configuration_setting.content_type = content_type
        if tags is not None:
            current_configuration_setting.tags = tags
        return await self._client.create_or_update_configuration_setting(configuration_setting=current_configuration_setting, key=key, label=label, custom_headers=custom_headers)
    
    async def set_configuration_setting(
            self, configuration_setting, **kwargs):
        """Set a KeyValue.

        Create or update a KeyValue.

        :param configuration_setting:
        :type configuration_setting: ~azure.configurationservice.models.KeyValue
        :param key: string
        :type key: str
        :param label:
        :type label: str
        :param dict kwargs: if headers key exists, it will be added to the request
        :return: KeyValue
        :rtype: ~azure.configurationservice.models.KeyValue
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        custom_headers = validate_set_configuration_setting(configuration_setting, **kwargs)
        key = configuration_setting.key
        return await self._client.create_or_update_configuration_setting(configuration_setting=configuration_setting, key=key, label=configuration_setting.label, custom_headers=custom_headers)
    
    async def delete_configuration_setting(
            self, key, label=None, etag=None, **kwargs):
        """Delete a KeyValue.

        :param key: string
        :type key: str
        :param label:
        :type label: str
        :param etag:
        :type etag: str
        :param dict kwargs: if headers key exists, it will be added to the request
        :return: KeyValue
        :rtype: ~azure.configurationservice.models.KeyValue
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        custom_headers = validate_delete_configuration_setting(key, etag, **kwargs)
        return await self._client.delete_configuration_setting(key=key, label=label, custom_headers=custom_headers)

    async def lock_configuration_setting(
            self, key, label=None, **kwargs):
        """

        :param key:
        :type key: str
        :param label:
        :type label: str
        :param dict kwargs: if headers key exists, it will be added to the request
        :return: KeyValue
        :rtype: ~azure.configurationservice.models.KeyValue
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        custom_headers = validate_lock_configuration_setting(key)
        return await self._client.lock_configuration_setting(key=key, label=label, custom_headers=custom_headers)
    
    async def unlock_configuration_setting(
            self, key, label=None, **kwargs):
        """

        :param key:
        :type key: str
        :param label:
        :type label: str
        :param dict kwargs: if headers key exists, it will be added to the request
        :return: KeyValue
        :rtype: ~azure.configurationservice.models.KeyValue
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        custom_headers = validate_unlock_configuration_setting(key)
        return await self._client.unlock_configuration_setting(key=key, label=label, custom_headers=custom_headers)
    
    def list_revisions(
            self, labels=None, keys=None, accept_date_time=None, fields=None, **kwargs):
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
        :return: An iterator like instance of KeyValue
        :rtype:
         ~azure.configurationservice.models.KeyValuePaged[~azure.configurationservice.models.KeyValue]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        return self._client.list_revisions(label=labels, key=keys, accept_date_time=accept_date_time, fields=fields, custom_headers=kwargs.get("headers"))