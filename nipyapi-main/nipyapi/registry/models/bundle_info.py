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


class BundleInfo(object):
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
        'bucket_id': 'str',
        'bucket_name': 'str',
        'bundle_id': 'str',
        'bundle_type': 'str',
        'group_id': 'str',
        'artifact_id': 'str',
        'version': 'str',
        'system_api_version': 'str'
    }

    attribute_map = {
        'bucket_id': 'bucketId',
        'bucket_name': 'bucketName',
        'bundle_id': 'bundleId',
        'bundle_type': 'bundleType',
        'group_id': 'groupId',
        'artifact_id': 'artifactId',
        'version': 'version',
        'system_api_version': 'systemApiVersion'
    }

    def __init__(self, bucket_id=None, bucket_name=None, bundle_id=None, bundle_type=None, group_id=None, artifact_id=None, version=None, system_api_version=None):
        """
        BundleInfo - a model defined in Swagger
        """

        self._bucket_id = None
        self._bucket_name = None
        self._bundle_id = None
        self._bundle_type = None
        self._group_id = None
        self._artifact_id = None
        self._version = None
        self._system_api_version = None

        if bucket_id is not None:
          self.bucket_id = bucket_id
        if bucket_name is not None:
          self.bucket_name = bucket_name
        if bundle_id is not None:
          self.bundle_id = bundle_id
        if bundle_type is not None:
          self.bundle_type = bundle_type
        if group_id is not None:
          self.group_id = group_id
        if artifact_id is not None:
          self.artifact_id = artifact_id
        if version is not None:
          self.version = version
        if system_api_version is not None:
          self.system_api_version = system_api_version

    @property
    def bucket_id(self):
        """
        Gets the bucket_id of this BundleInfo.
        The id of the bucket where the bundle is located

        :return: The bucket_id of this BundleInfo.
        :rtype: str
        """
        return self._bucket_id

    @bucket_id.setter
    def bucket_id(self, bucket_id):
        """
        Sets the bucket_id of this BundleInfo.
        The id of the bucket where the bundle is located

        :param bucket_id: The bucket_id of this BundleInfo.
        :type: str
        """

        self._bucket_id = bucket_id

    @property
    def bucket_name(self):
        """
        Gets the bucket_name of this BundleInfo.
        The name of the bucket where the bundle is located

        :return: The bucket_name of this BundleInfo.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this BundleInfo.
        The name of the bucket where the bundle is located

        :param bucket_name: The bucket_name of this BundleInfo.
        :type: str
        """

        self._bucket_name = bucket_name

    @property
    def bundle_id(self):
        """
        Gets the bundle_id of this BundleInfo.
        The id of the bundle

        :return: The bundle_id of this BundleInfo.
        :rtype: str
        """
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, bundle_id):
        """
        Sets the bundle_id of this BundleInfo.
        The id of the bundle

        :param bundle_id: The bundle_id of this BundleInfo.
        :type: str
        """

        self._bundle_id = bundle_id

    @property
    def bundle_type(self):
        """
        Gets the bundle_type of this BundleInfo.
        The type of bundle (i.e. a NiFi NAR vs MiNiFi CPP)

        :return: The bundle_type of this BundleInfo.
        :rtype: str
        """
        return self._bundle_type

    @bundle_type.setter
    def bundle_type(self, bundle_type):
        """
        Sets the bundle_type of this BundleInfo.
        The type of bundle (i.e. a NiFi NAR vs MiNiFi CPP)

        :param bundle_type: The bundle_type of this BundleInfo.
        :type: str
        """
        allowed_values = ["NIFI_NAR", "MINIFI_CPP"]
        if bundle_type not in allowed_values:
            raise ValueError(
                "Invalid value for `bundle_type` ({0}), must be one of {1}"
                .format(bundle_type, allowed_values)
            )

        self._bundle_type = bundle_type

    @property
    def group_id(self):
        """
        Gets the group_id of this BundleInfo.
        The group id of the bundle

        :return: The group_id of this BundleInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this BundleInfo.
        The group id of the bundle

        :param group_id: The group_id of this BundleInfo.
        :type: str
        """

        self._group_id = group_id

    @property
    def artifact_id(self):
        """
        Gets the artifact_id of this BundleInfo.
        The artifact id of the bundle

        :return: The artifact_id of this BundleInfo.
        :rtype: str
        """
        return self._artifact_id

    @artifact_id.setter
    def artifact_id(self, artifact_id):
        """
        Sets the artifact_id of this BundleInfo.
        The artifact id of the bundle

        :param artifact_id: The artifact_id of this BundleInfo.
        :type: str
        """

        self._artifact_id = artifact_id

    @property
    def version(self):
        """
        Gets the version of this BundleInfo.
        The version of the bundle

        :return: The version of this BundleInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this BundleInfo.
        The version of the bundle

        :param version: The version of this BundleInfo.
        :type: str
        """

        self._version = version

    @property
    def system_api_version(self):
        """
        Gets the system_api_version of this BundleInfo.
        The version of the system API the bundle was built against

        :return: The system_api_version of this BundleInfo.
        :rtype: str
        """
        return self._system_api_version

    @system_api_version.setter
    def system_api_version(self, system_api_version):
        """
        Sets the system_api_version of this BundleInfo.
        The version of the system API the bundle was built against

        :param system_api_version: The system_api_version of this BundleInfo.
        :type: str
        """

        self._system_api_version = system_api_version

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
        if not isinstance(other, BundleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
