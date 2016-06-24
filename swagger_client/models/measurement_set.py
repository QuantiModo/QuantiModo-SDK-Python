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


class MeasurementSet(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, measurements=None, variable_name=None, source_name=None, variable_category_name=None, combination_operation=None, abbreviated_unit_name=None):
        """
        MeasurementSet - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'measurements': 'list[ValueObject]',
            'variable_name': 'str',
            'source_name': 'str',
            'variable_category_name': 'str',
            'combination_operation': 'str',
            'abbreviated_unit_name': 'str'
        }

        self.attribute_map = {
            'measurements': 'measurements',
            'variable_name': 'variableName',
            'source_name': 'sourceName',
            'variable_category_name': 'variableCategoryName',
            'combination_operation': 'combinationOperation',
            'abbreviated_unit_name': 'abbreviatedUnitName'
        }

        self._measurements = measurements
        self._variable_name = variable_name
        self._source_name = source_name
        self._variable_category_name = variable_category_name
        self._combination_operation = combination_operation
        self._abbreviated_unit_name = abbreviated_unit_name

    @property
    def measurements(self):
        """
        Gets the measurements of this MeasurementSet.
        Array of timestamps, values, and optional notes

        :return: The measurements of this MeasurementSet.
        :rtype: list[ValueObject]
        """
        return self._measurements

    @measurements.setter
    def measurements(self, measurements):
        """
        Sets the measurements of this MeasurementSet.
        Array of timestamps, values, and optional notes

        :param measurements: The measurements of this MeasurementSet.
        :type: list[ValueObject]
        """

        self._measurements = measurements

    @property
    def variable_name(self):
        """
        Gets the variable_name of this MeasurementSet.
        ORIGINAL name of the variable for which we are creating the measurement records

        :return: The variable_name of this MeasurementSet.
        :rtype: str
        """
        return self._variable_name

    @variable_name.setter
    def variable_name(self, variable_name):
        """
        Sets the variable_name of this MeasurementSet.
        ORIGINAL name of the variable for which we are creating the measurement records

        :param variable_name: The variable_name of this MeasurementSet.
        :type: str
        """

        self._variable_name = variable_name

    @property
    def source_name(self):
        """
        Gets the source_name of this MeasurementSet.
        Name of the application or device used to record the measurement values

        :return: The source_name of this MeasurementSet.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """
        Sets the source_name of this MeasurementSet.
        Name of the application or device used to record the measurement values

        :param source_name: The source_name of this MeasurementSet.
        :type: str
        """

        self._source_name = source_name

    @property
    def variable_category_name(self):
        """
        Gets the variable_category_name of this MeasurementSet.
        Variable category name

        :return: The variable_category_name of this MeasurementSet.
        :rtype: str
        """
        return self._variable_category_name

    @variable_category_name.setter
    def variable_category_name(self, variable_category_name):
        """
        Sets the variable_category_name of this MeasurementSet.
        Variable category name

        :param variable_category_name: The variable_category_name of this MeasurementSet.
        :type: str
        """

        self._variable_category_name = variable_category_name

    @property
    def combination_operation(self):
        """
        Gets the combination_operation of this MeasurementSet.
        Way to aggregate measurements over time. Options are \"MEAN\" or \"SUM\".  SUM should be used for things like minutes of exercise.  If you use MEAN for exercise, then a person might exercise more minutes in one day but add separate measurements that were smaller.  So when we are doing correlational analysis, we would think that the person exercised less that day even though they exercised more.  Conversely, we must use MEAN for things such as ratings which cannot be SUMMED.

        :return: The combination_operation of this MeasurementSet.
        :rtype: str
        """
        return self._combination_operation

    @combination_operation.setter
    def combination_operation(self, combination_operation):
        """
        Sets the combination_operation of this MeasurementSet.
        Way to aggregate measurements over time. Options are \"MEAN\" or \"SUM\".  SUM should be used for things like minutes of exercise.  If you use MEAN for exercise, then a person might exercise more minutes in one day but add separate measurements that were smaller.  So when we are doing correlational analysis, we would think that the person exercised less that day even though they exercised more.  Conversely, we must use MEAN for things such as ratings which cannot be SUMMED.

        :param combination_operation: The combination_operation of this MeasurementSet.
        :type: str
        """
        allowed_values = ["MEAN", "SUM"]
        if combination_operation not in allowed_values:
            raise ValueError(
                "Invalid value for `combination_operation`, must be one of {0}"
                .format(allowed_values)
            )

        self._combination_operation = combination_operation

    @property
    def abbreviated_unit_name(self):
        """
        Gets the abbreviated_unit_name of this MeasurementSet.
        Unit of measurement

        :return: The abbreviated_unit_name of this MeasurementSet.
        :rtype: str
        """
        return self._abbreviated_unit_name

    @abbreviated_unit_name.setter
    def abbreviated_unit_name(self, abbreviated_unit_name):
        """
        Sets the abbreviated_unit_name of this MeasurementSet.
        Unit of measurement

        :param abbreviated_unit_name: The abbreviated_unit_name of this MeasurementSet.
        :type: str
        """

        self._abbreviated_unit_name = abbreviated_unit_name

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
