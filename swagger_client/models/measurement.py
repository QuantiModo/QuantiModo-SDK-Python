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


class Measurement(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, variable=None, source=None, start_time=None, human_time=None, value=None, unit=None, original_value=None, stored_value=None, stored_abbreviated_unit_name=None, original_abbreviated_unit_name=None, abbreviated_unit_name=None, note=None):
        """
        Measurement - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'variable': 'str',
            'source': 'str',
            'start_time': 'str',
            'human_time': 'HumanTime',
            'value': 'float',
            'unit': 'str',
            'original_value': 'int',
            'stored_value': 'float',
            'stored_abbreviated_unit_name': 'str',
            'original_abbreviated_unit_name': 'str',
            'abbreviated_unit_name': 'str',
            'note': 'str'
        }

        self.attribute_map = {
            'variable': 'variable',
            'source': 'source',
            'start_time': 'startTime',
            'human_time': 'humanTime',
            'value': 'value',
            'unit': 'unit',
            'original_value': 'originalValue',
            'stored_value': 'storedValue',
            'stored_abbreviated_unit_name': 'storedAbbreviatedUnitName',
            'original_abbreviated_unit_name': 'originalAbbreviatedUnitName',
            'abbreviated_unit_name': 'abbreviatedUnitName',
            'note': 'note'
        }

        self._variable = variable
        self._source = source
        self._start_time = start_time
        self._human_time = human_time
        self._value = value
        self._unit = unit
        self._original_value = original_value
        self._stored_value = stored_value
        self._stored_abbreviated_unit_name = stored_abbreviated_unit_name
        self._original_abbreviated_unit_name = original_abbreviated_unit_name
        self._abbreviated_unit_name = abbreviated_unit_name
        self._note = note

    @property
    def variable(self):
        """
        Gets the variable of this Measurement.
        ORIGINAL Name of the variable for which we are creating the measurement records

        :return: The variable of this Measurement.
        :rtype: str
        """
        return self._variable

    @variable.setter
    def variable(self, variable):
        """
        Sets the variable of this Measurement.
        ORIGINAL Name of the variable for which we are creating the measurement records

        :param variable: The variable of this Measurement.
        :type: str
        """

        self._variable = variable

    @property
    def source(self):
        """
        Gets the source of this Measurement.
        Application or device used to record the measurement values

        :return: The source of this Measurement.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this Measurement.
        Application or device used to record the measurement values

        :param source: The source of this Measurement.
        :type: str
        """

        self._source = source

    @property
    def start_time(self):
        """
        Gets the start_time of this Measurement.
        Start Time for the measurement event in ISO 8601

        :return: The start_time of this Measurement.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this Measurement.
        Start Time for the measurement event in ISO 8601

        :param start_time: The start_time of this Measurement.
        :type: str
        """

        self._start_time = start_time

    @property
    def human_time(self):
        """
        Gets the human_time of this Measurement.
        Start Time for the measurement event in ISO 8601

        :return: The human_time of this Measurement.
        :rtype: HumanTime
        """
        return self._human_time

    @human_time.setter
    def human_time(self, human_time):
        """
        Sets the human_time of this Measurement.
        Start Time for the measurement event in ISO 8601

        :param human_time: The human_time of this Measurement.
        :type: HumanTime
        """

        self._human_time = human_time

    @property
    def value(self):
        """
        Gets the value of this Measurement.
        Converted measurement value in requested unit

        :return: The value of this Measurement.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Measurement.
        Converted measurement value in requested unit

        :param value: The value of this Measurement.
        :type: float
        """

        self._value = value

    @property
    def unit(self):
        """
        Gets the unit of this Measurement.
        Unit of measurement as requested in GET request

        :return: The unit of this Measurement.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this Measurement.
        Unit of measurement as requested in GET request

        :param unit: The unit of this Measurement.
        :type: str
        """

        self._unit = unit

    @property
    def original_value(self):
        """
        Gets the original_value of this Measurement.
        Original value

        :return: The original_value of this Measurement.
        :rtype: int
        """
        return self._original_value

    @original_value.setter
    def original_value(self, original_value):
        """
        Sets the original_value of this Measurement.
        Original value

        :param original_value: The original_value of this Measurement.
        :type: int
        """

        self._original_value = original_value

    @property
    def stored_value(self):
        """
        Gets the stored_value of this Measurement.
        Measurement value in the unit as orignally submitted

        :return: The stored_value of this Measurement.
        :rtype: float
        """
        return self._stored_value

    @stored_value.setter
    def stored_value(self, stored_value):
        """
        Sets the stored_value of this Measurement.
        Measurement value in the unit as orignally submitted

        :param stored_value: The stored_value of this Measurement.
        :type: float
        """

        self._stored_value = stored_value

    @property
    def stored_abbreviated_unit_name(self):
        """
        Gets the stored_abbreviated_unit_name of this Measurement.
        Unit of measurement as originally submitted

        :return: The stored_abbreviated_unit_name of this Measurement.
        :rtype: str
        """
        return self._stored_abbreviated_unit_name

    @stored_abbreviated_unit_name.setter
    def stored_abbreviated_unit_name(self, stored_abbreviated_unit_name):
        """
        Sets the stored_abbreviated_unit_name of this Measurement.
        Unit of measurement as originally submitted

        :param stored_abbreviated_unit_name: The stored_abbreviated_unit_name of this Measurement.
        :type: str
        """

        self._stored_abbreviated_unit_name = stored_abbreviated_unit_name

    @property
    def original_abbreviated_unit_name(self):
        """
        Gets the original_abbreviated_unit_name of this Measurement.
        Original Unit of measurement as originally submitted

        :return: The original_abbreviated_unit_name of this Measurement.
        :rtype: str
        """
        return self._original_abbreviated_unit_name

    @original_abbreviated_unit_name.setter
    def original_abbreviated_unit_name(self, original_abbreviated_unit_name):
        """
        Sets the original_abbreviated_unit_name of this Measurement.
        Original Unit of measurement as originally submitted

        :param original_abbreviated_unit_name: The original_abbreviated_unit_name of this Measurement.
        :type: str
        """

        self._original_abbreviated_unit_name = original_abbreviated_unit_name

    @property
    def abbreviated_unit_name(self):
        """
        Gets the abbreviated_unit_name of this Measurement.
        Unit of measurement as originally submitted

        :return: The abbreviated_unit_name of this Measurement.
        :rtype: str
        """
        return self._abbreviated_unit_name

    @abbreviated_unit_name.setter
    def abbreviated_unit_name(self, abbreviated_unit_name):
        """
        Sets the abbreviated_unit_name of this Measurement.
        Unit of measurement as originally submitted

        :param abbreviated_unit_name: The abbreviated_unit_name of this Measurement.
        :type: str
        """

        self._abbreviated_unit_name = abbreviated_unit_name

    @property
    def note(self):
        """
        Gets the note of this Measurement.
        Note of measurement

        :return: The note of this Measurement.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """
        Sets the note of this Measurement.
        Note of measurement

        :param note: The note of this Measurement.
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
