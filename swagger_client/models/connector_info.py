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


class ConnectorInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ConnectorInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'connected': 'bool',
            'error': 'str',
            'history': 'list[ConnectorInfoHistoryItem]'
        }

        self.attribute_map = {
            'id': 'id',
            'connected': 'connected',
            'error': 'error',
            'history': 'history'
        }

        self._id = None
        self._connected = None
        self._error = None
        self._history = None

    @property
    def id(self):
        """
        Gets the id of this ConnectorInfo.
        Connector ID number

        :return: The id of this ConnectorInfo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ConnectorInfo.
        Connector ID number

        :param id: The id of this ConnectorInfo.
        :type: int
        """
        self._id = id

    @property
    def connected(self):
        """
        Gets the connected of this ConnectorInfo.
        True if the authenticated user has this connector enabled

        :return: The connected of this ConnectorInfo.
        :rtype: bool
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        """
        Sets the connected of this ConnectorInfo.
        True if the authenticated user has this connector enabled

        :param connected: The connected of this ConnectorInfo.
        :type: bool
        """
        self._connected = connected

    @property
    def error(self):
        """
        Gets the error of this ConnectorInfo.
        Error message. Empty if connected.

        :return: The error of this ConnectorInfo.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this ConnectorInfo.
        Error message. Empty if connected.

        :param error: The error of this ConnectorInfo.
        :type: str
        """
        self._error = error

    @property
    def history(self):
        """
        Gets the history of this ConnectorInfo.


        :return: The history of this ConnectorInfo.
        :rtype: list[ConnectorInfoHistoryItem]
        """
        return self._history

    @history.setter
    def history(self, history):
        """
        Sets the history of this ConnectorInfo.


        :param history: The history of this ConnectorInfo.
        :type: list[ConnectorInfoHistoryItem]
        """
        self._history = history

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