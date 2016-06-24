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


class UserVariable(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, parent_id=None, user_id=None, client_id=None, variable_id=None, default_unit_id=None, minimum_allowed_value=None, maximum_allowed_value=None, filling_value=None, join_with=None, onset_delay=None, duration_of_action=None, variable_category_id=None, updated=None, public=None, cause_only=None, filling_type=None, number_of_measurements=None, number_of_processed_measurements=None, measurements_at_last_analysis=None, last_unit_id=None, last_original_unit_id=None, last_value=None, last_original_value=None, last_source_id=None, number_of_correlations=None, status=None, error_message=None, last_successful_update_time=None, standard_deviation=None, variance=None, minimum_recorded_value=None, maximum_recorded_daily_value=None, mean=None, median=None, most_common_unit_id=None, most_common_value=None, number_of_unique_daily_values=None, number_of_changes=None, skewness=None, kurtosis=None, latitude=None, longitude=None, location=None, experiment_start_time=None, experiment_end_time=None, created_at=None, updated_at=None, outcome=None, sources=None, earliest_source_time=None, latest_source_time=None, earliest_measurement_time=None, latest_measurement_time=None, earliest_filling_time=None, latest_filling_time=None):
        """
        UserVariable - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'parent_id': 'int',
            'user_id': 'int',
            'client_id': 'str',
            'variable_id': 'int',
            'default_unit_id': 'int',
            'minimum_allowed_value': 'float',
            'maximum_allowed_value': 'float',
            'filling_value': 'float',
            'join_with': 'int',
            'onset_delay': 'int',
            'duration_of_action': 'int',
            'variable_category_id': 'int',
            'updated': 'int',
            'public': 'int',
            'cause_only': 'bool',
            'filling_type': 'str',
            'number_of_measurements': 'int',
            'number_of_processed_measurements': 'int',
            'measurements_at_last_analysis': 'int',
            'last_unit_id': 'int',
            'last_original_unit_id': 'int',
            'last_value': 'float',
            'last_original_value': 'int',
            'last_source_id': 'int',
            'number_of_correlations': 'int',
            'status': 'str',
            'error_message': 'str',
            'last_successful_update_time': 'datetime',
            'standard_deviation': 'float',
            'variance': 'float',
            'minimum_recorded_value': 'float',
            'maximum_recorded_daily_value': 'float',
            'mean': 'float',
            'median': 'float',
            'most_common_unit_id': 'int',
            'most_common_value': 'float',
            'number_of_unique_daily_values': 'float',
            'number_of_changes': 'int',
            'skewness': 'float',
            'kurtosis': 'float',
            'latitude': 'float',
            'longitude': 'float',
            'location': 'str',
            'experiment_start_time': 'datetime',
            'experiment_end_time': 'datetime',
            'created_at': 'datetime',
            'updated_at': 'datetime',
            'outcome': 'bool',
            'sources': 'str',
            'earliest_source_time': 'int',
            'latest_source_time': 'int',
            'earliest_measurement_time': 'int',
            'latest_measurement_time': 'int',
            'earliest_filling_time': 'int',
            'latest_filling_time': 'int'
        }

        self.attribute_map = {
            'parent_id': 'parent_id',
            'user_id': 'user_id',
            'client_id': 'client_id',
            'variable_id': 'variable_id',
            'default_unit_id': 'default_unit_id',
            'minimum_allowed_value': 'minimum_allowed_value',
            'maximum_allowed_value': 'maximum_allowed_value',
            'filling_value': 'filling_value',
            'join_with': 'join_with',
            'onset_delay': 'onset_delay',
            'duration_of_action': 'duration_of_action',
            'variable_category_id': 'variable_category_id',
            'updated': 'updated',
            'public': 'public',
            'cause_only': 'cause_only',
            'filling_type': 'filling_type',
            'number_of_measurements': 'number_of_measurements',
            'number_of_processed_measurements': 'number_of_processed_measurements',
            'measurements_at_last_analysis': 'measurements_at_last_analysis',
            'last_unit_id': 'last_unit_id',
            'last_original_unit_id': 'last_original_unit_id',
            'last_value': 'last_value',
            'last_original_value': 'last_original_value',
            'last_source_id': 'last_source_id',
            'number_of_correlations': 'number_of_correlations',
            'status': 'status',
            'error_message': 'error_message',
            'last_successful_update_time': 'last_successful_update_time',
            'standard_deviation': 'standard_deviation',
            'variance': 'variance',
            'minimum_recorded_value': 'minimum_recorded_value',
            'maximum_recorded_daily_value': 'maximum_recorded_daily_value',
            'mean': 'mean',
            'median': 'median',
            'most_common_unit_id': 'most_common_unit_id',
            'most_common_value': 'most_common_value',
            'number_of_unique_daily_values': 'number_of_unique_daily_values',
            'number_of_changes': 'number_of_changes',
            'skewness': 'skewness',
            'kurtosis': 'kurtosis',
            'latitude': 'latitude',
            'longitude': 'longitude',
            'location': 'location',
            'experiment_start_time': 'experiment_start_time',
            'experiment_end_time': 'experiment_end_time',
            'created_at': 'created_at',
            'updated_at': 'updated_at',
            'outcome': 'outcome',
            'sources': 'sources',
            'earliest_source_time': 'earliest_source_time',
            'latest_source_time': 'latest_source_time',
            'earliest_measurement_time': 'earliest_measurement_time',
            'latest_measurement_time': 'latest_measurement_time',
            'earliest_filling_time': 'earliest_filling_time',
            'latest_filling_time': 'latest_filling_time'
        }

        self._parent_id = parent_id
        self._user_id = user_id
        self._client_id = client_id
        self._variable_id = variable_id
        self._default_unit_id = default_unit_id
        self._minimum_allowed_value = minimum_allowed_value
        self._maximum_allowed_value = maximum_allowed_value
        self._filling_value = filling_value
        self._join_with = join_with
        self._onset_delay = onset_delay
        self._duration_of_action = duration_of_action
        self._variable_category_id = variable_category_id
        self._updated = updated
        self._public = public
        self._cause_only = cause_only
        self._filling_type = filling_type
        self._number_of_measurements = number_of_measurements
        self._number_of_processed_measurements = number_of_processed_measurements
        self._measurements_at_last_analysis = measurements_at_last_analysis
        self._last_unit_id = last_unit_id
        self._last_original_unit_id = last_original_unit_id
        self._last_value = last_value
        self._last_original_value = last_original_value
        self._last_source_id = last_source_id
        self._number_of_correlations = number_of_correlations
        self._status = status
        self._error_message = error_message
        self._last_successful_update_time = last_successful_update_time
        self._standard_deviation = standard_deviation
        self._variance = variance
        self._minimum_recorded_value = minimum_recorded_value
        self._maximum_recorded_daily_value = maximum_recorded_daily_value
        self._mean = mean
        self._median = median
        self._most_common_unit_id = most_common_unit_id
        self._most_common_value = most_common_value
        self._number_of_unique_daily_values = number_of_unique_daily_values
        self._number_of_changes = number_of_changes
        self._skewness = skewness
        self._kurtosis = kurtosis
        self._latitude = latitude
        self._longitude = longitude
        self._location = location
        self._experiment_start_time = experiment_start_time
        self._experiment_end_time = experiment_end_time
        self._created_at = created_at
        self._updated_at = updated_at
        self._outcome = outcome
        self._sources = sources
        self._earliest_source_time = earliest_source_time
        self._latest_source_time = latest_source_time
        self._earliest_measurement_time = earliest_measurement_time
        self._latest_measurement_time = latest_measurement_time
        self._earliest_filling_time = earliest_filling_time
        self._latest_filling_time = latest_filling_time

    @property
    def parent_id(self):
        """
        Gets the parent_id of this UserVariable.
        ID of the parent variable if this variable has any parent

        :return: The parent_id of this UserVariable.
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """
        Sets the parent_id of this UserVariable.
        ID of the parent variable if this variable has any parent

        :param parent_id: The parent_id of this UserVariable.
        :type: int
        """

        self._parent_id = parent_id

    @property
    def user_id(self):
        """
        Gets the user_id of this UserVariable.
        User ID

        :return: The user_id of this UserVariable.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this UserVariable.
        User ID

        :param user_id: The user_id of this UserVariable.
        :type: int
        """

        self._user_id = user_id

    @property
    def client_id(self):
        """
        Gets the client_id of this UserVariable.
        client_id

        :return: The client_id of this UserVariable.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this UserVariable.
        client_id

        :param client_id: The client_id of this UserVariable.
        :type: str
        """

        self._client_id = client_id

    @property
    def variable_id(self):
        """
        Gets the variable_id of this UserVariable.
        ID of variable

        :return: The variable_id of this UserVariable.
        :rtype: int
        """
        return self._variable_id

    @variable_id.setter
    def variable_id(self, variable_id):
        """
        Sets the variable_id of this UserVariable.
        ID of variable

        :param variable_id: The variable_id of this UserVariable.
        :type: int
        """

        self._variable_id = variable_id

    @property
    def default_unit_id(self):
        """
        Gets the default_unit_id of this UserVariable.
        ID of unit to use for this variable

        :return: The default_unit_id of this UserVariable.
        :rtype: int
        """
        return self._default_unit_id

    @default_unit_id.setter
    def default_unit_id(self, default_unit_id):
        """
        Sets the default_unit_id of this UserVariable.
        ID of unit to use for this variable

        :param default_unit_id: The default_unit_id of this UserVariable.
        :type: int
        """

        self._default_unit_id = default_unit_id

    @property
    def minimum_allowed_value(self):
        """
        Gets the minimum_allowed_value of this UserVariable.
        Minimum reasonable value for this variable (uses default unit)

        :return: The minimum_allowed_value of this UserVariable.
        :rtype: float
        """
        return self._minimum_allowed_value

    @minimum_allowed_value.setter
    def minimum_allowed_value(self, minimum_allowed_value):
        """
        Sets the minimum_allowed_value of this UserVariable.
        Minimum reasonable value for this variable (uses default unit)

        :param minimum_allowed_value: The minimum_allowed_value of this UserVariable.
        :type: float
        """

        self._minimum_allowed_value = minimum_allowed_value

    @property
    def maximum_allowed_value(self):
        """
        Gets the maximum_allowed_value of this UserVariable.
        Maximum reasonable value for this variable (uses default unit)

        :return: The maximum_allowed_value of this UserVariable.
        :rtype: float
        """
        return self._maximum_allowed_value

    @maximum_allowed_value.setter
    def maximum_allowed_value(self, maximum_allowed_value):
        """
        Sets the maximum_allowed_value of this UserVariable.
        Maximum reasonable value for this variable (uses default unit)

        :param maximum_allowed_value: The maximum_allowed_value of this UserVariable.
        :type: float
        """

        self._maximum_allowed_value = maximum_allowed_value

    @property
    def filling_value(self):
        """
        Gets the filling_value of this UserVariable.
        Value for replacing null measurements

        :return: The filling_value of this UserVariable.
        :rtype: float
        """
        return self._filling_value

    @filling_value.setter
    def filling_value(self, filling_value):
        """
        Sets the filling_value of this UserVariable.
        Value for replacing null measurements

        :param filling_value: The filling_value of this UserVariable.
        :type: float
        """

        self._filling_value = filling_value

    @property
    def join_with(self):
        """
        Gets the join_with of this UserVariable.
        The Variable this Variable should be joined with. If the variable is joined with some other variable then it is not shown to user in the list of variables

        :return: The join_with of this UserVariable.
        :rtype: int
        """
        return self._join_with

    @join_with.setter
    def join_with(self, join_with):
        """
        Sets the join_with of this UserVariable.
        The Variable this Variable should be joined with. If the variable is joined with some other variable then it is not shown to user in the list of variables

        :param join_with: The join_with of this UserVariable.
        :type: int
        """

        self._join_with = join_with

    @property
    def onset_delay(self):
        """
        Gets the onset_delay of this UserVariable.
        How long it takes for a measurement in this variable to take effect

        :return: The onset_delay of this UserVariable.
        :rtype: int
        """
        return self._onset_delay

    @onset_delay.setter
    def onset_delay(self, onset_delay):
        """
        Sets the onset_delay of this UserVariable.
        How long it takes for a measurement in this variable to take effect

        :param onset_delay: The onset_delay of this UserVariable.
        :type: int
        """

        self._onset_delay = onset_delay

    @property
    def duration_of_action(self):
        """
        Gets the duration_of_action of this UserVariable.
        Estimated duration of time following the onset delay in which a stimulus produces a perceivable effect

        :return: The duration_of_action of this UserVariable.
        :rtype: int
        """
        return self._duration_of_action

    @duration_of_action.setter
    def duration_of_action(self, duration_of_action):
        """
        Sets the duration_of_action of this UserVariable.
        Estimated duration of time following the onset delay in which a stimulus produces a perceivable effect

        :param duration_of_action: The duration_of_action of this UserVariable.
        :type: int
        """

        self._duration_of_action = duration_of_action

    @property
    def variable_category_id(self):
        """
        Gets the variable_category_id of this UserVariable.
        ID of variable category

        :return: The variable_category_id of this UserVariable.
        :rtype: int
        """
        return self._variable_category_id

    @variable_category_id.setter
    def variable_category_id(self, variable_category_id):
        """
        Sets the variable_category_id of this UserVariable.
        ID of variable category

        :param variable_category_id: The variable_category_id of this UserVariable.
        :type: int
        """

        self._variable_category_id = variable_category_id

    @property
    def updated(self):
        """
        Gets the updated of this UserVariable.
        updated

        :return: The updated of this UserVariable.
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this UserVariable.
        updated

        :param updated: The updated of this UserVariable.
        :type: int
        """

        self._updated = updated

    @property
    def public(self):
        """
        Gets the public of this UserVariable.
        Is variable public

        :return: The public of this UserVariable.
        :rtype: int
        """
        return self._public

    @public.setter
    def public(self, public):
        """
        Sets the public of this UserVariable.
        Is variable public

        :param public: The public of this UserVariable.
        :type: int
        """

        self._public = public

    @property
    def cause_only(self):
        """
        Gets the cause_only of this UserVariable.
        A value of 1 indicates that this variable is generally a cause in a causal relationship.  An example of a causeOnly variable would be a variable such as Cloud Cover which would generally not be influenced by the behaviour of the user

        :return: The cause_only of this UserVariable.
        :rtype: bool
        """
        return self._cause_only

    @cause_only.setter
    def cause_only(self, cause_only):
        """
        Sets the cause_only of this UserVariable.
        A value of 1 indicates that this variable is generally a cause in a causal relationship.  An example of a causeOnly variable would be a variable such as Cloud Cover which would generally not be influenced by the behaviour of the user

        :param cause_only: The cause_only of this UserVariable.
        :type: bool
        """

        self._cause_only = cause_only

    @property
    def filling_type(self):
        """
        Gets the filling_type of this UserVariable.
        0 -> No filling, 1 -> Use filling-value

        :return: The filling_type of this UserVariable.
        :rtype: str
        """
        return self._filling_type

    @filling_type.setter
    def filling_type(self, filling_type):
        """
        Sets the filling_type of this UserVariable.
        0 -> No filling, 1 -> Use filling-value

        :param filling_type: The filling_type of this UserVariable.
        :type: str
        """

        self._filling_type = filling_type

    @property
    def number_of_measurements(self):
        """
        Gets the number_of_measurements of this UserVariable.
        Number of measurements

        :return: The number_of_measurements of this UserVariable.
        :rtype: int
        """
        return self._number_of_measurements

    @number_of_measurements.setter
    def number_of_measurements(self, number_of_measurements):
        """
        Sets the number_of_measurements of this UserVariable.
        Number of measurements

        :param number_of_measurements: The number_of_measurements of this UserVariable.
        :type: int
        """

        self._number_of_measurements = number_of_measurements

    @property
    def number_of_processed_measurements(self):
        """
        Gets the number_of_processed_measurements of this UserVariable.
        Number of processed measurements

        :return: The number_of_processed_measurements of this UserVariable.
        :rtype: int
        """
        return self._number_of_processed_measurements

    @number_of_processed_measurements.setter
    def number_of_processed_measurements(self, number_of_processed_measurements):
        """
        Sets the number_of_processed_measurements of this UserVariable.
        Number of processed measurements

        :param number_of_processed_measurements: The number_of_processed_measurements of this UserVariable.
        :type: int
        """

        self._number_of_processed_measurements = number_of_processed_measurements

    @property
    def measurements_at_last_analysis(self):
        """
        Gets the measurements_at_last_analysis of this UserVariable.
        Number of measurements at last analysis

        :return: The measurements_at_last_analysis of this UserVariable.
        :rtype: int
        """
        return self._measurements_at_last_analysis

    @measurements_at_last_analysis.setter
    def measurements_at_last_analysis(self, measurements_at_last_analysis):
        """
        Sets the measurements_at_last_analysis of this UserVariable.
        Number of measurements at last analysis

        :param measurements_at_last_analysis: The measurements_at_last_analysis of this UserVariable.
        :type: int
        """

        self._measurements_at_last_analysis = measurements_at_last_analysis

    @property
    def last_unit_id(self):
        """
        Gets the last_unit_id of this UserVariable.
        ID of last Unit

        :return: The last_unit_id of this UserVariable.
        :rtype: int
        """
        return self._last_unit_id

    @last_unit_id.setter
    def last_unit_id(self, last_unit_id):
        """
        Sets the last_unit_id of this UserVariable.
        ID of last Unit

        :param last_unit_id: The last_unit_id of this UserVariable.
        :type: int
        """

        self._last_unit_id = last_unit_id

    @property
    def last_original_unit_id(self):
        """
        Gets the last_original_unit_id of this UserVariable.
        ID of last original Unit

        :return: The last_original_unit_id of this UserVariable.
        :rtype: int
        """
        return self._last_original_unit_id

    @last_original_unit_id.setter
    def last_original_unit_id(self, last_original_unit_id):
        """
        Sets the last_original_unit_id of this UserVariable.
        ID of last original Unit

        :param last_original_unit_id: The last_original_unit_id of this UserVariable.
        :type: int
        """

        self._last_original_unit_id = last_original_unit_id

    @property
    def last_value(self):
        """
        Gets the last_value of this UserVariable.
        Last Value

        :return: The last_value of this UserVariable.
        :rtype: float
        """
        return self._last_value

    @last_value.setter
    def last_value(self, last_value):
        """
        Sets the last_value of this UserVariable.
        Last Value

        :param last_value: The last_value of this UserVariable.
        :type: float
        """

        self._last_value = last_value

    @property
    def last_original_value(self):
        """
        Gets the last_original_value of this UserVariable.
        Last original value which is stored

        :return: The last_original_value of this UserVariable.
        :rtype: int
        """
        return self._last_original_value

    @last_original_value.setter
    def last_original_value(self, last_original_value):
        """
        Sets the last_original_value of this UserVariable.
        Last original value which is stored

        :param last_original_value: The last_original_value of this UserVariable.
        :type: int
        """

        self._last_original_value = last_original_value

    @property
    def last_source_id(self):
        """
        Gets the last_source_id of this UserVariable.
        ID of last source

        :return: The last_source_id of this UserVariable.
        :rtype: int
        """
        return self._last_source_id

    @last_source_id.setter
    def last_source_id(self, last_source_id):
        """
        Sets the last_source_id of this UserVariable.
        ID of last source

        :param last_source_id: The last_source_id of this UserVariable.
        :type: int
        """

        self._last_source_id = last_source_id

    @property
    def number_of_correlations(self):
        """
        Gets the number_of_correlations of this UserVariable.
        Number of correlations for this variable

        :return: The number_of_correlations of this UserVariable.
        :rtype: int
        """
        return self._number_of_correlations

    @number_of_correlations.setter
    def number_of_correlations(self, number_of_correlations):
        """
        Sets the number_of_correlations of this UserVariable.
        Number of correlations for this variable

        :param number_of_correlations: The number_of_correlations of this UserVariable.
        :type: int
        """

        self._number_of_correlations = number_of_correlations

    @property
    def status(self):
        """
        Gets the status of this UserVariable.
        status

        :return: The status of this UserVariable.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UserVariable.
        status

        :param status: The status of this UserVariable.
        :type: str
        """

        self._status = status

    @property
    def error_message(self):
        """
        Gets the error_message of this UserVariable.
        error_message

        :return: The error_message of this UserVariable.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this UserVariable.
        error_message

        :param error_message: The error_message of this UserVariable.
        :type: str
        """

        self._error_message = error_message

    @property
    def last_successful_update_time(self):
        """
        Gets the last_successful_update_time of this UserVariable.
        When this variable or its settings were last updated

        :return: The last_successful_update_time of this UserVariable.
        :rtype: datetime
        """
        return self._last_successful_update_time

    @last_successful_update_time.setter
    def last_successful_update_time(self, last_successful_update_time):
        """
        Sets the last_successful_update_time of this UserVariable.
        When this variable or its settings were last updated

        :param last_successful_update_time: The last_successful_update_time of this UserVariable.
        :type: datetime
        """

        self._last_successful_update_time = last_successful_update_time

    @property
    def standard_deviation(self):
        """
        Gets the standard_deviation of this UserVariable.
        Standard deviation

        :return: The standard_deviation of this UserVariable.
        :rtype: float
        """
        return self._standard_deviation

    @standard_deviation.setter
    def standard_deviation(self, standard_deviation):
        """
        Sets the standard_deviation of this UserVariable.
        Standard deviation

        :param standard_deviation: The standard_deviation of this UserVariable.
        :type: float
        """

        self._standard_deviation = standard_deviation

    @property
    def variance(self):
        """
        Gets the variance of this UserVariable.
        Variance

        :return: The variance of this UserVariable.
        :rtype: float
        """
        return self._variance

    @variance.setter
    def variance(self, variance):
        """
        Sets the variance of this UserVariable.
        Variance

        :param variance: The variance of this UserVariable.
        :type: float
        """

        self._variance = variance

    @property
    def minimum_recorded_value(self):
        """
        Gets the minimum_recorded_value of this UserVariable.
        Minimum recorded value of this variable

        :return: The minimum_recorded_value of this UserVariable.
        :rtype: float
        """
        return self._minimum_recorded_value

    @minimum_recorded_value.setter
    def minimum_recorded_value(self, minimum_recorded_value):
        """
        Sets the minimum_recorded_value of this UserVariable.
        Minimum recorded value of this variable

        :param minimum_recorded_value: The minimum_recorded_value of this UserVariable.
        :type: float
        """

        self._minimum_recorded_value = minimum_recorded_value

    @property
    def maximum_recorded_daily_value(self):
        """
        Gets the maximum_recorded_daily_value of this UserVariable.
        Maximum recorded daily value of this variable

        :return: The maximum_recorded_daily_value of this UserVariable.
        :rtype: float
        """
        return self._maximum_recorded_daily_value

    @maximum_recorded_daily_value.setter
    def maximum_recorded_daily_value(self, maximum_recorded_daily_value):
        """
        Sets the maximum_recorded_daily_value of this UserVariable.
        Maximum recorded daily value of this variable

        :param maximum_recorded_daily_value: The maximum_recorded_daily_value of this UserVariable.
        :type: float
        """

        self._maximum_recorded_daily_value = maximum_recorded_daily_value

    @property
    def mean(self):
        """
        Gets the mean of this UserVariable.
        Mean

        :return: The mean of this UserVariable.
        :rtype: float
        """
        return self._mean

    @mean.setter
    def mean(self, mean):
        """
        Sets the mean of this UserVariable.
        Mean

        :param mean: The mean of this UserVariable.
        :type: float
        """

        self._mean = mean

    @property
    def median(self):
        """
        Gets the median of this UserVariable.
        Median

        :return: The median of this UserVariable.
        :rtype: float
        """
        return self._median

    @median.setter
    def median(self, median):
        """
        Sets the median of this UserVariable.
        Median

        :param median: The median of this UserVariable.
        :type: float
        """

        self._median = median

    @property
    def most_common_unit_id(self):
        """
        Gets the most_common_unit_id of this UserVariable.
        Most common Unit ID

        :return: The most_common_unit_id of this UserVariable.
        :rtype: int
        """
        return self._most_common_unit_id

    @most_common_unit_id.setter
    def most_common_unit_id(self, most_common_unit_id):
        """
        Sets the most_common_unit_id of this UserVariable.
        Most common Unit ID

        :param most_common_unit_id: The most_common_unit_id of this UserVariable.
        :type: int
        """

        self._most_common_unit_id = most_common_unit_id

    @property
    def most_common_value(self):
        """
        Gets the most_common_value of this UserVariable.
        Most common value

        :return: The most_common_value of this UserVariable.
        :rtype: float
        """
        return self._most_common_value

    @most_common_value.setter
    def most_common_value(self, most_common_value):
        """
        Sets the most_common_value of this UserVariable.
        Most common value

        :param most_common_value: The most_common_value of this UserVariable.
        :type: float
        """

        self._most_common_value = most_common_value

    @property
    def number_of_unique_daily_values(self):
        """
        Gets the number_of_unique_daily_values of this UserVariable.
        Number of unique daily values

        :return: The number_of_unique_daily_values of this UserVariable.
        :rtype: float
        """
        return self._number_of_unique_daily_values

    @number_of_unique_daily_values.setter
    def number_of_unique_daily_values(self, number_of_unique_daily_values):
        """
        Sets the number_of_unique_daily_values of this UserVariable.
        Number of unique daily values

        :param number_of_unique_daily_values: The number_of_unique_daily_values of this UserVariable.
        :type: float
        """

        self._number_of_unique_daily_values = number_of_unique_daily_values

    @property
    def number_of_changes(self):
        """
        Gets the number_of_changes of this UserVariable.
        Number of changes

        :return: The number_of_changes of this UserVariable.
        :rtype: int
        """
        return self._number_of_changes

    @number_of_changes.setter
    def number_of_changes(self, number_of_changes):
        """
        Sets the number_of_changes of this UserVariable.
        Number of changes

        :param number_of_changes: The number_of_changes of this UserVariable.
        :type: int
        """

        self._number_of_changes = number_of_changes

    @property
    def skewness(self):
        """
        Gets the skewness of this UserVariable.
        Skewness

        :return: The skewness of this UserVariable.
        :rtype: float
        """
        return self._skewness

    @skewness.setter
    def skewness(self, skewness):
        """
        Sets the skewness of this UserVariable.
        Skewness

        :param skewness: The skewness of this UserVariable.
        :type: float
        """

        self._skewness = skewness

    @property
    def kurtosis(self):
        """
        Gets the kurtosis of this UserVariable.
        Kurtosis

        :return: The kurtosis of this UserVariable.
        :rtype: float
        """
        return self._kurtosis

    @kurtosis.setter
    def kurtosis(self, kurtosis):
        """
        Sets the kurtosis of this UserVariable.
        Kurtosis

        :param kurtosis: The kurtosis of this UserVariable.
        :type: float
        """

        self._kurtosis = kurtosis

    @property
    def latitude(self):
        """
        Gets the latitude of this UserVariable.
        Latitude

        :return: The latitude of this UserVariable.
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """
        Sets the latitude of this UserVariable.
        Latitude

        :param latitude: The latitude of this UserVariable.
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """
        Gets the longitude of this UserVariable.
        Longitude

        :return: The longitude of this UserVariable.
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """
        Sets the longitude of this UserVariable.
        Longitude

        :param longitude: The longitude of this UserVariable.
        :type: float
        """

        self._longitude = longitude

    @property
    def location(self):
        """
        Gets the location of this UserVariable.
        Location

        :return: The location of this UserVariable.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this UserVariable.
        Location

        :param location: The location of this UserVariable.
        :type: str
        """

        self._location = location

    @property
    def experiment_start_time(self):
        """
        Gets the experiment_start_time of this UserVariable.
        Earliest measurement start_time to be used in analysis. Use ISO 8601 datetime format

        :return: The experiment_start_time of this UserVariable.
        :rtype: datetime
        """
        return self._experiment_start_time

    @experiment_start_time.setter
    def experiment_start_time(self, experiment_start_time):
        """
        Sets the experiment_start_time of this UserVariable.
        Earliest measurement start_time to be used in analysis. Use ISO 8601 datetime format

        :param experiment_start_time: The experiment_start_time of this UserVariable.
        :type: datetime
        """

        self._experiment_start_time = experiment_start_time

    @property
    def experiment_end_time(self):
        """
        Gets the experiment_end_time of this UserVariable.
        Latest measurement start_time to be used in analysis. Use ISO 8601 datetime format

        :return: The experiment_end_time of this UserVariable.
        :rtype: datetime
        """
        return self._experiment_end_time

    @experiment_end_time.setter
    def experiment_end_time(self, experiment_end_time):
        """
        Sets the experiment_end_time of this UserVariable.
        Latest measurement start_time to be used in analysis. Use ISO 8601 datetime format

        :param experiment_end_time: The experiment_end_time of this UserVariable.
        :type: datetime
        """

        self._experiment_end_time = experiment_end_time

    @property
    def created_at(self):
        """
        Gets the created_at of this UserVariable.
        When the record was first created. Use ISO 8601 datetime format

        :return: The created_at of this UserVariable.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this UserVariable.
        When the record was first created. Use ISO 8601 datetime format

        :param created_at: The created_at of this UserVariable.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this UserVariable.
        When the record in the database was last updated. Use ISO 8601 datetime format

        :return: The updated_at of this UserVariable.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this UserVariable.
        When the record in the database was last updated. Use ISO 8601 datetime format

        :param updated_at: The updated_at of this UserVariable.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def outcome(self):
        """
        Gets the outcome of this UserVariable.
        Outcome variables (those with `outcome` == 1) are variables for which a human would generally want to identify the influencing factors.  These include symptoms of illness, physique, mood, cognitive performance, etc.  Generally correlation calculations are only performed on outcome variables

        :return: The outcome of this UserVariable.
        :rtype: bool
        """
        return self._outcome

    @outcome.setter
    def outcome(self, outcome):
        """
        Sets the outcome of this UserVariable.
        Outcome variables (those with `outcome` == 1) are variables for which a human would generally want to identify the influencing factors.  These include symptoms of illness, physique, mood, cognitive performance, etc.  Generally correlation calculations are only performed on outcome variables

        :param outcome: The outcome of this UserVariable.
        :type: bool
        """

        self._outcome = outcome

    @property
    def sources(self):
        """
        Gets the sources of this UserVariable.
        Comma-separated list of source names to limit variables to those sources

        :return: The sources of this UserVariable.
        :rtype: str
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """
        Sets the sources of this UserVariable.
        Comma-separated list of source names to limit variables to those sources

        :param sources: The sources of this UserVariable.
        :type: str
        """

        self._sources = sources

    @property
    def earliest_source_time(self):
        """
        Gets the earliest_source_time of this UserVariable.
        Earliest source time

        :return: The earliest_source_time of this UserVariable.
        :rtype: int
        """
        return self._earliest_source_time

    @earliest_source_time.setter
    def earliest_source_time(self, earliest_source_time):
        """
        Sets the earliest_source_time of this UserVariable.
        Earliest source time

        :param earliest_source_time: The earliest_source_time of this UserVariable.
        :type: int
        """

        self._earliest_source_time = earliest_source_time

    @property
    def latest_source_time(self):
        """
        Gets the latest_source_time of this UserVariable.
        Latest source time

        :return: The latest_source_time of this UserVariable.
        :rtype: int
        """
        return self._latest_source_time

    @latest_source_time.setter
    def latest_source_time(self, latest_source_time):
        """
        Sets the latest_source_time of this UserVariable.
        Latest source time

        :param latest_source_time: The latest_source_time of this UserVariable.
        :type: int
        """

        self._latest_source_time = latest_source_time

    @property
    def earliest_measurement_time(self):
        """
        Gets the earliest_measurement_time of this UserVariable.
        Earliest measurement time

        :return: The earliest_measurement_time of this UserVariable.
        :rtype: int
        """
        return self._earliest_measurement_time

    @earliest_measurement_time.setter
    def earliest_measurement_time(self, earliest_measurement_time):
        """
        Sets the earliest_measurement_time of this UserVariable.
        Earliest measurement time

        :param earliest_measurement_time: The earliest_measurement_time of this UserVariable.
        :type: int
        """

        self._earliest_measurement_time = earliest_measurement_time

    @property
    def latest_measurement_time(self):
        """
        Gets the latest_measurement_time of this UserVariable.
        Latest measurement time

        :return: The latest_measurement_time of this UserVariable.
        :rtype: int
        """
        return self._latest_measurement_time

    @latest_measurement_time.setter
    def latest_measurement_time(self, latest_measurement_time):
        """
        Sets the latest_measurement_time of this UserVariable.
        Latest measurement time

        :param latest_measurement_time: The latest_measurement_time of this UserVariable.
        :type: int
        """

        self._latest_measurement_time = latest_measurement_time

    @property
    def earliest_filling_time(self):
        """
        Gets the earliest_filling_time of this UserVariable.
        Earliest filling time

        :return: The earliest_filling_time of this UserVariable.
        :rtype: int
        """
        return self._earliest_filling_time

    @earliest_filling_time.setter
    def earliest_filling_time(self, earliest_filling_time):
        """
        Sets the earliest_filling_time of this UserVariable.
        Earliest filling time

        :param earliest_filling_time: The earliest_filling_time of this UserVariable.
        :type: int
        """

        self._earliest_filling_time = earliest_filling_time

    @property
    def latest_filling_time(self):
        """
        Gets the latest_filling_time of this UserVariable.
        Latest filling time

        :return: The latest_filling_time of this UserVariable.
        :rtype: int
        """
        return self._latest_filling_time

    @latest_filling_time.setter
    def latest_filling_time(self, latest_filling_time):
        """
        Sets the latest_filling_time of this UserVariable.
        Latest filling time

        :param latest_filling_time: The latest_filling_time of this UserVariable.
        :type: int
        """

        self._latest_filling_time = latest_filling_time

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
