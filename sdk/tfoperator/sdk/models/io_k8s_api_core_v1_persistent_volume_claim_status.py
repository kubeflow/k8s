# coding: utf-8

"""
    TFOpeartor

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v0.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from tfoperator.sdk.models.io_k8s_api_core_v1_persistent_volume_claim_condition import IoK8sApiCoreV1PersistentVolumeClaimCondition  # noqa: F401,E501
from tfoperator.sdk.models.io_k8s_apimachinery_pkg_api_resource_quantity import IoK8sApimachineryPkgApiResourceQuantity  # noqa: F401,E501


class IoK8sApiCoreV1PersistentVolumeClaimStatus(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'access_modes': 'list[str]',
        'capacity': 'dict(str, IoK8sApimachineryPkgApiResourceQuantity)',
        'conditions': 'list[IoK8sApiCoreV1PersistentVolumeClaimCondition]',
        'phase': 'str'
    }

    attribute_map = {
        'access_modes': 'accessModes',
        'capacity': 'capacity',
        'conditions': 'conditions',
        'phase': 'phase'
    }

    def __init__(self, access_modes=None, capacity=None, conditions=None, phase=None):  # noqa: E501
        """IoK8sApiCoreV1PersistentVolumeClaimStatus - a model defined in Swagger"""  # noqa: E501
        self._access_modes = None
        self._capacity = None
        self._conditions = None
        self._phase = None
        self.discriminator = None
        if access_modes is not None:
            self.access_modes = access_modes
        if capacity is not None:
            self.capacity = capacity
        if conditions is not None:
            self.conditions = conditions
        if phase is not None:
            self.phase = phase

    @property
    def access_modes(self):
        """Gets the access_modes of this IoK8sApiCoreV1PersistentVolumeClaimStatus.  # noqa: E501

        AccessModes contains the actual access modes the volume backing the PVC has. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1  # noqa: E501

        :return: The access_modes of this IoK8sApiCoreV1PersistentVolumeClaimStatus.  # noqa: E501
        :rtype: list[str]
        """
        return self._access_modes

    @access_modes.setter
    def access_modes(self, access_modes):
        """Sets the access_modes of this IoK8sApiCoreV1PersistentVolumeClaimStatus.

        AccessModes contains the actual access modes the volume backing the PVC has. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1  # noqa: E501

        :param access_modes: The access_modes of this IoK8sApiCoreV1PersistentVolumeClaimStatus.  # noqa: E501
        :type: list[str]
        """

        self._access_modes = access_modes

    @property
    def capacity(self):
        """Gets the capacity of this IoK8sApiCoreV1PersistentVolumeClaimStatus.  # noqa: E501

        Represents the actual resources of the underlying volume.  # noqa: E501

        :return: The capacity of this IoK8sApiCoreV1PersistentVolumeClaimStatus.  # noqa: E501
        :rtype: dict(str, IoK8sApimachineryPkgApiResourceQuantity)
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this IoK8sApiCoreV1PersistentVolumeClaimStatus.

        Represents the actual resources of the underlying volume.  # noqa: E501

        :param capacity: The capacity of this IoK8sApiCoreV1PersistentVolumeClaimStatus.  # noqa: E501
        :type: dict(str, IoK8sApimachineryPkgApiResourceQuantity)
        """

        self._capacity = capacity

    @property
    def conditions(self):
        """Gets the conditions of this IoK8sApiCoreV1PersistentVolumeClaimStatus.  # noqa: E501

        Current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'ResizeStarted'.  # noqa: E501

        :return: The conditions of this IoK8sApiCoreV1PersistentVolumeClaimStatus.  # noqa: E501
        :rtype: list[IoK8sApiCoreV1PersistentVolumeClaimCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this IoK8sApiCoreV1PersistentVolumeClaimStatus.

        Current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'ResizeStarted'.  # noqa: E501

        :param conditions: The conditions of this IoK8sApiCoreV1PersistentVolumeClaimStatus.  # noqa: E501
        :type: list[IoK8sApiCoreV1PersistentVolumeClaimCondition]
        """

        self._conditions = conditions

    @property
    def phase(self):
        """Gets the phase of this IoK8sApiCoreV1PersistentVolumeClaimStatus.  # noqa: E501

        Phase represents the current phase of PersistentVolumeClaim.  # noqa: E501

        :return: The phase of this IoK8sApiCoreV1PersistentVolumeClaimStatus.  # noqa: E501
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this IoK8sApiCoreV1PersistentVolumeClaimStatus.

        Phase represents the current phase of PersistentVolumeClaim.  # noqa: E501

        :param phase: The phase of this IoK8sApiCoreV1PersistentVolumeClaimStatus.  # noqa: E501
        :type: str
        """

        self._phase = phase

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(IoK8sApiCoreV1PersistentVolumeClaimStatus, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IoK8sApiCoreV1PersistentVolumeClaimStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
