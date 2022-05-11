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


class ExtensionMetadata(object):
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
        'link': 'JaxbLink',
        'name': 'str',
        'display_name': 'str',
        'type': 'str',
        'description': 'str',
        'deprecation_notice': 'DeprecationNotice',
        'tags': 'list[str]',
        'restricted': 'Restricted',
        'provided_service_ap_is': 'list[ProvidedServiceAPI]',
        'bundle_info': 'BundleInfo',
        'has_additional_details': 'bool',
        'link_docs': 'JaxbLink'
    }

    attribute_map = {
        'link': 'link',
        'name': 'name',
        'display_name': 'displayName',
        'type': 'type',
        'description': 'description',
        'deprecation_notice': 'deprecationNotice',
        'tags': 'tags',
        'restricted': 'restricted',
        'provided_service_ap_is': 'providedServiceAPIs',
        'bundle_info': 'bundleInfo',
        'has_additional_details': 'hasAdditionalDetails',
        'link_docs': 'linkDocs'
    }

    def __init__(self, link=None, name=None, display_name=None, type=None, description=None, deprecation_notice=None, tags=None, restricted=None, provided_service_ap_is=None, bundle_info=None, has_additional_details=None, link_docs=None):
        """
        ExtensionMetadata - a model defined in Swagger
        """

        self._link = None
        self._name = None
        self._display_name = None
        self._type = None
        self._description = None
        self._deprecation_notice = None
        self._tags = None
        self._restricted = None
        self._provided_service_ap_is = None
        self._bundle_info = None
        self._has_additional_details = None
        self._link_docs = None

        if link is not None:
          self.link = link
        if name is not None:
          self.name = name
        if display_name is not None:
          self.display_name = display_name
        if type is not None:
          self.type = type
        if description is not None:
          self.description = description
        if deprecation_notice is not None:
          self.deprecation_notice = deprecation_notice
        if tags is not None:
          self.tags = tags
        if restricted is not None:
          self.restricted = restricted
        if provided_service_ap_is is not None:
          self.provided_service_ap_is = provided_service_ap_is
        if bundle_info is not None:
          self.bundle_info = bundle_info
        if has_additional_details is not None:
          self.has_additional_details = has_additional_details
        if link_docs is not None:
          self.link_docs = link_docs

    @property
    def link(self):
        """
        Gets the link of this ExtensionMetadata.
        An WebLink to this entity.

        :return: The link of this ExtensionMetadata.
        :rtype: JaxbLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """
        Sets the link of this ExtensionMetadata.
        An WebLink to this entity.

        :param link: The link of this ExtensionMetadata.
        :type: JaxbLink
        """

        self._link = link

    @property
    def name(self):
        """
        Gets the name of this ExtensionMetadata.
        The name of the extension

        :return: The name of this ExtensionMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ExtensionMetadata.
        The name of the extension

        :param name: The name of this ExtensionMetadata.
        :type: str
        """

        self._name = name

    @property
    def display_name(self):
        """
        Gets the display_name of this ExtensionMetadata.
        The display name of the extension

        :return: The display_name of this ExtensionMetadata.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ExtensionMetadata.
        The display name of the extension

        :param display_name: The display_name of this ExtensionMetadata.
        :type: str
        """

        self._display_name = display_name

    @property
    def type(self):
        """
        Gets the type of this ExtensionMetadata.
        The type of the extension

        :return: The type of this ExtensionMetadata.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ExtensionMetadata.
        The type of the extension

        :param type: The type of this ExtensionMetadata.
        :type: str
        """
        allowed_values = ["PROCESSOR", "CONTROLLER_SERVICE", "REPORTING_TASK"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def description(self):
        """
        Gets the description of this ExtensionMetadata.
        The description of the extension

        :return: The description of this ExtensionMetadata.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ExtensionMetadata.
        The description of the extension

        :param description: The description of this ExtensionMetadata.
        :type: str
        """

        self._description = description

    @property
    def deprecation_notice(self):
        """
        Gets the deprecation_notice of this ExtensionMetadata.
        The deprecation notice of the extension

        :return: The deprecation_notice of this ExtensionMetadata.
        :rtype: DeprecationNotice
        """
        return self._deprecation_notice

    @deprecation_notice.setter
    def deprecation_notice(self, deprecation_notice):
        """
        Sets the deprecation_notice of this ExtensionMetadata.
        The deprecation notice of the extension

        :param deprecation_notice: The deprecation_notice of this ExtensionMetadata.
        :type: DeprecationNotice
        """

        self._deprecation_notice = deprecation_notice

    @property
    def tags(self):
        """
        Gets the tags of this ExtensionMetadata.
        The tags of the extension

        :return: The tags of this ExtensionMetadata.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this ExtensionMetadata.
        The tags of the extension

        :param tags: The tags of this ExtensionMetadata.
        :type: list[str]
        """

        self._tags = tags

    @property
    def restricted(self):
        """
        Gets the restricted of this ExtensionMetadata.
        The restrictions of the extension

        :return: The restricted of this ExtensionMetadata.
        :rtype: Restricted
        """
        return self._restricted

    @restricted.setter
    def restricted(self, restricted):
        """
        Sets the restricted of this ExtensionMetadata.
        The restrictions of the extension

        :param restricted: The restricted of this ExtensionMetadata.
        :type: Restricted
        """

        self._restricted = restricted

    @property
    def provided_service_ap_is(self):
        """
        Gets the provided_service_ap_is of this ExtensionMetadata.
        The service APIs provided by the extension

        :return: The provided_service_ap_is of this ExtensionMetadata.
        :rtype: list[ProvidedServiceAPI]
        """
        return self._provided_service_ap_is

    @provided_service_ap_is.setter
    def provided_service_ap_is(self, provided_service_ap_is):
        """
        Sets the provided_service_ap_is of this ExtensionMetadata.
        The service APIs provided by the extension

        :param provided_service_ap_is: The provided_service_ap_is of this ExtensionMetadata.
        :type: list[ProvidedServiceAPI]
        """

        self._provided_service_ap_is = provided_service_ap_is

    @property
    def bundle_info(self):
        """
        Gets the bundle_info of this ExtensionMetadata.
        The information for the bundle where this extension is located

        :return: The bundle_info of this ExtensionMetadata.
        :rtype: BundleInfo
        """
        return self._bundle_info

    @bundle_info.setter
    def bundle_info(self, bundle_info):
        """
        Sets the bundle_info of this ExtensionMetadata.
        The information for the bundle where this extension is located

        :param bundle_info: The bundle_info of this ExtensionMetadata.
        :type: BundleInfo
        """

        self._bundle_info = bundle_info

    @property
    def has_additional_details(self):
        """
        Gets the has_additional_details of this ExtensionMetadata.
        Whether or not the extension has additional detail documentation

        :return: The has_additional_details of this ExtensionMetadata.
        :rtype: bool
        """
        return self._has_additional_details

    @has_additional_details.setter
    def has_additional_details(self, has_additional_details):
        """
        Sets the has_additional_details of this ExtensionMetadata.
        Whether or not the extension has additional detail documentation

        :param has_additional_details: The has_additional_details of this ExtensionMetadata.
        :type: bool
        """

        self._has_additional_details = has_additional_details

    @property
    def link_docs(self):
        """
        Gets the link_docs of this ExtensionMetadata.
        A WebLink to the documentation for this extension.

        :return: The link_docs of this ExtensionMetadata.
        :rtype: JaxbLink
        """
        return self._link_docs

    @link_docs.setter
    def link_docs(self, link_docs):
        """
        Sets the link_docs of this ExtensionMetadata.
        A WebLink to the documentation for this extension.

        :param link_docs: The link_docs of this ExtensionMetadata.
        :type: JaxbLink
        """

        self._link_docs = link_docs

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
        if not isinstance(other, ExtensionMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
