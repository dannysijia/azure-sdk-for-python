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


class ApplicationUpgradeProgressInfo(Model):
    """Describes the parameters for an application upgrade.

    :param name:
    :type name: str
    :param type_name:
    :type type_name: str
    :param target_application_type_version:
    :type target_application_type_version: str
    :param upgrade_domains:
    :type upgrade_domains: list of :class:`UpgradeDomainInfo
     <azure.servicefabric.models.UpgradeDomainInfo>`
    :param upgrade_state: Possible values include: 'Invalid',
     'RollingBackInProgress', 'RollingBackCompleted', 'RollingForwardPending',
     'RollingForwardInProgress', 'RollingForwardCompleted', 'Failed'
    :type upgrade_state: str or :class:`enum
     <azure.servicefabric.models.enum>`
    :param next_upgrade_domain:
    :type next_upgrade_domain: str
    :param rolling_upgrade_mode: Possible values include: 'Invalid',
     'UnmonitoredAuto', 'UnmonitoredManual', 'Monitored'. Default value:
     "UnmonitoredAuto" .
    :type rolling_upgrade_mode: str or :class:`enum
     <azure.servicefabric.models.enum>`
    :param upgrade_description:
    :type upgrade_description: :class:`ApplicationUpgradeDescription
     <azure.servicefabric.models.ApplicationUpgradeDescription>`
    :param upgrade_duration_in_milliseconds: The estimated total amount of
     time spent processing the overall upgrade.
    :type upgrade_duration_in_milliseconds: str
    :param upgrade_domain_duration_in_milliseconds: The estimated total amount
     of time spent processing the current upgrade domain.
    :type upgrade_domain_duration_in_milliseconds: str
    :param unhealthy_evaluations:
    :type unhealthy_evaluations: list of :class:`HealthEvaluationWrapper
     <azure.servicefabric.models.HealthEvaluationWrapper>`
    :param current_upgrade_domain_progress:
    :type current_upgrade_domain_progress:
     :class:`CurrentUpgradeDomainProgressInfo
     <azure.servicefabric.models.CurrentUpgradeDomainProgressInfo>`
    :param start_timestamp_utc: The estimated UTC datetime when the upgrade
     started.
    :type start_timestamp_utc: str
    :param failure_timestamp_utc: The estimated UTC datetime when the upgrade
     failed and FailureAction was executed.
    :type failure_timestamp_utc: str
    :param failure_reason: Possible values include: 'None', 'Interrupted',
     'HealthCheck', 'UpgradeDomainTimeout', 'UpgradeTimeout'
    :type failure_reason: str or :class:`enum
     <azure.servicefabric.models.enum>`
    :param upgrade_domain_progress_at_failure:
    :type upgrade_domain_progress_at_failure:
     :class:`FailureUpgradeDomainProgressInfo
     <azure.servicefabric.models.FailureUpgradeDomainProgressInfo>`
    :param upgrade_status_details: Additional detailed information about the
     status of the pending upgrade.
    :type upgrade_status_details: str
    """

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'type_name': {'key': 'TypeName', 'type': 'str'},
        'target_application_type_version': {'key': 'TargetApplicationTypeVersion', 'type': 'str'},
        'upgrade_domains': {'key': 'UpgradeDomains', 'type': '[UpgradeDomainInfo]'},
        'upgrade_state': {'key': 'UpgradeState', 'type': 'str'},
        'next_upgrade_domain': {'key': 'NextUpgradeDomain', 'type': 'str'},
        'rolling_upgrade_mode': {'key': 'RollingUpgradeMode', 'type': 'str'},
        'upgrade_description': {'key': 'UpgradeDescription', 'type': 'ApplicationUpgradeDescription'},
        'upgrade_duration_in_milliseconds': {'key': 'UpgradeDurationInMilliseconds', 'type': 'str'},
        'upgrade_domain_duration_in_milliseconds': {'key': 'UpgradeDomainDurationInMilliseconds', 'type': 'str'},
        'unhealthy_evaluations': {'key': 'UnhealthyEvaluations', 'type': '[HealthEvaluationWrapper]'},
        'current_upgrade_domain_progress': {'key': 'CurrentUpgradeDomainProgress', 'type': 'CurrentUpgradeDomainProgressInfo'},
        'start_timestamp_utc': {'key': 'StartTimestampUtc', 'type': 'str'},
        'failure_timestamp_utc': {'key': 'FailureTimestampUtc', 'type': 'str'},
        'failure_reason': {'key': 'FailureReason', 'type': 'str'},
        'upgrade_domain_progress_at_failure': {'key': 'UpgradeDomainProgressAtFailure', 'type': 'FailureUpgradeDomainProgressInfo'},
        'upgrade_status_details': {'key': 'UpgradeStatusDetails', 'type': 'str'},
    }

    def __init__(self, name=None, type_name=None, target_application_type_version=None, upgrade_domains=None, upgrade_state=None, next_upgrade_domain=None, rolling_upgrade_mode="UnmonitoredAuto", upgrade_description=None, upgrade_duration_in_milliseconds=None, upgrade_domain_duration_in_milliseconds=None, unhealthy_evaluations=None, current_upgrade_domain_progress=None, start_timestamp_utc=None, failure_timestamp_utc=None, failure_reason=None, upgrade_domain_progress_at_failure=None, upgrade_status_details=None):
        self.name = name
        self.type_name = type_name
        self.target_application_type_version = target_application_type_version
        self.upgrade_domains = upgrade_domains
        self.upgrade_state = upgrade_state
        self.next_upgrade_domain = next_upgrade_domain
        self.rolling_upgrade_mode = rolling_upgrade_mode
        self.upgrade_description = upgrade_description
        self.upgrade_duration_in_milliseconds = upgrade_duration_in_milliseconds
        self.upgrade_domain_duration_in_milliseconds = upgrade_domain_duration_in_milliseconds
        self.unhealthy_evaluations = unhealthy_evaluations
        self.current_upgrade_domain_progress = current_upgrade_domain_progress
        self.start_timestamp_utc = start_timestamp_utc
        self.failure_timestamp_utc = failure_timestamp_utc
        self.failure_reason = failure_reason
        self.upgrade_domain_progress_at_failure = upgrade_domain_progress_at_failure
        self.upgrade_status_details = upgrade_status_details
