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
from tfoperator.sdk.models.io_k8s_api_core_v1_container_state_running import IoK8sApiCoreV1ContainerStateRunning  # noqa: F401,E501
from tfoperator.sdk.models.io_k8s_api_core_v1_container_state_terminated import IoK8sApiCoreV1ContainerStateTerminated  # noqa: F401,E501
from tfoperator.sdk.models.io_k8s_api_core_v1_container_state_waiting import IoK8sApiCoreV1ContainerStateWaiting  # noqa: F401,E501


class IoK8sApiCoreV1ContainerState(object):
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
        'running': 'IoK8sApiCoreV1ContainerStateRunning',
        'terminated': 'IoK8sApiCoreV1ContainerStateTerminated',
        'waiting': 'IoK8sApiCoreV1ContainerStateWaiting'
    }

    attribute_map = {
        'running': 'running',
        'terminated': 'terminated',
        'waiting': 'waiting'
    }

    def __init__(self, running=None, terminated=None, waiting=None):  # noqa: E501
        """IoK8sApiCoreV1ContainerState - a model defined in Swagger"""  # noqa: E501
        self._running = None
        self._terminated = None
        self._waiting = None
        self.discriminator = None
        if running is not None:
            self.running = running
        if terminated is not None:
            self.terminated = terminated
        if waiting is not None:
            self.waiting = waiting

    @property
    def running(self):
        """Gets the running of this IoK8sApiCoreV1ContainerState.  # noqa: E501


        :return: The running of this IoK8sApiCoreV1ContainerState.  # noqa: E501
        :rtype: IoK8sApiCoreV1ContainerStateRunning
        """
        return self._running

    @running.setter
    def running(self, running):
        """Sets the running of this IoK8sApiCoreV1ContainerState.


        :param running: The running of this IoK8sApiCoreV1ContainerState.  # noqa: E501
        :type: IoK8sApiCoreV1ContainerStateRunning
        """

        self._running = running

    @property
    def terminated(self):
        """Gets the terminated of this IoK8sApiCoreV1ContainerState.  # noqa: E501


        :return: The terminated of this IoK8sApiCoreV1ContainerState.  # noqa: E501
        :rtype: IoK8sApiCoreV1ContainerStateTerminated
        """
        return self._terminated

    @terminated.setter
    def terminated(self, terminated):
        """Sets the terminated of this IoK8sApiCoreV1ContainerState.


        :param terminated: The terminated of this IoK8sApiCoreV1ContainerState.  # noqa: E501
        :type: IoK8sApiCoreV1ContainerStateTerminated
        """

        self._terminated = terminated

    @property
    def waiting(self):
        """Gets the waiting of this IoK8sApiCoreV1ContainerState.  # noqa: E501


        :return: The waiting of this IoK8sApiCoreV1ContainerState.  # noqa: E501
        :rtype: IoK8sApiCoreV1ContainerStateWaiting
        """
        return self._waiting

    @waiting.setter
    def waiting(self, waiting):
        """Sets the waiting of this IoK8sApiCoreV1ContainerState.


        :param waiting: The waiting of this IoK8sApiCoreV1ContainerState.  # noqa: E501
        :type: IoK8sApiCoreV1ContainerStateWaiting
        """

        self._waiting = waiting

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
        if issubclass(IoK8sApiCoreV1ContainerState, dict):
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
        if not isinstance(other, IoK8sApiCoreV1ContainerState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
