# coding: utf-8

"""
    Apache NiFi Registry REST API

    The REST API provides an interface to a registry with operations for saving, versioning, reading NiFi flows and components.

    OpenAPI spec version: 1.15.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ControllerServiceAPI(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'type': 'str',
        'bundle': 'Bundle'
    }

    attribute_map = {
        'type': 'type',
        'bundle': 'bundle'
    }

    def __init__(self, type=None, bundle=None):
        """
        ControllerServiceAPI - a model defined in Swagger
        """

        self._type = None
        self._bundle = None

        if type is not None:
          self.type = type
        if bundle is not None:
          self.bundle = bundle

    @property
    def type(self):
        """
        Gets the type of this ControllerServiceAPI.
        The fully qualified name of the service interface.

        :return: The type of this ControllerServiceAPI.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ControllerServiceAPI.
        The fully qualified name of the service interface.

        :param type: The type of this ControllerServiceAPI.
        :type: str
        """

        self._type = type

    @property
    def bundle(self):
        """
        Gets the bundle of this ControllerServiceAPI.
        The details of the artifact that bundled this service interface.

        :return: The bundle of this ControllerServiceAPI.
        :rtype: Bundle
        """
        return self._bundle

    @bundle.setter
    def bundle(self, bundle):
        """
        Sets the bundle of this ControllerServiceAPI.
        The details of the artifact that bundled this service interface.

        :param bundle: The bundle of this ControllerServiceAPI.
        :type: Bundle
        """

        self._bundle = bundle

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ControllerServiceAPI):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
