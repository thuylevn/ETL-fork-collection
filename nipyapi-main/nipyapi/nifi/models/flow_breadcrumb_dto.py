# coding: utf-8

"""
    NiFi Rest API

    The Rest API provides programmatic access to command and control a NiFi instance in real time. Start and                                             stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.15.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class FlowBreadcrumbDTO(object):
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
        'id': 'str',
        'name': 'str',
        'version_control_information': 'VersionControlInformationDTO'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'version_control_information': 'versionControlInformation'
    }

    def __init__(self, id=None, name=None, version_control_information=None):
        """
        FlowBreadcrumbDTO - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._version_control_information = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if version_control_information is not None:
          self.version_control_information = version_control_information

    @property
    def id(self):
        """
        Gets the id of this FlowBreadcrumbDTO.
        The id of the group.

        :return: The id of this FlowBreadcrumbDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FlowBreadcrumbDTO.
        The id of the group.

        :param id: The id of this FlowBreadcrumbDTO.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this FlowBreadcrumbDTO.
        The id of the group.

        :return: The name of this FlowBreadcrumbDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FlowBreadcrumbDTO.
        The id of the group.

        :param name: The name of this FlowBreadcrumbDTO.
        :type: str
        """

        self._name = name

    @property
    def version_control_information(self):
        """
        Gets the version_control_information of this FlowBreadcrumbDTO.
        The process group version control information or null if not version controlled.

        :return: The version_control_information of this FlowBreadcrumbDTO.
        :rtype: VersionControlInformationDTO
        """
        return self._version_control_information

    @version_control_information.setter
    def version_control_information(self, version_control_information):
        """
        Sets the version_control_information of this FlowBreadcrumbDTO.
        The process group version control information or null if not version controlled.

        :param version_control_information: The version_control_information of this FlowBreadcrumbDTO.
        :type: VersionControlInformationDTO
        """

        self._version_control_information = version_control_information

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
        if not isinstance(other, FlowBreadcrumbDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other