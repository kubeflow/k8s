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


class IoK8sApiCoreV1PhotonPersistentDiskVolumeSource(object):
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
        'fs_type': 'str',
        'pd_id': 'str'
    }

    attribute_map = {
        'fs_type': 'fsType',
        'pd_id': 'pdID'
    }

    def __init__(self, fs_type=None, pd_id=None):  # noqa: E501
        """IoK8sApiCoreV1PhotonPersistentDiskVolumeSource - a model defined in Swagger"""  # noqa: E501
        self._fs_type = None
        self._pd_id = None
        self.discriminator = None
        if fs_type is not None:
            self.fs_type = fs_type
        self.pd_id = pd_id

    @property
    def fs_type(self):
        """Gets the fs_type of this IoK8sApiCoreV1PhotonPersistentDiskVolumeSource.  # noqa: E501

        Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified.  # noqa: E501

        :return: The fs_type of this IoK8sApiCoreV1PhotonPersistentDiskVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._fs_type

    @fs_type.setter
    def fs_type(self, fs_type):
        """Sets the fs_type of this IoK8sApiCoreV1PhotonPersistentDiskVolumeSource.

        Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified.  # noqa: E501

        :param fs_type: The fs_type of this IoK8sApiCoreV1PhotonPersistentDiskVolumeSource.  # noqa: E501
        :type: str
        """

        self._fs_type = fs_type

    @property
    def pd_id(self):
        """Gets the pd_id of this IoK8sApiCoreV1PhotonPersistentDiskVolumeSource.  # noqa: E501

        ID that identifies Photon Controller persistent disk  # noqa: E501

        :return: The pd_id of this IoK8sApiCoreV1PhotonPersistentDiskVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._pd_id

    @pd_id.setter
    def pd_id(self, pd_id):
        """Sets the pd_id of this IoK8sApiCoreV1PhotonPersistentDiskVolumeSource.

        ID that identifies Photon Controller persistent disk  # noqa: E501

        :param pd_id: The pd_id of this IoK8sApiCoreV1PhotonPersistentDiskVolumeSource.  # noqa: E501
        :type: str
        """
        if pd_id is None:
            raise ValueError("Invalid value for `pd_id`, must not be `None`")  # noqa: E501

        self._pd_id = pd_id

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
        if issubclass(IoK8sApiCoreV1PhotonPersistentDiskVolumeSource, dict):
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
        if not isinstance(other, IoK8sApiCoreV1PhotonPersistentDiskVolumeSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
