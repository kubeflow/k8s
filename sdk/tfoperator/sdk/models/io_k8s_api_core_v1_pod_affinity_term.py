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
from tfoperator.sdk.models.io_k8s_apimachinery_pkg_apis_meta_v1_label_selector import IoK8sApimachineryPkgApisMetaV1LabelSelector  # noqa: F401,E501


class IoK8sApiCoreV1PodAffinityTerm(object):
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
        'label_selector': 'IoK8sApimachineryPkgApisMetaV1LabelSelector',
        'namespaces': 'list[str]',
        'topology_key': 'str'
    }

    attribute_map = {
        'label_selector': 'labelSelector',
        'namespaces': 'namespaces',
        'topology_key': 'topologyKey'
    }

    def __init__(self, label_selector=None, namespaces=None, topology_key=None):  # noqa: E501
        """IoK8sApiCoreV1PodAffinityTerm - a model defined in Swagger"""  # noqa: E501
        self._label_selector = None
        self._namespaces = None
        self._topology_key = None
        self.discriminator = None
        if label_selector is not None:
            self.label_selector = label_selector
        if namespaces is not None:
            self.namespaces = namespaces
        self.topology_key = topology_key

    @property
    def label_selector(self):
        """Gets the label_selector of this IoK8sApiCoreV1PodAffinityTerm.  # noqa: E501


        :return: The label_selector of this IoK8sApiCoreV1PodAffinityTerm.  # noqa: E501
        :rtype: IoK8sApimachineryPkgApisMetaV1LabelSelector
        """
        return self._label_selector

    @label_selector.setter
    def label_selector(self, label_selector):
        """Sets the label_selector of this IoK8sApiCoreV1PodAffinityTerm.


        :param label_selector: The label_selector of this IoK8sApiCoreV1PodAffinityTerm.  # noqa: E501
        :type: IoK8sApimachineryPkgApisMetaV1LabelSelector
        """

        self._label_selector = label_selector

    @property
    def namespaces(self):
        """Gets the namespaces of this IoK8sApiCoreV1PodAffinityTerm.  # noqa: E501

        namespaces specifies which namespaces the labelSelector applies to (matches against); null or empty list means \"this pod's namespace\"  # noqa: E501

        :return: The namespaces of this IoK8sApiCoreV1PodAffinityTerm.  # noqa: E501
        :rtype: list[str]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        """Sets the namespaces of this IoK8sApiCoreV1PodAffinityTerm.

        namespaces specifies which namespaces the labelSelector applies to (matches against); null or empty list means \"this pod's namespace\"  # noqa: E501

        :param namespaces: The namespaces of this IoK8sApiCoreV1PodAffinityTerm.  # noqa: E501
        :type: list[str]
        """

        self._namespaces = namespaces

    @property
    def topology_key(self):
        """Gets the topology_key of this IoK8sApiCoreV1PodAffinityTerm.  # noqa: E501

        This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.  # noqa: E501

        :return: The topology_key of this IoK8sApiCoreV1PodAffinityTerm.  # noqa: E501
        :rtype: str
        """
        return self._topology_key

    @topology_key.setter
    def topology_key(self, topology_key):
        """Sets the topology_key of this IoK8sApiCoreV1PodAffinityTerm.

        This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.  # noqa: E501

        :param topology_key: The topology_key of this IoK8sApiCoreV1PodAffinityTerm.  # noqa: E501
        :type: str
        """
        if topology_key is None:
            raise ValueError("Invalid value for `topology_key`, must not be `None`")  # noqa: E501

        self._topology_key = topology_key

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
        if issubclass(IoK8sApiCoreV1PodAffinityTerm, dict):
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
        if not isinstance(other, IoK8sApiCoreV1PodAffinityTerm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
