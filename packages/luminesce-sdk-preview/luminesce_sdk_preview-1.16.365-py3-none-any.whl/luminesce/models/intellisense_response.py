# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.16.365
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from luminesce.configuration import Configuration


class IntellisenseResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'auto_complete_list': 'list[IntellisenseItem]',
        'try_again_soon_for_more': 'bool',
        'sql_with_marker': 'str',
        'start_replacement_position': 'CursorPosition',
        'end_replacement_position': 'CursorPosition'
    }

    attribute_map = {
        'auto_complete_list': 'autoCompleteList',
        'try_again_soon_for_more': 'tryAgainSoonForMore',
        'sql_with_marker': 'sqlWithMarker',
        'start_replacement_position': 'startReplacementPosition',
        'end_replacement_position': 'endReplacementPosition'
    }

    required_map = {
        'auto_complete_list': 'required',
        'try_again_soon_for_more': 'required',
        'sql_with_marker': 'required',
        'start_replacement_position': 'required',
        'end_replacement_position': 'required'
    }

    def __init__(self, auto_complete_list=None, try_again_soon_for_more=None, sql_with_marker=None, start_replacement_position=None, end_replacement_position=None, local_vars_configuration=None):  # noqa: E501
        """IntellisenseResponse - a model defined in OpenAPI"
        
        :param auto_complete_list:  The available items at this point (required)
        :type auto_complete_list: list[luminesce.IntellisenseItem]
        :param try_again_soon_for_more:  Should the caller try again soon? (true means a cache is being built and this is a preliminary response!) (required)
        :type try_again_soon_for_more: bool
        :param sql_with_marker:  The SQL this is for with characters indicating the location the pop-up is for (required)
        :type sql_with_marker: str
        :param start_replacement_position:  (required)
        :type start_replacement_position: luminesce.CursorPosition
        :param end_replacement_position:  (required)
        :type end_replacement_position: luminesce.CursorPosition

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._auto_complete_list = None
        self._try_again_soon_for_more = None
        self._sql_with_marker = None
        self._start_replacement_position = None
        self._end_replacement_position = None
        self.discriminator = None

        self.auto_complete_list = auto_complete_list
        self.try_again_soon_for_more = try_again_soon_for_more
        self.sql_with_marker = sql_with_marker
        self.start_replacement_position = start_replacement_position
        self.end_replacement_position = end_replacement_position

    @property
    def auto_complete_list(self):
        """Gets the auto_complete_list of this IntellisenseResponse.  # noqa: E501

        The available items at this point  # noqa: E501

        :return: The auto_complete_list of this IntellisenseResponse.  # noqa: E501
        :rtype: list[luminesce.IntellisenseItem]
        """
        return self._auto_complete_list

    @auto_complete_list.setter
    def auto_complete_list(self, auto_complete_list):
        """Sets the auto_complete_list of this IntellisenseResponse.

        The available items at this point  # noqa: E501

        :param auto_complete_list: The auto_complete_list of this IntellisenseResponse.  # noqa: E501
        :type auto_complete_list: list[luminesce.IntellisenseItem]
        """
        if self.local_vars_configuration.client_side_validation and auto_complete_list is None:  # noqa: E501
            raise ValueError("Invalid value for `auto_complete_list`, must not be `None`")  # noqa: E501

        self._auto_complete_list = auto_complete_list

    @property
    def try_again_soon_for_more(self):
        """Gets the try_again_soon_for_more of this IntellisenseResponse.  # noqa: E501

        Should the caller try again soon? (true means a cache is being built and this is a preliminary response!)  # noqa: E501

        :return: The try_again_soon_for_more of this IntellisenseResponse.  # noqa: E501
        :rtype: bool
        """
        return self._try_again_soon_for_more

    @try_again_soon_for_more.setter
    def try_again_soon_for_more(self, try_again_soon_for_more):
        """Sets the try_again_soon_for_more of this IntellisenseResponse.

        Should the caller try again soon? (true means a cache is being built and this is a preliminary response!)  # noqa: E501

        :param try_again_soon_for_more: The try_again_soon_for_more of this IntellisenseResponse.  # noqa: E501
        :type try_again_soon_for_more: bool
        """
        if self.local_vars_configuration.client_side_validation and try_again_soon_for_more is None:  # noqa: E501
            raise ValueError("Invalid value for `try_again_soon_for_more`, must not be `None`")  # noqa: E501

        self._try_again_soon_for_more = try_again_soon_for_more

    @property
    def sql_with_marker(self):
        """Gets the sql_with_marker of this IntellisenseResponse.  # noqa: E501

        The SQL this is for with characters indicating the location the pop-up is for  # noqa: E501

        :return: The sql_with_marker of this IntellisenseResponse.  # noqa: E501
        :rtype: str
        """
        return self._sql_with_marker

    @sql_with_marker.setter
    def sql_with_marker(self, sql_with_marker):
        """Sets the sql_with_marker of this IntellisenseResponse.

        The SQL this is for with characters indicating the location the pop-up is for  # noqa: E501

        :param sql_with_marker: The sql_with_marker of this IntellisenseResponse.  # noqa: E501
        :type sql_with_marker: str
        """
        if self.local_vars_configuration.client_side_validation and sql_with_marker is None:  # noqa: E501
            raise ValueError("Invalid value for `sql_with_marker`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                sql_with_marker is not None and len(sql_with_marker) < 1):
            raise ValueError("Invalid value for `sql_with_marker`, length must be greater than or equal to `1`")  # noqa: E501

        self._sql_with_marker = sql_with_marker

    @property
    def start_replacement_position(self):
        """Gets the start_replacement_position of this IntellisenseResponse.  # noqa: E501


        :return: The start_replacement_position of this IntellisenseResponse.  # noqa: E501
        :rtype: luminesce.CursorPosition
        """
        return self._start_replacement_position

    @start_replacement_position.setter
    def start_replacement_position(self, start_replacement_position):
        """Sets the start_replacement_position of this IntellisenseResponse.


        :param start_replacement_position: The start_replacement_position of this IntellisenseResponse.  # noqa: E501
        :type start_replacement_position: luminesce.CursorPosition
        """
        if self.local_vars_configuration.client_side_validation and start_replacement_position is None:  # noqa: E501
            raise ValueError("Invalid value for `start_replacement_position`, must not be `None`")  # noqa: E501

        self._start_replacement_position = start_replacement_position

    @property
    def end_replacement_position(self):
        """Gets the end_replacement_position of this IntellisenseResponse.  # noqa: E501


        :return: The end_replacement_position of this IntellisenseResponse.  # noqa: E501
        :rtype: luminesce.CursorPosition
        """
        return self._end_replacement_position

    @end_replacement_position.setter
    def end_replacement_position(self, end_replacement_position):
        """Sets the end_replacement_position of this IntellisenseResponse.


        :param end_replacement_position: The end_replacement_position of this IntellisenseResponse.  # noqa: E501
        :type end_replacement_position: luminesce.CursorPosition
        """
        if self.local_vars_configuration.client_side_validation and end_replacement_position is None:  # noqa: E501
            raise ValueError("Invalid value for `end_replacement_position`, must not be `None`")  # noqa: E501

        self._end_replacement_position = end_replacement_position

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IntellisenseResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IntellisenseResponse):
            return True

        return self.to_dict() != other.to_dict()
