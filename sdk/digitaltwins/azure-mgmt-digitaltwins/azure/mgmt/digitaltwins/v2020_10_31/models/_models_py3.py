# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._azure_digital_twins_management_client_enums import *


class CheckNameRequest(msrest.serialization.Model):
    """The result returned from a database check name availability request.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Resource name.
    :type name: str
    :ivar type: Required. The type of resource, for instance
     Microsoft.DigitalTwins/digitalTwinsInstances. Default value:
     "Microsoft.DigitalTwins/digitalTwinsInstances".
    :vartype type: str
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    type = "Microsoft.DigitalTwins/digitalTwinsInstances"

    def __init__(
        self,
        *,
        name: str,
        **kwargs
    ):
        super(CheckNameRequest, self).__init__(**kwargs)
        self.name = name


class CheckNameResult(msrest.serialization.Model):
    """The result returned from a check name availability request.

    :param name_available: Specifies a Boolean value that indicates if the name is available.
    :type name_available: bool
    :param message: Message indicating an unavailable name due to a conflict, or a description of
     the naming rules that are violated.
    :type message: str
    :param reason: Message providing the reason why the given name is invalid. Possible values
     include: "Invalid", "AlreadyExists".
    :type reason: str or ~azure.mgmt.digitaltwins.v2020_10_31.models.Reason
    """

    _attribute_map = {
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'message': {'key': 'message', 'type': 'str'},
        'reason': {'key': 'reason', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name_available: Optional[bool] = None,
        message: Optional[str] = None,
        reason: Optional[Union[str, "Reason"]] = None,
        **kwargs
    ):
        super(CheckNameResult, self).__init__(**kwargs)
        self.name_available = name_available
        self.message = message
        self.reason = reason


class DigitalTwinsResource(msrest.serialization.Model):
    """The common properties of a DigitalTwinsInstance.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The resource identifier.
    :vartype id: str
    :ivar name: The resource name.
    :vartype name: str
    :ivar type: The resource type.
    :vartype type: str
    :param location: Required. The resource location.
    :type location: str
    :param tags: A set of tags. The resource tags.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True, 'pattern': r'^(?!-)[A-Za-z0-9-]{3,63}(?<!-)$'},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(DigitalTwinsResource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = location
        self.tags = tags


class DigitalTwinsDescription(DigitalTwinsResource):
    """The description of the DigitalTwins service.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The resource identifier.
    :vartype id: str
    :ivar name: The resource name.
    :vartype name: str
    :ivar type: The resource type.
    :vartype type: str
    :param location: Required. The resource location.
    :type location: str
    :param tags: A set of tags. The resource tags.
    :type tags: dict[str, str]
    :ivar created_time: Time when DigitalTwinsInstance was created.
    :vartype created_time: ~datetime.datetime
    :ivar last_updated_time: Time when DigitalTwinsInstance was updated.
    :vartype last_updated_time: ~datetime.datetime
    :ivar provisioning_state: The provisioning state. Possible values include: "Provisioning",
     "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", "Warning", "Suspending", "Restoring",
     "Moving".
    :vartype provisioning_state: str or
     ~azure.mgmt.digitaltwins.v2020_10_31.models.ProvisioningState
    :ivar host_name: Api endpoint to work with DigitalTwinsInstance.
    :vartype host_name: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True, 'pattern': r'^(?!-)[A-Za-z0-9-]{3,63}(?<!-)$'},
        'type': {'readonly': True},
        'location': {'required': True},
        'created_time': {'readonly': True},
        'last_updated_time': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'host_name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'created_time': {'key': 'properties.createdTime', 'type': 'iso-8601'},
        'last_updated_time': {'key': 'properties.lastUpdatedTime', 'type': 'iso-8601'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'host_name': {'key': 'properties.hostName', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(DigitalTwinsDescription, self).__init__(location=location, tags=tags, **kwargs)
        self.created_time = None
        self.last_updated_time = None
        self.provisioning_state = None
        self.host_name = None


class DigitalTwinsDescriptionListResult(msrest.serialization.Model):
    """A list of DigitalTwins description objects with a next link.

    :param next_link: The link used to get the next page of DigitalTwins description objects.
    :type next_link: str
    :param value: A list of DigitalTwins description objects.
    :type value: list[~azure.mgmt.digitaltwins.v2020_10_31.models.DigitalTwinsDescription]
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'value': {'key': 'value', 'type': '[DigitalTwinsDescription]'},
    }

    def __init__(
        self,
        *,
        next_link: Optional[str] = None,
        value: Optional[List["DigitalTwinsDescription"]] = None,
        **kwargs
    ):
        super(DigitalTwinsDescriptionListResult, self).__init__(**kwargs)
        self.next_link = next_link
        self.value = value


