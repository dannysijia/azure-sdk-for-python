# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

# pylint: disable=unsubscriptable-object
# disabled unsubscriptable-object because of pylint bug referenced here:
# https://github.com/PyCQA/pylint/issues/3882

from typing import IO, TYPE_CHECKING

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse # type: ignore

from msrest import Deserializer, Serializer
from azure.core import PipelineClient
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from ._generated import models as _models
from ._generated._configuration import AzureCommunicationCallingServerServiceConfiguration

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]


class ContentDownloader(object):
    """ContentDownloader operations.

       You should not instantiate this class directly. Instead, you should create a Client instance that
        instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.communication.callingserver.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self,
        client, # type: PipelineClient
        serializer, # type: Serializer
        deserializer, # type: Deserializer
        config # type: AzureCommunicationCallingServerServiceConfiguration
    ): # type: (...) -> None
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def download(
            self,
            content_url,  # type: str
            http_range=None, #type: Optional[str]
            **kwargs  # type: Any
    ):  # type: (...) -> IO
        """Start download.

        :param content_url: The content url
        :return: Stream, or the result of cls(response)
        :param http_range: Return only the bytes of the content in the specified range.
        :type http_range: str
        :rtype: ~azure.communication.callingserver.models.DownloadContentResult
        :return: IO, or the result of cls(response)
        :rtype: IO
        :raises: ~azure.core.exceptions.HttpResponseError
        """

        cls = kwargs.pop('cls', None)  # type: ClsType[IO]
        error_map = {
            409: ResourceExistsError,
            400: lambda response: HttpResponseError(response=response,
                                                    model=self._deserialize(_models.CommunicationErrorResponse,
                                                                            response)),
            401: lambda response: ClientAuthenticationError(response=response,
                                                            model=self._deserialize(_models.CommunicationErrorResponse,
                                                                                    response)),
            403: lambda response: HttpResponseError(response=response,
                                                    model=self._deserialize(_models.CommunicationErrorResponse,
                                                                            response)),
            404: lambda response: ResourceNotFoundError(response=response,
                                                        model=self._deserialize(_models.CommunicationErrorResponse,
                                                                                response)),
            500: lambda response: HttpResponseError(response=response,
                                                    model=self._deserialize(_models.CommunicationErrorResponse,
                                                                            response)),
        }
        error_map.update(kwargs.pop('error_map', {}))

        url = content_url
        uri_to_sign_with = self.get_url_to_sign_request_with(url)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['UriToSignWith'] = self._serialize.header("uri_to_sign_with", uri_to_sign_with, 'str') # pylint:disable=protected-access
        if http_range is not None:
            header_parameters['Range'] = self._serialize.header("range", http_range, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=True, **kwargs) # pylint:disable=protected-access
        response = pipeline_response.http_response
        if response.status_code not in [200, 206]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)
        deserialized = response.stream_download(self._client._pipeline) # pylint:disable=protected-access

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized


    def get_url_to_sign_request_with(self,
        content_url # type: str
    ): # type: (...) -> str
        path = urlparse(content_url).path
        return self._config.endpoint + path
