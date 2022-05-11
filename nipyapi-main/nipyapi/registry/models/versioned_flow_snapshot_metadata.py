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


class VersionedFlowSnapshotMetadata(object):
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
        'bucket_identifier': 'str',
        'flow_identifier': 'str',
        'version': 'int',
        'timestamp': 'int',
        'author': 'str',
        'comments': 'str'
    }

    attribute_map = {
        'link': 'link',
        'bucket_identifier': 'bucketIdentifier',
        'flow_identifier': 'flowIdentifier',
        'version': 'version',
        'timestamp': 'timestamp',
        'author': 'author',
        'comments': 'comments'
    }

    def __init__(self, link=None, bucket_identifier=None, flow_identifier=None, version=None, timestamp=None, author=None, comments=None):
        """
        VersionedFlowSnapshotMetadata - a model defined in Swagger
        """

        self._link = None
        self._bucket_identifier = None
        self._flow_identifier = None
        self._version = None
        self._timestamp = None
        self._author = None
        self._comments = None

        if link is not None:
          self.link = link
        self.bucket_identifier = bucket_identifier
        self.flow_identifier = flow_identifier
        self.version = version
        if timestamp is not None:
          self.timestamp = timestamp
        if author is not None:
          self.author = author
        if comments is not None:
          self.comments = comments

    @property
    def link(self):
        """
        Gets the link of this VersionedFlowSnapshotMetadata.
        An WebLink to this entity.

        :return: The link of this VersionedFlowSnapshotMetadata.
        :rtype: JaxbLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """
        Sets the link of this VersionedFlowSnapshotMetadata.
        An WebLink to this entity.

        :param link: The link of this VersionedFlowSnapshotMetadata.
        :type: JaxbLink
        """

        self._link = link

    @property
    def bucket_identifier(self):
        """
        Gets the bucket_identifier of this VersionedFlowSnapshotMetadata.
        The identifier of the bucket this snapshot belongs to.

        :return: The bucket_identifier of this VersionedFlowSnapshotMetadata.
        :rtype: str
        """
        return self._bucket_identifier

    @bucket_identifier.setter
    def bucket_identifier(self, bucket_identifier):
        """
        Sets the bucket_identifier of this VersionedFlowSnapshotMetadata.
        The identifier of the bucket this snapshot belongs to.

        :param bucket_identifier: The bucket_identifier of this VersionedFlowSnapshotMetadata.
        :type: str
        """
        if bucket_identifier is None:
            raise ValueError("Invalid value for `bucket_identifier`, must not be `None`")

        self._bucket_identifier = bucket_identifier

    @property
    def flow_identifier(self):
        """
        Gets the flow_identifier of this VersionedFlowSnapshotMetadata.
        The identifier of the flow this snapshot belongs to.

        :return: The flow_identifier of this VersionedFlowSnapshotMetadata.
        :rtype: str
        """
        return self._flow_identifier

    @flow_identifier.setter
    def flow_identifier(self, flow_identifier):
        """
        Sets the flow_identifier of this VersionedFlowSnapshotMetadata.
        The identifier of the flow this snapshot belongs to.

        :param flow_identifier: The flow_identifier of this VersionedFlowSnapshotMetadata.
        :type: str
        """
        if flow_identifier is None:
            raise ValueError("Invalid value for `flow_identifier`, must not be `None`")

        self._flow_identifier = flow_identifier

    @property
    def version(self):
        """
        Gets the version of this VersionedFlowSnapshotMetadata.
        The version of this snapshot of the flow.

        :return: The version of this VersionedFlowSnapshotMetadata.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this VersionedFlowSnapshotMetadata.
        The version of this snapshot of the flow.

        :param version: The version of this VersionedFlowSnapshotMetadata.
        :type: int
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")
        if version is not None and version < -1:
            raise ValueError("Invalid value for `version`, must be a value greater than or equal to `-1`")

        self._version = version

    @property
    def timestamp(self):
        """
        Gets the timestamp of this VersionedFlowSnapshotMetadata.
        The timestamp when the flow was saved, as milliseconds since epoch.

        :return: The timestamp of this VersionedFlowSnapshotMetadata.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this VersionedFlowSnapshotMetadata.
        The timestamp when the flow was saved, as milliseconds since epoch.

        :param timestamp: The timestamp of this VersionedFlowSnapshotMetadata.
        :type: int
        """
        if timestamp is not None and timestamp < 1:
            raise ValueError("Invalid value for `timestamp`, must be a value greater than or equal to `1`")

        self._timestamp = timestamp

    @property
    def author(self):
        """
        Gets the author of this VersionedFlowSnapshotMetadata.
        The user that created this snapshot of the flow.

        :return: The author of this VersionedFlowSnapshotMetadata.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """
        Sets the author of this VersionedFlowSnapshotMetadata.
        The user that created this snapshot of the flow.

        :param author: The author of this VersionedFlowSnapshotMetadata.
        :type: str
        """

        self._author = author

    @property
    def comments(self):
        """
        Gets the comments of this VersionedFlowSnapshotMetadata.
        The comments provided by the user when creating the snapshot.

        :return: The comments of this VersionedFlowSnapshotMetadata.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """
        Sets the comments of this VersionedFlowSnapshotMetadata.
        The comments provided by the user when creating the snapshot.

        :param comments: The comments of this VersionedFlowSnapshotMetadata.
        :type: str
        """

        self._comments = comments

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
        if not isinstance(other, VersionedFlowSnapshotMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