class ExternalResource(msrest.serialization.Model):
    """Definition of a resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The resource identifier.
    :vartype id: str
    :ivar name: Extension resource name.
    :vartype name: str
    :ivar type: The resource type.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True, 'pattern': r'^(?![0-9]+$)(?!-)[a-zA-Z0-9-]{2,49}[a-zA-Z0-9]$'},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ExternalResource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class DigitalTwinsEndpointResource(ExternalResource):
    """DigitalTwinsInstance endpoint resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The resource identifier.
    :vartype id: str
    :ivar name: Extension resource name.
    :vartype name: str
    :ivar type: The resource type.
    :vartype type: str
    :param properties: Required. DigitalTwinsInstance endpoint resource properties.
    :type properties:
     ~azure.mgmt.digitaltwins.v2020_10_31.models.DigitalTwinsEndpointResourceProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True, 'pattern': r'^(?![0-9]+$)(?!-)[a-zA-Z0-9-]{2,49}[a-zA-Z0-9]$'},
        'type': {'readonly': True},
        'properties': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'DigitalTwinsEndpointResourceProperties'},
    }

    def __init__(
        self,
        *,
        properties: "DigitalTwinsEndpointResourceProperties",
        **kwargs
    ):
        super(DigitalTwinsEndpointResource, self).__init__(**kwargs)
        self.properties = properties


class DigitalTwinsEndpointResourceListResult(msrest.serialization.Model):
    """A list of DigitalTwinsInstance Endpoints with a next link.

    :param next_link: The link used to get the next page of DigitalTwinsInstance Endpoints.
    :type next_link: str
    :param value: A list of DigitalTwinsInstance Endpoints.
    :type value: list[~azure.mgmt.digitaltwins.v2020_10_31.models.DigitalTwinsEndpointResource]
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'value': {'key': 'value', 'type': '[DigitalTwinsEndpointResource]'},
    }

    def __init__(
        self,
        *,
        next_link: Optional[str] = None,
        value: Optional[List["DigitalTwinsEndpointResource"]] = None,
        **kwargs
    ):
        super(DigitalTwinsEndpointResourceListResult, self).__init__(**kwargs)
        self.next_link = next_link
        self.value = value


class DigitalTwinsEndpointResourceProperties(msrest.serialization.Model):
    """Properties related to Digital Twins Endpoint.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: EventGrid, EventHub, ServiceBus.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param endpoint_type: Required. The type of Digital Twins endpoint.Constant filled by server.
     Possible values include: "EventHub", "EventGrid", "ServiceBus".
    :type endpoint_type: str or ~azure.mgmt.digitaltwins.v2020_10_31.models.EndpointType
    :ivar provisioning_state: The provisioning state. Possible values include: "Provisioning",
     "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", "Warning", "Suspending", "Restoring",
     "Moving", "Disabled".
    :vartype provisioning_state: str or
     ~azure.mgmt.digitaltwins.v2020_10_31.models.EndpointProvisioningState
    :ivar created_time: Time when the Endpoint was added to DigitalTwinsInstance.
    :vartype created_time: ~datetime.datetime
    :param dead_letter_secret: Dead letter storage secret. Will be obfuscated during read.
    :type dead_letter_secret: str
    """

    _validation = {
        'endpoint_type': {'required': True},
        'provisioning_state': {'readonly': True},
        'created_time': {'readonly': True},
    }

    _attribute_map = {
        'endpoint_type': {'key': 'endpointType', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'created_time': {'key': 'createdTime', 'type': 'iso-8601'},
        'dead_letter_secret': {'key': 'deadLetterSecret', 'type': 'str'},
    }

    _subtype_map = {
        'endpoint_type': {'EventGrid': 'EventGrid', 'EventHub': 'EventHub', 'ServiceBus': 'ServiceBus'}
    }

    def __init__(
        self,
        *,
        dead_letter_secret: Optional[str] = None,
        **kwargs
    ):
        super(DigitalTwinsEndpointResourceProperties, self).__init__(**kwargs)
        self.endpoint_type = None  # type: Optional[str]
        self.provisioning_state = None
        self.created_time = None
        self.dead_letter_secret = dead_letter_secret


class DigitalTwinsPatchDescription(msrest.serialization.Model):
    """The description of the DigitalTwins service.

    :param tags: A set of tags. Instance tags.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(DigitalTwinsPatchDescription, self).__init__(**kwargs)
        self.tags = tags


