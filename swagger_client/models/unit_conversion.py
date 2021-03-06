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


class UnitConversion(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        UnitConversion - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'unit_id': 'int',
            'step_number': 'bool',
            'operation': 'bool',
            'value': 'float',
            'created_at': 'datetime',
            'updated_at': 'datetime'
        }

        self.attribute_map = {
            'unit_id': 'unit_id',
            'step_number': 'step_number',
            'operation': 'operation',
            'value': 'value',
            'created_at': 'created_at',
            'updated_at': 'updated_at'
        }

        self._unit_id = None
        self._step_number = None
        self._operation = None
        self._value = None
        self._created_at = None
        self._updated_at = None

    @property
    def unit_id(self):
        """
        Gets the unit_id of this UnitConversion.
        unit_id

        :return: The unit_id of this UnitConversion.
        :rtype: int
        """
        return self._unit_id

    @unit_id.setter
    def unit_id(self, unit_id):
        """
        Sets the unit_id of this UnitConversion.
        unit_id

        :param unit_id: The unit_id of this UnitConversion.
        :type: int
        """
        self._unit_id = unit_id

    @property
    def step_number(self):
        """
        Gets the step_number of this UnitConversion.
        step in the conversion process

        :return: The step_number of this UnitConversion.
        :rtype: bool
        """
        return self._step_number

    @step_number.setter
    def step_number(self, step_number):
        """
        Sets the step_number of this UnitConversion.
        step in the conversion process

        :param step_number: The step_number of this UnitConversion.
        :type: bool
        """
        self._step_number = step_number

    @property
    def operation(self):
        """
        Gets the operation of this UnitConversion.
        0 is add and 1 is multiply

        :return: The operation of this UnitConversion.
        :rtype: bool
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        Sets the operation of this UnitConversion.
        0 is add and 1 is multiply

        :param operation: The operation of this UnitConversion.
        :type: bool
        """
        self._operation = operation

    @property
    def value(self):
        """
        Gets the value of this UnitConversion.
        number used in the operation

        :return: The value of this UnitConversion.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this UnitConversion.
        number used in the operation

        :param value: The value of this UnitConversion.
        :type: float
        """
        self._value = value

    @property
    def created_at(self):
        """
        Gets the created_at of this UnitConversion.
        created_at

        :return: The created_at of this UnitConversion.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this UnitConversion.
        created_at

        :param created_at: The created_at of this UnitConversion.
        :type: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this UnitConversion.
        updated_at

        :return: The updated_at of this UnitConversion.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this UnitConversion.
        updated_at

        :param updated_at: The updated_at of this UnitConversion.
        :type: datetime
        """
        self._updated_at = updated_at

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
