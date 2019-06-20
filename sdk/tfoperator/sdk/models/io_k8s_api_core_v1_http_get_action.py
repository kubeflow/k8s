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
from tfoperator.sdk.models.io_k8s_api_core_v1_http_header import IoK8sApiCoreV1HTTPHeader  # noqa: F401,E501
from tfoperator.sdk.models.io_k8s_apimachinery_pkg_util_intstr_int_or_string import IoK8sApimachineryPkgUtilIntstrIntOrString  # noqa: F401,E501


class IoK8sApiCoreV1HTTPGetAction(object):
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
        'host': 'str',
        'http_headers': 'list[IoK8sApiCoreV1HTTPHeader]',
        'path': 'str',
        'port': 'IoK8sApimachineryPkgUtilIntstrIntOrString',
        'scheme': 'str'
    }

    attribute_map = {
        'host': 'host',
        'http_headers': 'httpHeaders',
        'path': 'path',
        'port': 'port',
        'scheme': 'scheme'
    }

    def __init__(self, host=None, http_headers=None, path=None, port=None, scheme=None):  # noqa: E501
        """IoK8sApiCoreV1HTTPGetAction - a model defined in Swagger"""  # noqa: E501
        self._host = None
        self._http_headers = None
        self._path = None
        self._port = None
        self._scheme = None
        self.discriminator = None
        if host is not None:
            self.host = host
        if http_headers is not None:
            self.http_headers = http_headers
        if path is not None:
            self.path = path
        self.port = port
        if scheme is not None:
            self.scheme = scheme

    @property
    def host(self):
        """Gets the host of this IoK8sApiCoreV1HTTPGetAction.  # noqa: E501

        Host name to connect to, defaults to the pod IP. You probably want to set \"Host\" in httpHeaders instead.  # noqa: E501

        :return: The host of this IoK8sApiCoreV1HTTPGetAction.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this IoK8sApiCoreV1HTTPGetAction.

        Host name to connect to, defaults to the pod IP. You probably want to set \"Host\" in httpHeaders instead.  # noqa: E501

        :param host: The host of this IoK8sApiCoreV1HTTPGetAction.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def http_headers(self):
        """Gets the http_headers of this IoK8sApiCoreV1HTTPGetAction.  # noqa: E501

        Custom headers to set in the request. HTTP allows repeated headers.  # noqa: E501

        :return: The http_headers of this IoK8sApiCoreV1HTTPGetAction.  # noqa: E501
        :rtype: list[IoK8sApiCoreV1HTTPHeader]
        """
        return self._http_headers

    @http_headers.setter
    def http_headers(self, http_headers):
        """Sets the http_headers of this IoK8sApiCoreV1HTTPGetAction.

        Custom headers to set in the request. HTTP allows repeated headers.  # noqa: E501

        :param http_headers: The http_headers of this IoK8sApiCoreV1HTTPGetAction.  # noqa: E501
        :type: list[IoK8sApiCoreV1HTTPHeader]
        """

        self._http_headers = http_headers

    @property
    def path(self):
        """Gets the path of this IoK8sApiCoreV1HTTPGetAction.  # noqa: E501

        Path to access on the HTTP server.  # noqa: E501

        :return: The path of this IoK8sApiCoreV1HTTPGetAction.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this IoK8sApiCoreV1HTTPGetAction.

        Path to access on the HTTP server.  # noqa: E501

        :param path: The path of this IoK8sApiCoreV1HTTPGetAction.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def port(self):
        """Gets the port of this IoK8sApiCoreV1HTTPGetAction.  # noqa: E501


        :return: The port of this IoK8sApiCoreV1HTTPGetAction.  # noqa: E501
        :rtype: IoK8sApimachineryPkgUtilIntstrIntOrString
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this IoK8sApiCoreV1HTTPGetAction.


        :param port: The port of this IoK8sApiCoreV1HTTPGetAction.  # noqa: E501
        :type: IoK8sApimachineryPkgUtilIntstrIntOrString
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def scheme(self):
        """Gets the scheme of this IoK8sApiCoreV1HTTPGetAction.  # noqa: E501

        Scheme to use for connecting to the host. Defaults to HTTP.  # noqa: E501

        :return: The scheme of this IoK8sApiCoreV1HTTPGetAction.  # noqa: E501
        :rtype: str
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        """Sets the scheme of this IoK8sApiCoreV1HTTPGetAction.

        Scheme to use for connecting to the host. Defaults to HTTP.  # noqa: E501

        :param scheme: The scheme of this IoK8sApiCoreV1HTTPGetAction.  # noqa: E501
        :type: str
        """

        self._scheme = scheme

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
        if issubclass(IoK8sApiCoreV1HTTPGetAction, dict):
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
        if not isinstance(other, IoK8sApiCoreV1HTTPGetAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
