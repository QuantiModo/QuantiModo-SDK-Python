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


class ValueObject(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ValueObject - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'timestamp': 'int',
            'value': 'float',
            'note': 'str'
        }

        self.attribute_map = {
            'timestamp': 'timestamp',
            'value': 'value',
            'note': 'note'
        }

        self._timestamp = None
        self._value = None
        self._note = None

    @property
    def timestamp(self):
        """
        Gets the timestamp of this ValueObject.
        Timestamp for the measurement event in epoch time (unixtime)

        :return: The timestamp of this ValueObject.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this ValueObject.
        Timestamp for the measurement event in epoch time (unixtime)

        :param timestamp: The timestamp of this ValueObject.
        :type: int
        """
        self._timestamp = timestamp

    @property
    def value(self):
        """
        Gets the value of this ValueObject.
        Measurement value

        :return: The value of this ValueObject.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this ValueObject.
        Measurement value

        :param value: The value of this ValueObject.
        :type: float
        """
        self._value = value

    @property
    def note(self):
        """
        Gets the note of this ValueObject.
        Optional note to include with the measurement

        :return: The note of this ValueObject.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """
        Sets the note of this ValueObject.
        Optional note to include with the measurement

        :param note: The note of this ValueObject.
        :type: str
        """
        self._note = note

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