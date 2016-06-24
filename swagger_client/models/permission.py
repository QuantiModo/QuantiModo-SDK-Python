# coding: utf-8

"""
    QuantiModo

    Welcome to QuantiModo API! QuantiModo makes it easy to retrieve normalized user data from a wide array of devices and applications. [Learn about QuantiModo](https://quantimo.do) or contact us at <api@quantimo.do>.         Before you get started, you will need to: * Sign in/Sign up, and add some data at [https://app.quantimo.do/api/v2/account/connectors](https://app.quantimo.do/api/v2/account/connectors) to try out the API for yourself * Create an app to get your client id and secret at [https://app.quantimo.do/api/v2/apps](https://app.quantimo.do/api/v2/apps) * As long as you're signed in, it will use your browser's cookie for authentication.  However, client applications must use OAuth2 tokens to access the API.     ## Application Endpoints These endpoints give you access to all authorized users' data for that application. ### Getting Application Token Make a `POST` request to `/api/v2/oauth/access_token`         * `grant_type` Must be `client_credentials`.         * `clientId` Your application's clientId.         * `client_secret` Your application's client_secret.         * `redirect_uri` Your application's redirect url.                ## Example Queries ### Query Options The standard query options for QuantiModo API are as described in the table below. These are the available query options in QuantiModo API: <table>            <thead>                <tr>                    <th>Parameter</th>                    <th>Description</th>                </tr>            </thead>            <tbody>                <tr>                    <td>limit</td>                    <td>The LIMIT is used to limit the number of results returned.  So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records.</td>                </tr>                <tr>                    <td>offset</td>                    <td>Suppose you wanted to show results 11-20. You'd set the    offset to 10 and the limit to 10.</td>                </tr>                <tr>                    <td>sort</td>                    <td>Sort by given field. If the field is prefixed with '-', it    will sort in descending order.</td>                </tr>            </tbody>        </table>         ### Pagination Conventions Since the maximum limit is 200 records, to get more than that you'll have to make multiple API calls and page through the results. To retrieve all the data, you can iterate through data by using the `limit` and `offset` query parameters.For example, if you want to retrieve data from 61-80 then you can use a query with the following parameters,         `/v2/variables?limit=20&offset=60`         Generally, you'll be retrieving new or updated user data. To avoid unnecessary API calls, you'll want to store your last refresh time locally.  Initially, it should be set to 0. Then whenever you make a request to get new data, you should limit the returned results to those updated since your last refresh by appending append         `?lastUpdated=(ge)&quot2013-01-D01T01:01:01&quot`         to your request.         Also for better pagination, you can get link to the records of first, last, next and previous page from response headers: * `Total-Count` - Total number of results for given query * `Link-First` - Link to get first page records * `Link-Last` - Link to get last page records * `Link-Prev` - Link to get previous records set * `Link-Next` - Link to get next records set         Remember, response header will be only sent when the record set is available. e.g. You will not get a ```Link-Last``` & ```Link-Next``` when you query for the last page.         ### Filter operators support API supports the following operators with filter parameters: <br> **Comparison operators**         Comparison operators allow you to limit results to those greater than, less than, or equal to a specified value for a specified attribute. These operators can be used with strings, numbers, and dates. The following comparison operators are available: * `gt` for `greater than` comparison * `ge` for `greater than or equal` comparison * `lt` for `less than` comparison * `le` for `less than or equal` comparison         They are included in queries using the following format:         `(<operator>)<value>`         For example, in order to filter value which is greater than 21, the following query parameter should be used:         `?value=(gt)21` <br><br> **Equals/In Operators**         It also allows filtering by the exact value of an attribute or by a set of values, depending on the type of value passed as a query parameter. If the value contains commas, the parameter is split on commas and used as array input for `IN` filtering, otherwise the exact match is applied. In order to only show records which have the value 42, the following query should be used:         `?value=42`         In order to filter records which have value 42 or 43, the following query should be used:         `?value=42,43` <br><br> **Like operators**         Like operators allow filtering using `LIKE` query. This operator is triggered if exact match operator is used, but value contains `%` sign as the first or last character. In order to filter records which category that start with `Food`, the following query should be used:         `?category=Food%` <br><br> **Negation operator**         It is possible to get negated results of a query by prefixed the operator with `!`. Some examples:         `//filter records except those with value are not 42 or 43`<br> `?value=!42,43`         `//filter records with value not greater than 21`<br> `?value=!(ge)21` <br><br> **Multiple constraints for single attribute**         It is possible to apply multiple constraints by providing an array of query filters:         Filter all records which value is greater than 20.2 and less than 20.3<br> `?value[]=(gt)20.2&value[]=(lt)20.3`         Filter all records which value is greater than 20.2 and less than 20.3 but not 20.2778<br> `?value[]=(gt)20.2&value[]=(lt)20.3&value[]=!20.2778`<br><br> 

    OpenAPI spec version: 2.0.6
    
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


class Permission(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, target=None, variable_name=None, min_timestamp=None, max_timestamp=None, min_time_of_day=None, max_time_of_day=None, week=None):
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
            'min_timestamp': 'minTimestamp',
            'max_timestamp': 'maxTimestamp',
            'min_time_of_day': 'minTimeOfDay',
            'max_time_of_day': 'maxTimeOfDay',
            'week': 'week'
        }

        self._target = target
        self._variable_name = variable_name
        self._min_timestamp = min_timestamp
        self._max_timestamp = max_timestamp
        self._min_time_of_day = min_time_of_day
        self._max_time_of_day = max_time_of_day
        self._week = week

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
