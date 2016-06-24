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


class Variable(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, original_name=None, category=None, abbreviated_unit_name=None, abbreviated_unit_id=None, sources=None, minimum_value=None, maximum_value=None, combination_operation=None, filling_value=None, join_with=None, joined_variables=None, parent=None, sub_variables=None, onset_delay=None, duration_of_action=None, earliest_measurement_time=None, latest_measurement_time=None, updated=None, cause_only=None, number_of_correlations=None, outcome=None, measurements_at_last_analysis=None, number_of_measurements=None, last_unit=None, last_value=None, most_common_value=None, most_common_unit=None, last_source=None):
        """
        Variable - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'original_name': 'str',
            'category': 'str',
            'abbreviated_unit_name': 'str',
            'abbreviated_unit_id': 'int',
            'sources': 'str',
            'minimum_value': 'float',
            'maximum_value': 'float',
            'combination_operation': 'str',
            'filling_value': 'float',
            'join_with': 'str',
            'joined_variables': 'list[Variable]',
            'parent': 'int',
            'sub_variables': 'list[Variable]',
            'onset_delay': 'int',
            'duration_of_action': 'int',
            'earliest_measurement_time': 'int',
            'latest_measurement_time': 'int',
            'updated': 'int',
            'cause_only': 'int',
            'number_of_correlations': 'int',
            'outcome': 'int',
            'measurements_at_last_analysis': 'int',
            'number_of_measurements': 'int',
            'last_unit': 'str',
            'last_value': 'int',
            'most_common_value': 'int',
            'most_common_unit': 'str',
            'last_source': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'original_name': 'originalName',
            'category': 'category',
            'abbreviated_unit_name': 'abbreviatedUnitName',
            'abbreviated_unit_id': 'abbreviatedUnitId',
            'sources': 'sources',
            'minimum_value': 'minimumValue',
            'maximum_value': 'maximumValue',
            'combination_operation': 'combinationOperation',
            'filling_value': 'fillingValue',
            'join_with': 'joinWith',
            'joined_variables': 'joinedVariables',
            'parent': 'parent',
            'sub_variables': 'subVariables',
            'onset_delay': 'onsetDelay',
            'duration_of_action': 'durationOfAction',
            'earliest_measurement_time': 'earliestMeasurementTime',
            'latest_measurement_time': 'latestMeasurementTime',
            'updated': 'updated',
            'cause_only': 'causeOnly',
            'number_of_correlations': 'numberOfCorrelations',
            'outcome': 'outcome',
            'measurements_at_last_analysis': 'measurementsAtLastAnalysis',
            'number_of_measurements': 'numberOfMeasurements',
            'last_unit': 'lastUnit',
            'last_value': 'lastValue',
            'most_common_value': 'mostCommonValue',
            'most_common_unit': 'mostCommonUnit',
            'last_source': 'lastSource'
        }

        self._id = id
        self._name = name
        self._original_name = original_name
        self._category = category
        self._abbreviated_unit_name = abbreviated_unit_name
        self._abbreviated_unit_id = abbreviated_unit_id
        self._sources = sources
        self._minimum_value = minimum_value
        self._maximum_value = maximum_value
        self._combination_operation = combination_operation
        self._filling_value = filling_value
        self._join_with = join_with
        self._joined_variables = joined_variables
        self._parent = parent
        self._sub_variables = sub_variables
        self._onset_delay = onset_delay
        self._duration_of_action = duration_of_action
        self._earliest_measurement_time = earliest_measurement_time
        self._latest_measurement_time = latest_measurement_time
        self._updated = updated
        self._cause_only = cause_only
        self._number_of_correlations = number_of_correlations
        self._outcome = outcome
        self._measurements_at_last_analysis = measurements_at_last_analysis
        self._number_of_measurements = number_of_measurements
        self._last_unit = last_unit
        self._last_value = last_value
        self._most_common_value = most_common_value
        self._most_common_unit = most_common_unit
        self._last_source = last_source

    @property
    def id(self):
        """
        Gets the id of this Variable.
        Variable ID

        :return: The id of this Variable.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Variable.
        Variable ID

        :param id: The id of this Variable.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Variable.
        User-defined variable display name.

        :return: The name of this Variable.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Variable.
        User-defined variable display name.

        :param name: The name of this Variable.
        :type: str
        """

        self._name = name

    @property
    def original_name(self):
        """
        Gets the original_name of this Variable.
        Name used when the variable was originally created in the `variables` table.

        :return: The original_name of this Variable.
        :rtype: str
        """
        return self._original_name

    @original_name.setter
    def original_name(self, original_name):
        """
        Sets the original_name of this Variable.
        Name used when the variable was originally created in the `variables` table.

        :param original_name: The original_name of this Variable.
        :type: str
        """

        self._original_name = original_name

    @property
    def category(self):
        """
        Gets the category of this Variable.
        Variable category like Mood, Sleep, Physical Activity, Treatment, Symptom, etc.

        :return: The category of this Variable.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this Variable.
        Variable category like Mood, Sleep, Physical Activity, Treatment, Symptom, etc.

        :param category: The category of this Variable.
        :type: str
        """

        self._category = category

    @property
    def abbreviated_unit_name(self):
        """
        Gets the abbreviated_unit_name of this Variable.
        Abbreviated name of the default unit for the variable

        :return: The abbreviated_unit_name of this Variable.
        :rtype: str
        """
        return self._abbreviated_unit_name

    @abbreviated_unit_name.setter
    def abbreviated_unit_name(self, abbreviated_unit_name):
        """
        Sets the abbreviated_unit_name of this Variable.
        Abbreviated name of the default unit for the variable

        :param abbreviated_unit_name: The abbreviated_unit_name of this Variable.
        :type: str
        """

        self._abbreviated_unit_name = abbreviated_unit_name

    @property
    def abbreviated_unit_id(self):
        """
        Gets the abbreviated_unit_id of this Variable.
        Id of the default unit for the variable

        :return: The abbreviated_unit_id of this Variable.
        :rtype: int
        """
        return self._abbreviated_unit_id

    @abbreviated_unit_id.setter
    def abbreviated_unit_id(self, abbreviated_unit_id):
        """
        Sets the abbreviated_unit_id of this Variable.
        Id of the default unit for the variable

        :param abbreviated_unit_id: The abbreviated_unit_id of this Variable.
        :type: int
        """

        self._abbreviated_unit_id = abbreviated_unit_id

    @property
    def sources(self):
        """
        Gets the sources of this Variable.
        Comma-separated list of source names to limit variables to those sources

        :return: The sources of this Variable.
        :rtype: str
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """
        Sets the sources of this Variable.
        Comma-separated list of source names to limit variables to those sources

        :param sources: The sources of this Variable.
        :type: str
        """

        self._sources = sources

    @property
    def minimum_value(self):
        """
        Gets the minimum_value of this Variable.
        Minimum reasonable value for this variable (uses default unit)

        :return: The minimum_value of this Variable.
        :rtype: float
        """
        return self._minimum_value

    @minimum_value.setter
    def minimum_value(self, minimum_value):
        """
        Sets the minimum_value of this Variable.
        Minimum reasonable value for this variable (uses default unit)

        :param minimum_value: The minimum_value of this Variable.
        :type: float
        """

        self._minimum_value = minimum_value

    @property
    def maximum_value(self):
        """
        Gets the maximum_value of this Variable.
        Maximum reasonable value for this variable (uses default unit)

        :return: The maximum_value of this Variable.
        :rtype: float
        """
        return self._maximum_value

    @maximum_value.setter
    def maximum_value(self, maximum_value):
        """
        Sets the maximum_value of this Variable.
        Maximum reasonable value for this variable (uses default unit)

        :param maximum_value: The maximum_value of this Variable.
        :type: float
        """

        self._maximum_value = maximum_value

    @property
    def combination_operation(self):
        """
        Gets the combination_operation of this Variable.
        Way to aggregate measurements over time. Options are \"MEAN\" or \"SUM\".  SUM should be used for things like minutes of exercise.  If you use MEAN for exercise, then a person might exercise more minutes in one day but add separate measurements that were smaller.  So when we are doing correlational analysis, we would think that the person exercised less that day even though they exercised more.  Conversely, we must use MEAN for things such as ratings which cannot be SUMMED.

        :return: The combination_operation of this Variable.
        :rtype: str
        """
        return self._combination_operation

    @combination_operation.setter
    def combination_operation(self, combination_operation):
        """
        Sets the combination_operation of this Variable.
        Way to aggregate measurements over time. Options are \"MEAN\" or \"SUM\".  SUM should be used for things like minutes of exercise.  If you use MEAN for exercise, then a person might exercise more minutes in one day but add separate measurements that were smaller.  So when we are doing correlational analysis, we would think that the person exercised less that day even though they exercised more.  Conversely, we must use MEAN for things such as ratings which cannot be SUMMED.

        :param combination_operation: The combination_operation of this Variable.
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
    def filling_value(self):
        """
        Gets the filling_value of this Variable.
        Value for replacing null measurements

        :return: The filling_value of this Variable.
        :rtype: float
        """
        return self._filling_value

    @filling_value.setter
    def filling_value(self, filling_value):
        """
        Sets the filling_value of this Variable.
        Value for replacing null measurements

        :param filling_value: The filling_value of this Variable.
        :type: float
        """

        self._filling_value = filling_value

    @property
    def join_with(self):
        """
        Gets the join_with of this Variable.
        The Variable this Variable should be joined with. If the variable is joined with some other variable then it is not shown to user in the list of variables.

        :return: The join_with of this Variable.
        :rtype: str
        """
        return self._join_with

    @join_with.setter
    def join_with(self, join_with):
        """
        Sets the join_with of this Variable.
        The Variable this Variable should be joined with. If the variable is joined with some other variable then it is not shown to user in the list of variables.

        :param join_with: The join_with of this Variable.
        :type: str
        """

        self._join_with = join_with

    @property
    def joined_variables(self):
        """
        Gets the joined_variables of this Variable.
        Array of Variables that are joined with this Variable

        :return: The joined_variables of this Variable.
        :rtype: list[Variable]
        """
        return self._joined_variables

    @joined_variables.setter
    def joined_variables(self, joined_variables):
        """
        Sets the joined_variables of this Variable.
        Array of Variables that are joined with this Variable

        :param joined_variables: The joined_variables of this Variable.
        :type: list[Variable]
        """

        self._joined_variables = joined_variables

    @property
    def parent(self):
        """
        Gets the parent of this Variable.
        Id of the parent variable if this variable has any parent

        :return: The parent of this Variable.
        :rtype: int
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this Variable.
        Id of the parent variable if this variable has any parent

        :param parent: The parent of this Variable.
        :type: int
        """

        self._parent = parent

    @property
    def sub_variables(self):
        """
        Gets the sub_variables of this Variable.
        Array of Variables that are sub variables to this Variable

        :return: The sub_variables of this Variable.
        :rtype: list[Variable]
        """
        return self._sub_variables

    @sub_variables.setter
    def sub_variables(self, sub_variables):
        """
        Sets the sub_variables of this Variable.
        Array of Variables that are sub variables to this Variable

        :param sub_variables: The sub_variables of this Variable.
        :type: list[Variable]
        """

        self._sub_variables = sub_variables

    @property
    def onset_delay(self):
        """
        Gets the onset_delay of this Variable.
        How long it takes for a measurement in this variable to take effect

        :return: The onset_delay of this Variable.
        :rtype: int
        """
        return self._onset_delay

    @onset_delay.setter
    def onset_delay(self, onset_delay):
        """
        Sets the onset_delay of this Variable.
        How long it takes for a measurement in this variable to take effect

        :param onset_delay: The onset_delay of this Variable.
        :type: int
        """

        self._onset_delay = onset_delay

    @property
    def duration_of_action(self):
        """
        Gets the duration_of_action of this Variable.
        How long the effect of a measurement in this variable lasts

        :return: The duration_of_action of this Variable.
        :rtype: int
        """
        return self._duration_of_action

    @duration_of_action.setter
    def duration_of_action(self, duration_of_action):
        """
        Sets the duration_of_action of this Variable.
        How long the effect of a measurement in this variable lasts

        :param duration_of_action: The duration_of_action of this Variable.
        :type: int
        """

        self._duration_of_action = duration_of_action

    @property
    def earliest_measurement_time(self):
        """
        Gets the earliest_measurement_time of this Variable.
        Earliest measurement time

        :return: The earliest_measurement_time of this Variable.
        :rtype: int
        """
        return self._earliest_measurement_time

    @earliest_measurement_time.setter
    def earliest_measurement_time(self, earliest_measurement_time):
        """
        Sets the earliest_measurement_time of this Variable.
        Earliest measurement time

        :param earliest_measurement_time: The earliest_measurement_time of this Variable.
        :type: int
        """

        self._earliest_measurement_time = earliest_measurement_time

    @property
    def latest_measurement_time(self):
        """
        Gets the latest_measurement_time of this Variable.
        Latest measurement time

        :return: The latest_measurement_time of this Variable.
        :rtype: int
        """
        return self._latest_measurement_time

    @latest_measurement_time.setter
    def latest_measurement_time(self, latest_measurement_time):
        """
        Sets the latest_measurement_time of this Variable.
        Latest measurement time

        :param latest_measurement_time: The latest_measurement_time of this Variable.
        :type: int
        """

        self._latest_measurement_time = latest_measurement_time

    @property
    def updated(self):
        """
        Gets the updated of this Variable.
        When this variable or its settings were last updated

        :return: The updated of this Variable.
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this Variable.
        When this variable or its settings were last updated

        :param updated: The updated of this Variable.
        :type: int
        """

        self._updated = updated

    @property
    def cause_only(self):
        """
        Gets the cause_only of this Variable.
        A value of 1 indicates that this variable is generally a cause in a causal relationship.  An example of a causeOnly variable would be a variable such as Cloud Cover which would generally not be influenced by the behaviour of the user.

        :return: The cause_only of this Variable.
        :rtype: int
        """
        return self._cause_only

    @cause_only.setter
    def cause_only(self, cause_only):
        """
        Sets the cause_only of this Variable.
        A value of 1 indicates that this variable is generally a cause in a causal relationship.  An example of a causeOnly variable would be a variable such as Cloud Cover which would generally not be influenced by the behaviour of the user.

        :param cause_only: The cause_only of this Variable.
        :type: int
        """

        self._cause_only = cause_only

    @property
    def number_of_correlations(self):
        """
        Gets the number_of_correlations of this Variable.
        Number of correlations

        :return: The number_of_correlations of this Variable.
        :rtype: int
        """
        return self._number_of_correlations

    @number_of_correlations.setter
    def number_of_correlations(self, number_of_correlations):
        """
        Sets the number_of_correlations of this Variable.
        Number of correlations

        :param number_of_correlations: The number_of_correlations of this Variable.
        :type: int
        """

        self._number_of_correlations = number_of_correlations

    @property
    def outcome(self):
        """
        Gets the outcome of this Variable.
        Outcome variables (those with `outcome` == 1) are variables for which a human would generally want to identify the influencing factors.  These include symptoms of illness, physique, mood, cognitive performance, etc.  Generally correlation calculations are only performed on outcome variables.

        :return: The outcome of this Variable.
        :rtype: int
        """
        return self._outcome

    @outcome.setter
    def outcome(self, outcome):
        """
        Sets the outcome of this Variable.
        Outcome variables (those with `outcome` == 1) are variables for which a human would generally want to identify the influencing factors.  These include symptoms of illness, physique, mood, cognitive performance, etc.  Generally correlation calculations are only performed on outcome variables.

        :param outcome: The outcome of this Variable.
        :type: int
        """

        self._outcome = outcome

    @property
    def measurements_at_last_analysis(self):
        """
        Gets the measurements_at_last_analysis of this Variable.
        The number of measurements that a given user had for this variable the last time a correlation calculation was performed. Generally correlation values are only updated once the current number of measurements for a variable is more than 10% greater than the measurementsAtLastAnalysis.  This avoids a computationally-demanding recalculation when there's not enough new data to make a significant difference in the correlation.

        :return: The measurements_at_last_analysis of this Variable.
        :rtype: int
        """
        return self._measurements_at_last_analysis

    @measurements_at_last_analysis.setter
    def measurements_at_last_analysis(self, measurements_at_last_analysis):
        """
        Sets the measurements_at_last_analysis of this Variable.
        The number of measurements that a given user had for this variable the last time a correlation calculation was performed. Generally correlation values are only updated once the current number of measurements for a variable is more than 10% greater than the measurementsAtLastAnalysis.  This avoids a computationally-demanding recalculation when there's not enough new data to make a significant difference in the correlation.

        :param measurements_at_last_analysis: The measurements_at_last_analysis of this Variable.
        :type: int
        """

        self._measurements_at_last_analysis = measurements_at_last_analysis

    @property
    def number_of_measurements(self):
        """
        Gets the number_of_measurements of this Variable.
        Number of measurements

        :return: The number_of_measurements of this Variable.
        :rtype: int
        """
        return self._number_of_measurements

    @number_of_measurements.setter
    def number_of_measurements(self, number_of_measurements):
        """
        Sets the number_of_measurements of this Variable.
        Number of measurements

        :param number_of_measurements: The number_of_measurements of this Variable.
        :type: int
        """

        self._number_of_measurements = number_of_measurements

    @property
    def last_unit(self):
        """
        Gets the last_unit of this Variable.
        Last unit

        :return: The last_unit of this Variable.
        :rtype: str
        """
        return self._last_unit

    @last_unit.setter
    def last_unit(self, last_unit):
        """
        Sets the last_unit of this Variable.
        Last unit

        :param last_unit: The last_unit of this Variable.
        :type: str
        """

        self._last_unit = last_unit

    @property
    def last_value(self):
        """
        Gets the last_value of this Variable.
        Last value

        :return: The last_value of this Variable.
        :rtype: int
        """
        return self._last_value

    @last_value.setter
    def last_value(self, last_value):
        """
        Sets the last_value of this Variable.
        Last value

        :param last_value: The last_value of this Variable.
        :type: int
        """

        self._last_value = last_value

    @property
    def most_common_value(self):
        """
        Gets the most_common_value of this Variable.
        Most common value

        :return: The most_common_value of this Variable.
        :rtype: int
        """
        return self._most_common_value

    @most_common_value.setter
    def most_common_value(self, most_common_value):
        """
        Sets the most_common_value of this Variable.
        Most common value

        :param most_common_value: The most_common_value of this Variable.
        :type: int
        """

        self._most_common_value = most_common_value

    @property
    def most_common_unit(self):
        """
        Gets the most_common_unit of this Variable.
        Most common unit

        :return: The most_common_unit of this Variable.
        :rtype: str
        """
        return self._most_common_unit

    @most_common_unit.setter
    def most_common_unit(self, most_common_unit):
        """
        Sets the most_common_unit of this Variable.
        Most common unit

        :param most_common_unit: The most_common_unit of this Variable.
        :type: str
        """

        self._most_common_unit = most_common_unit

    @property
    def last_source(self):
        """
        Gets the last_source of this Variable.
        Last source

        :return: The last_source of this Variable.
        :rtype: int
        """
        return self._last_source

    @last_source.setter
    def last_source(self, last_source):
        """
        Sets the last_source of this Variable.
        Last source

        :param last_source: The last_source of this Variable.
        :type: int
        """

        self._last_source = last_source

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
