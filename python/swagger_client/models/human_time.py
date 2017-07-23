# coding: utf-8

"""
    QuantiModo

    QuantiModo makes it easy to retrieve normalized user data from a wide array of devices and applications. [Learn about QuantiModo](https://quantimo.do), check out our [docs](https://github.com/QuantiModo/docs) or contact us at [help.quantimo.do](https://help.quantimo.do). 

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class HumanTime(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, date=None, timezone_type=None, timezone=None):
        """
        HumanTime - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'date': 'str',
            'timezone_type': 'int',
            'timezone': 'str'
        }

        self.attribute_map = {
            'date': 'date',
            'timezone_type': 'timezone_type',
            'timezone': 'timezone'
        }

        self._date = date
        self._timezone_type = timezone_type
        self._timezone = timezone


    @property
    def date(self):
        """
        Gets the date of this HumanTime.
        date time

        :return: The date of this HumanTime.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """
        Sets the date of this HumanTime.
        date time

        :param date: The date of this HumanTime.
        :type: str
        """

        self._date = date

    @property
    def timezone_type(self):
        """
        Gets the timezone_type of this HumanTime.


        :return: The timezone_type of this HumanTime.
        :rtype: int
        """
        return self._timezone_type

    @timezone_type.setter
    def timezone_type(self, timezone_type):
        """
        Sets the timezone_type of this HumanTime.


        :param timezone_type: The timezone_type of this HumanTime.
        :type: int
        """

        self._timezone_type = timezone_type

    @property
    def timezone(self):
        """
        Gets the timezone of this HumanTime.
        timezone of date time

        :return: The timezone of this HumanTime.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this HumanTime.
        timezone of date time

        :param timezone: The timezone of this HumanTime.
        :type: str
        """

        self._timezone = timezone

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other