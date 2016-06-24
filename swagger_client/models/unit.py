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


class Unit(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, abbreviated_name=None, category=None, minimum_value=None, maximum_value=None, conversion_steps=None):
        """
        Unit - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'abbreviated_name': 'str',
            'category': 'str',
            'minimum_value': 'float',
            'maximum_value': 'float',
            'conversion_steps': 'list[ConversionStep]'
        }

        self.attribute_map = {
            'name': 'name',
            'abbreviated_name': 'abbreviatedName',
            'category': 'category',
            'minimum_value': 'minimumValue',
            'maximum_value': 'maximumValue',
            'conversion_steps': 'conversionSteps'
        }

        self._name = name
        self._abbreviated_name = abbreviated_name
        self._category = category
        self._minimum_value = minimum_value
        self._maximum_value = maximum_value
        self._conversion_steps = conversion_steps

    @property
    def name(self):
        """
        Gets the name of this Unit.
        Unit name

        :return: The name of this Unit.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Unit.
        Unit name

        :param name: The name of this Unit.
        :type: str
        """

        self._name = name

    @property
    def abbreviated_name(self):
        """
        Gets the abbreviated_name of this Unit.
        Unit abbreviation

        :return: The abbreviated_name of this Unit.
        :rtype: str
        """
        return self._abbreviated_name

    @abbreviated_name.setter
    def abbreviated_name(self, abbreviated_name):
        """
        Sets the abbreviated_name of this Unit.
        Unit abbreviation

        :param abbreviated_name: The abbreviated_name of this Unit.
        :type: str
        """

        self._abbreviated_name = abbreviated_name

    @property
    def category(self):
        """
        Gets the category of this Unit.
        Unit category

        :return: The category of this Unit.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this Unit.
        Unit category

        :param category: The category of this Unit.
        :type: str
        """
        allowed_values = ["Distance", "Duration", "Energy", "Frequency", "Miscellany", "Pressure", "Proportion", "Rating", "Temperature", "Volume", "Weight"]
        if category not in allowed_values:
            raise ValueError(
                "Invalid value for `category`, must be one of {0}"
                .format(allowed_values)
            )

        self._category = category

    @property
    def minimum_value(self):
        """
        Gets the minimum_value of this Unit.
        The smallest acceptable value for measurements using this unit

        :return: The minimum_value of this Unit.
        :rtype: float
        """
        return self._minimum_value

    @minimum_value.setter
    def minimum_value(self, minimum_value):
        """
        Sets the minimum_value of this Unit.
        The smallest acceptable value for measurements using this unit

        :param minimum_value: The minimum_value of this Unit.
        :type: float
        """

        self._minimum_value = minimum_value

    @property
    def maximum_value(self):
        """
        Gets the maximum_value of this Unit.
        The largest acceptable value for measurements using this unit

        :return: The maximum_value of this Unit.
        :rtype: float
        """
        return self._maximum_value

    @maximum_value.setter
    def maximum_value(self, maximum_value):
        """
        Sets the maximum_value of this Unit.
        The largest acceptable value for measurements using this unit

        :param maximum_value: The maximum_value of this Unit.
        :type: float
        """

        self._maximum_value = maximum_value

    @property
    def conversion_steps(self):
        """
        Gets the conversion_steps of this Unit.
        Conversion steps list

        :return: The conversion_steps of this Unit.
        :rtype: list[ConversionStep]
        """
        return self._conversion_steps

    @conversion_steps.setter
    def conversion_steps(self, conversion_steps):
        """
        Sets the conversion_steps of this Unit.
        Conversion steps list

        :param conversion_steps: The conversion_steps of this Unit.
        :type: list[ConversionStep]
        """

        self._conversion_steps = conversion_steps

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
