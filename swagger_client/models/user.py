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


class User(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        User - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'wp_id': 'int',
            'display_name': 'str',
            'login_name': 'str',
            'email': 'str',
            'token': 'str',
            'administrator': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'wp_id': 'wpId',
            'display_name': 'displayName',
            'login_name': 'loginName',
            'email': 'email',
            'token': 'token',
            'administrator': 'administrator'
        }

        self._id = None
        self._wp_id = None
        self._display_name = None
        self._login_name = None
        self._email = None
        self._token = None
        self._administrator = None

    @property
    def id(self):
        """
        Gets the id of this User.
        User id

        :return: The id of this User.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this User.
        User id

        :param id: The id of this User.
        :type: int
        """
        self._id = id

    @property
    def wp_id(self):
        """
        Gets the wp_id of this User.
        Wordpress user id

        :return: The wp_id of this User.
        :rtype: int
        """
        return self._wp_id

    @wp_id.setter
    def wp_id(self, wp_id):
        """
        Sets the wp_id of this User.
        Wordpress user id

        :param wp_id: The wp_id of this User.
        :type: int
        """
        self._wp_id = wp_id

    @property
    def display_name(self):
        """
        Gets the display_name of this User.
        User display name

        :return: The display_name of this User.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this User.
        User display name

        :param display_name: The display_name of this User.
        :type: str
        """
        self._display_name = display_name

    @property
    def login_name(self):
        """
        Gets the login_name of this User.
        User login name

        :return: The login_name of this User.
        :rtype: str
        """
        return self._login_name

    @login_name.setter
    def login_name(self, login_name):
        """
        Sets the login_name of this User.
        User login name

        :param login_name: The login_name of this User.
        :type: str
        """
        self._login_name = login_name

    @property
    def email(self):
        """
        Gets the email of this User.
        User email

        :return: The email of this User.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this User.
        User email

        :param email: The email of this User.
        :type: str
        """
        self._email = email

    @property
    def token(self):
        """
        Gets the token of this User.
        User token

        :return: The token of this User.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """
        Sets the token of this User.
        User token

        :param token: The token of this User.
        :type: str
        """
        self._token = token

    @property
    def administrator(self):
        """
        Gets the administrator of this User.
        Is user administrator

        :return: The administrator of this User.
        :rtype: bool
        """
        return self._administrator

    @administrator.setter
    def administrator(self, administrator):
        """
        Sets the administrator of this User.
        Is user administrator

        :param administrator: The administrator of this User.
        :type: bool
        """
        self._administrator = administrator

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