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


class ProcessGroupFlowEntity(object):
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
        'permissions': 'PermissionsDTO',
        'process_group_flow': 'ProcessGroupFlowDTO'
    }

    attribute_map = {
        'permissions': 'permissions',
        'process_group_flow': 'processGroupFlow'
    }

    def __init__(self, permissions=None, process_group_flow=None):
        """
        ProcessGroupFlowEntity - a model defined in Swagger
        """

        self._permissions = None
        self._process_group_flow = None

        if permissions is not None:
          self.permissions = permissions
        if process_group_flow is not None:
          self.process_group_flow = process_group_flow

    @property
    def permissions(self):
        """
        Gets the permissions of this ProcessGroupFlowEntity.
        The access policy for this process group.

        :return: The permissions of this ProcessGroupFlowEntity.
        :rtype: PermissionsDTO
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """
        Sets the permissions of this ProcessGroupFlowEntity.
        The access policy for this process group.

        :param permissions: The permissions of this ProcessGroupFlowEntity.
        :type: PermissionsDTO
        """

        self._permissions = permissions

    @property
    def process_group_flow(self):
        """
        Gets the process_group_flow of this ProcessGroupFlowEntity.

        :return: The process_group_flow of this ProcessGroupFlowEntity.
        :rtype: ProcessGroupFlowDTO
        """
        return self._process_group_flow

    @process_group_flow.setter
    def process_group_flow(self, process_group_flow):
        """
        Sets the process_group_flow of this ProcessGroupFlowEntity.

        :param process_group_flow: The process_group_flow of this ProcessGroupFlowEntity.
        :type: ProcessGroupFlowDTO
        """

        self._process_group_flow = process_group_flow

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
        if not isinstance(other, ProcessGroupFlowEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
