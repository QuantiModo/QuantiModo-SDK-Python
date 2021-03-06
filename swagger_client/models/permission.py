# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class Permission(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Permission - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'target': 'int',
            'variable_name': 'str',
            'min_timestamp': 'int',
            'max_timestamp': 'int',
            'min_time_of_day': 'int',
            'max_time_of_day': 'int',
            'week': 'str'
        }

        self.attribute_map = {
            'target': 'target',
            'variable_name': 'variableName',
            'min_timestamp': 'min_timestamp',
            'max_timestamp': 'max_timestamp',
            'min_time_of_day': 'min_time_of_day',
            'max_time_of_day': 'max_time_of_day',
            'week': 'week'
        }

        self._target = None
        self._variable_name = None
        self._min_timestamp = None
        self._max_timestamp = None
        self._min_time_of_day = None
        self._max_time_of_day = None
        self._week = None

    @property
    def target(self):
        """
        Gets the target of this Permission.
        Grant permission to target user or public so they may access measurements within the given parameters. TODO: Rename target to something more intuitive.

        :return: The target of this Permission.
        :rtype: int
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this Permission.
        Grant permission to target user or public so they may access measurements within the given parameters. TODO: Rename target to something more intuitive.

        :param target: The target of this Permission.
        :type: int
        """
        self._target = target

    @property
    def variable_name(self):
        """
        Gets the variable_name of this Permission.
        ORIGINAL Variable name

        :return: The variable_name of this Permission.
        :rtype: str
        """
        return self._variable_name

    @variable_name.setter
    def variable_name(self, variable_name):
        """
        Sets the variable_name of this Permission.
        ORIGINAL Variable name

        :param variable_name: The variable_name of this Permission.
        :type: str
        """
        self._variable_name = variable_name

    @property
    def min_timestamp(self):
        """
        Gets the min_timestamp of this Permission.
        Earliest time when measurements will be accessible in epoch seconds

        :return: The min_timestamp of this Permission.
        :rtype: int
        """
        return self._min_timestamp

    @min_timestamp.setter
    def min_timestamp(self, min_timestamp):
        """
        Sets the min_timestamp of this Permission.
        Earliest time when measurements will be accessible in epoch seconds

        :param min_timestamp: The min_timestamp of this Permission.
        :type: int
        """
        self._min_timestamp = min_timestamp

    @property
    def max_timestamp(self):
        """
        Gets the max_timestamp of this Permission.
        Latest time when measurements will be accessible in epoch seconds

        :return: The max_timestamp of this Permission.
        :rtype: int
        """
        return self._max_timestamp

    @max_timestamp.setter
    def max_timestamp(self, max_timestamp):
        """
        Sets the max_timestamp of this Permission.
        Latest time when measurements will be accessible in epoch seconds

        :param max_timestamp: The max_timestamp of this Permission.
        :type: int
        """
        self._max_timestamp = max_timestamp

    @property
    def min_time_of_day(self):
        """
        Gets the min_time_of_day of this Permission.
        Earliest time of day when measurements will be accessible in epoch seconds

        :return: The min_time_of_day of this Permission.
        :rtype: int
        """
        return self._min_time_of_day

    @min_time_of_day.setter
    def min_time_of_day(self, min_time_of_day):
        """
        Sets the min_time_of_day of this Permission.
        Earliest time of day when measurements will be accessible in epoch seconds

        :param min_time_of_day: The min_time_of_day of this Permission.
        :type: int
        """
        self._min_time_of_day = min_time_of_day

    @property
    def max_time_of_day(self):
        """
        Gets the max_time_of_day of this Permission.
        Latest time of day when measurements will be accessible in epoch seconds

        :return: The max_time_of_day of this Permission.
        :rtype: int
        """
        return self._max_time_of_day

    @max_time_of_day.setter
    def max_time_of_day(self, max_time_of_day):
        """
        Sets the max_time_of_day of this Permission.
        Latest time of day when measurements will be accessible in epoch seconds

        :param max_time_of_day: The max_time_of_day of this Permission.
        :type: int
        """
        self._max_time_of_day = max_time_of_day

    @property
    def week(self):
        """
        Gets the week of this Permission.
        Maybe specifies if only weekday measurements should be accessible

        :return: The week of this Permission.
        :rtype: str
        """
        return self._week

    @week.setter
    def week(self, week):
        """
        Sets the week of this Permission.
        Maybe specifies if only weekday measurements should be accessible

        :param week: The week of this Permission.
        :type: str
        """
        self._week = week

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
