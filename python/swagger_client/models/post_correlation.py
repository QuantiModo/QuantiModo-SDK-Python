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


class PostCorrelation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, cause_variable_name=None, effect_variable_name=None, correlation=None, vote=None):
        """
        PostCorrelation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cause_variable_name': 'str',
            'effect_variable_name': 'str',
            'correlation': 'float',
            'vote': 'int'
        }

        self.attribute_map = {
            'cause_variable_name': 'causeVariableName',
            'effect_variable_name': 'effectVariableName',
            'correlation': 'correlation',
            'vote': 'vote'
        }

        self._cause_variable_name = cause_variable_name
        self._effect_variable_name = effect_variable_name
        self._correlation = correlation
        self._vote = vote


    @property
    def cause_variable_name(self):
        """
        Gets the cause_variable_name of this PostCorrelation.
        Cause variable name

        :return: The cause_variable_name of this PostCorrelation.
        :rtype: str
        """
        return self._cause_variable_name

    @cause_variable_name.setter
    def cause_variable_name(self, cause_variable_name):
        """
        Sets the cause_variable_name of this PostCorrelation.
        Cause variable name

        :param cause_variable_name: The cause_variable_name of this PostCorrelation.
        :type: str
        """
        if cause_variable_name is None:
            raise ValueError("Invalid value for `cause_variable_name`, must not be `None`")

        self._cause_variable_name = cause_variable_name

    @property
    def effect_variable_name(self):
        """
        Gets the effect_variable_name of this PostCorrelation.
        Effect variable name

        :return: The effect_variable_name of this PostCorrelation.
        :rtype: str
        """
        return self._effect_variable_name

    @effect_variable_name.setter
    def effect_variable_name(self, effect_variable_name):
        """
        Sets the effect_variable_name of this PostCorrelation.
        Effect variable name

        :param effect_variable_name: The effect_variable_name of this PostCorrelation.
        :type: str
        """
        if effect_variable_name is None:
            raise ValueError("Invalid value for `effect_variable_name`, must not be `None`")

        self._effect_variable_name = effect_variable_name

    @property
    def correlation(self):
        """
        Gets the correlation of this PostCorrelation.
        Correlation value

        :return: The correlation of this PostCorrelation.
        :rtype: float
        """
        return self._correlation

    @correlation.setter
    def correlation(self, correlation):
        """
        Sets the correlation of this PostCorrelation.
        Correlation value

        :param correlation: The correlation of this PostCorrelation.
        :type: float
        """
        if correlation is None:
            raise ValueError("Invalid value for `correlation`, must not be `None`")

        self._correlation = correlation

    @property
    def vote(self):
        """
        Gets the vote of this PostCorrelation.
        Vote: 0 or 1

        :return: The vote of this PostCorrelation.
        :rtype: int
        """
        return self._vote

    @vote.setter
    def vote(self, vote):
        """
        Sets the vote of this PostCorrelation.
        Vote: 0 or 1

        :param vote: The vote of this PostCorrelation.
        :type: int
        """

        self._vote = vote

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