class ErrorDefinition(msrest.serialization.Model):
    """Error definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: Service specific error code which serves as the substatus for the HTTP error code.
    :vartype code: str
    :ivar message: Description of the error.
    :vartype message: str
    :ivar details: Internal error details.
    :vartype details: list[~azure.mgmt.digitaltwins.v2020_10_31.models.ErrorDefinition]
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'details': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorDefinition]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorDefinition, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.details = None


class ErrorResponse(msrest.serialization.Model):
    """Error response.

    :param error: Error description.
    :type error: ~azure.mgmt.digitaltwins.v2020_10_31.models.ErrorDefinition
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDefinition'},
    }

    def __init__(
        self,
        *,
        error: Optional["ErrorDefinition"] = None,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = error


class EventGrid(DigitalTwinsEndpointResourceProperties):
    """Properties related to EventGrid.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param endpoint_type: Required. The type of Digital Twins endpoint.Constant filled by server.
     Possible values include: "EventHub", "EventGrid", "ServiceBus".
    :type endpoint_type: str or ~azure.mgmt.digitaltwins.v2020_10_31.models.EndpointType
    :ivar provisioning_state: The provisioning state. Possible values include: "Provisioning",
     "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", "Warning", "Suspending", "Restoring",
     "Moving", "Disabled".
    :vartype provisioning_state: str or
     ~azure.mgmt.digitaltwins.v2020_10_31.models.EndpointProvisioningState
    :ivar created_time: Time when the Endpoint was added to DigitalTwinsInstance.
    :vartype created_time: ~datetime.datetime
    :param dead_letter_secret: Dead letter storage secret. Will be obfuscated during read.
    :type dead_letter_secret: str
    :param topic_endpoint: Required. EventGrid Topic Endpoint.
    :type topic_endpoint: str
    :param access_key1: Required. EventGrid secondary accesskey. Will be obfuscated during read.
    :type access_key1: str
    :param access_key2: EventGrid secondary accesskey. Will be obfuscated during read.
    :type access_key2: str
    """

    _validation = {
        'endpoint_type': {'required': True},
        'provisioning_state': {'readonly': True},
        'created_time': {'readonly': True},
        'topic_endpoint': {'required': True},
        'access_key1': {'required': True},
    }

    _attribute_map = {
        'endpoint_type': {'key': 'endpointType', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'created_time': {'key': 'createdTime', 'type': 'iso-8601'},
        'dead_letter_secret': {'key': 'deadLetterSecret', 'type': 'str'},
        'topic_endpoint': {'key': 'TopicEndpoint', 'type': 'str'},
        'access_key1': {'key': 'accessKey1', 'type': 'str'},
        'access_key2': {'key': 'accessKey2', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        topic_endpoint: str,
        access_key1: str,
        dead_letter_secret: Optional[str] = None,
        access_key2: Optional[str] = None,
        **kwargs
    ):
        super(EventGrid, self).__init__(dead_letter_secret=dead_letter_secret, **kwargs)
        self.endpoint_type = 'EventGrid'  # type: str
        self.topic_endpoint = topic_endpoint
        self.access_key1 = access_key1
        self.access_key2 = access_key2


class EventHub(DigitalTwinsEndpointResourceProperties):
    """Properties related to EventHub.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param endpoint_type: Required. The type of Digital Twins endpoint.Constant filled by server.
     Possible values include: "EventHub", "EventGrid", "ServiceBus".
    :type endpoint_type: str or ~azure.mgmt.digitaltwins.v2020_10_31.models.EndpointType
    :ivar provisioning_state: The provisioning state. Possible values include: "Provisioning",
     "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", "Warning", "Suspending", "Restoring",
     "Moving", "Disabled".
    :vartype provisioning_state: str or
     ~azure.mgmt.digitaltwins.v2020_10_31.models.EndpointProvisioningState
    :ivar created_time: Time when the Endpoint was added to DigitalTwinsInstance.
    :vartype created_time: ~datetime.datetime
    :param dead_letter_secret: Dead letter storage secret. Will be obfuscated during read.
    :type dead_letter_secret: str
    :param connection_string_primary_key: Required. PrimaryConnectionString of the endpoint. Will
     be obfuscated during read.
    :type connection_string_primary_key: str
    :param connection_string_secondary_key: SecondaryConnectionString of the endpoint. Will be
     obfuscated during read.
    :type connection_string_secondary_key: str
    """

    _validation = {
        'endpoint_type': {'required': True},
        'provisioning_state': {'readonly': True},
        'created_time': {'readonly': True},
        'connection_string_primary_key': {'required': True},
    }

    _attribute_map = {
        'endpoint_type': {'key': 'endpointType', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'created_time': {'key': 'createdTime', 'type': 'iso-8601'},
        'dead_letter_secret': {'key': 'deadLetterSecret', 'type': 'str'},
        'connection_string_primary_key': {'key': 'connectionStringPrimaryKey', 'type': 'str'},
        'connection_string_secondary_key': {'key': 'connectionStringSecondaryKey', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        connection_string_primary_key: str,
        dead_letter_secret: Optional[str] = None,
        connection_string_secondary_key: Optional[str] = None,
        **kwargs
    ):
        super(EventHub, self).__init__(dead_letter_secret=dead_letter_secret, **kwargs)
        self.endpoint_type = 'EventHub'  # type: str
        self.connection_string_primary_key = connection_string_primary_key
        self.connection_string_secondary_key = connection_string_secondary_key


class Operation(msrest.serialization.Model):
    """DigitalTwins service REST API operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: Operation name: {provider}/{resource}/{read | write | action | delete}.
    :vartype name: str
    :param display: Operation properties display.
    :type display: ~azure.mgmt.digitaltwins.v2020_10_31.models.OperationDisplay
    :ivar origin: The intended executor of the operation.
    :vartype origin: str
    :ivar is_data_action: If the operation is a data action (for data plane rbac).
    :vartype is_data_action: bool
    """

    _validation = {
        'name': {'readonly': True},
        'origin': {'readonly': True},
        'is_data_action': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
        'origin': {'key': 'origin', 'type': 'str'},
        'is_data_action': {'key': 'isDataAction', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        display: Optional["OperationDisplay"] = None,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = None
        self.display = display
        self.origin = None
        self.is_data_action = None


class OperationDisplay(msrest.serialization.Model):
    """The object that represents the operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar provider: Service provider: Microsoft DigitalTwins.
    :vartype provider: str
    :ivar resource: Resource Type: DigitalTwinsInstances.
    :vartype resource: str
    :ivar operation: Name of the operation.
    :vartype operation: str
    :ivar description: Friendly description for the operation,.
    :vartype description: str
    """

    _validation = {
        'provider': {'readonly': True},
        'resource': {'readonly': True},
        'operation': {'readonly': True},
        'description': {'readonly': True},
    }

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = None
        self.resource = None
        self.operation = None
        self.description = None


class OperationListResult(msrest.serialization.Model):
    """A list of DigitalTwins service operations. It contains a list of operations and a URL link to get the next set of results.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param next_link: The link used to get the next page of DigitalTwins description objects.
    :type next_link: str
    :ivar value: A list of DigitalTwins operations supported by the Microsoft.DigitalTwins resource
     provider.
    :vartype value: list[~azure.mgmt.digitaltwins.v2020_10_31.models.Operation]
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'value': {'key': 'value', 'type': '[Operation]'},
    }

    def __init__(
        self,
        *,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(OperationListResult, self).__init__(**kwargs)
        self.next_link = next_link
        self.value = None


class ServiceBus(DigitalTwinsEndpointResourceProperties):
    """Properties related to ServiceBus.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param endpoint_type: Required. The type of Digital Twins endpoint.Constant filled by server.
     Possible values include: "EventHub", "EventGrid", "ServiceBus".
    :type endpoint_type: str or ~azure.mgmt.digitaltwins.v2020_10_31.models.EndpointType
    :ivar provisioning_state: The provisioning state. Possible values include: "Provisioning",
     "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", "Warning", "Suspending", "Restoring",
     "Moving", "Disabled".
    :vartype provisioning_state: str or
     ~azure.mgmt.digitaltwins.v2020_10_31.models.EndpointProvisioningState
    :ivar created_time: Time when the Endpoint was added to DigitalTwinsInstance.
    :vartype created_time: ~datetime.datetime
    :param dead_letter_secret: Dead letter storage secret. Will be obfuscated during read.
    :type dead_letter_secret: str
    :param primary_connection_string: Required. PrimaryConnectionString of the endpoint. Will be
     obfuscated during read.
    :type primary_connection_string: str
    :param secondary_connection_string: SecondaryConnectionString of the endpoint. Will be
     obfuscated during read.
    :type secondary_connection_string: str
    """

    _validation = {
        'endpoint_type': {'required': True},
        'provisioning_state': {'readonly': True},
        'created_time': {'readonly': True},
        'primary_connection_string': {'required': True},
    }

    _attribute_map = {
        'endpoint_type': {'key': 'endpointType', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'created_time': {'key': 'createdTime', 'type': 'iso-8601'},
        'dead_letter_secret': {'key': 'deadLetterSecret', 'type': 'str'},
        'primary_connection_string': {'key': 'primaryConnectionString', 'type': 'str'},
        'secondary_connection_string': {'key': 'secondaryConnectionString', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        primary_connection_string: str,
        dead_letter_secret: Optional[str] = None,
        secondary_connection_string: Optional[str] = None,
        **kwargs
    ):
        super(ServiceBus, self).__init__(dead_letter_secret=dead_letter_secret, **kwargs)
        self.endpoint_type = 'ServiceBus'  # type: str
        self.primary_connection_string = primary_connection_string
        self.secondary_connection_string = secondary_connection_string
