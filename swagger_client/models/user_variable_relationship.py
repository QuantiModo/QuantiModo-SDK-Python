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


class UserVariableRelationship(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, confidence_level=None, confidence_score=None, direction=None, duration_of_action=None, error_message=None, onset_delay=None, outcome_variable_id=None, predictor_variable_id=None, predictor_unit_id=None, sinn_rank=None, strength_level=None, strength_score=None, user_id=None, vote=None, value_predicting_high_outcome=None, value_predicting_low_outcome=None):
        """
        UserVariableRelationship - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'confidence_level': 'str',
            'confidence_score': 'float',
            'direction': 'str',
            'duration_of_action': 'int',
            'error_message': 'str',
            'onset_delay': 'int',
            'outcome_variable_id': 'int',
            'predictor_variable_id': 'int',
            'predictor_unit_id': 'int',
            'sinn_rank': 'float',
            'strength_level': 'str',
            'strength_score': 'float',
            'user_id': 'int',
            'vote': 'str',
            'value_predicting_high_outcome': 'float',
            'value_predicting_low_outcome': 'float'
        }

        self.attribute_map = {
            'id': 'id',
            'confidence_level': 'confidence_level',
            'confidence_score': 'confidence_score',
            'direction': 'direction',
            'duration_of_action': 'duration_of_action',
            'error_message': 'error_message',
            'onset_delay': 'onset_delay',
            'outcome_variable_id': 'outcome_variable_id',
            'predictor_variable_id': 'predictor_variable_id',
            'predictor_unit_id': 'predictor_unit_id',
            'sinn_rank': 'sinn_rank',
            'strength_level': 'strength_level',
            'strength_score': 'strength_score',
            'user_id': 'user_id',
            'vote': 'vote',
            'value_predicting_high_outcome': 'value_predicting_high_outcome',
            'value_predicting_low_outcome': 'value_predicting_low_outcome'
        }

        self._id = id
        self._confidence_level = confidence_level
        self._confidence_score = confidence_score
        self._direction = direction
        self._duration_of_action = duration_of_action
        self._error_message = error_message
        self._onset_delay = onset_delay
        self._outcome_variable_id = outcome_variable_id
        self._predictor_variable_id = predictor_variable_id
        self._predictor_unit_id = predictor_unit_id
        self._sinn_rank = sinn_rank
        self._strength_level = strength_level
        self._strength_score = strength_score
        self._user_id = user_id
        self._vote = vote
        self._value_predicting_high_outcome = value_predicting_high_outcome
        self._value_predicting_low_outcome = value_predicting_low_outcome

    @property
    def id(self):
        """
        Gets the id of this UserVariableRelationship.
        id

        :return: The id of this UserVariableRelationship.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UserVariableRelationship.
        id

        :param id: The id of this UserVariableRelationship.
        :type: int
        """

        self._id = id

    @property
    def confidence_level(self):
        """
        Gets the confidence_level of this UserVariableRelationship.
        Our confidence that a consistent predictive relationship exists based on the amount of evidence, reproducibility, and other factors

        :return: The confidence_level of this UserVariableRelationship.
        :rtype: str
        """
        return self._confidence_level

    @confidence_level.setter
    def confidence_level(self, confidence_level):
        """
        Sets the confidence_level of this UserVariableRelationship.
        Our confidence that a consistent predictive relationship exists based on the amount of evidence, reproducibility, and other factors

        :param confidence_level: The confidence_level of this UserVariableRelationship.
        :type: str
        """

        self._confidence_level = confidence_level

    @property
    def confidence_score(self):
        """
        Gets the confidence_score of this UserVariableRelationship.
        A quantitative representation of our confidence that a consistent predictive relationship exists based on the amount of evidence, reproducibility, and other factors

        :return: The confidence_score of this UserVariableRelationship.
        :rtype: float
        """
        return self._confidence_score

    @confidence_score.setter
    def confidence_score(self, confidence_score):
        """
        Sets the confidence_score of this UserVariableRelationship.
        A quantitative representation of our confidence that a consistent predictive relationship exists based on the amount of evidence, reproducibility, and other factors

        :param confidence_score: The confidence_score of this UserVariableRelationship.
        :type: float
        """

        self._confidence_score = confidence_score

    @property
    def direction(self):
        """
        Gets the direction of this UserVariableRelationship.
        Direction is positive if higher predictor values generally precede higher outcome values. Direction is negative if higher predictor values generally precede lower outcome values.

        :return: The direction of this UserVariableRelationship.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        Sets the direction of this UserVariableRelationship.
        Direction is positive if higher predictor values generally precede higher outcome values. Direction is negative if higher predictor values generally precede lower outcome values.

        :param direction: The direction of this UserVariableRelationship.
        :type: str
        """

        self._direction = direction

    @property
    def duration_of_action(self):
        """
        Gets the duration_of_action of this UserVariableRelationship.
        Number of seconds over which the predictor variable event is expected to produce a perceivable effect following the onset delay

        :return: The duration_of_action of this UserVariableRelationship.
        :rtype: int
        """
        return self._duration_of_action

    @duration_of_action.setter
    def duration_of_action(self, duration_of_action):
        """
        Sets the duration_of_action of this UserVariableRelationship.
        Number of seconds over which the predictor variable event is expected to produce a perceivable effect following the onset delay

        :param duration_of_action: The duration_of_action of this UserVariableRelationship.
        :type: int
        """

        self._duration_of_action = duration_of_action

    @property
    def error_message(self):
        """
        Gets the error_message of this UserVariableRelationship.
        error_message

        :return: The error_message of this UserVariableRelationship.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this UserVariableRelationship.
        error_message

        :param error_message: The error_message of this UserVariableRelationship.
        :type: str
        """

        self._error_message = error_message

    @property
    def onset_delay(self):
        """
        Gets the onset_delay of this UserVariableRelationship.
        User estimated (or default number of seconds) after cause measurement before a perceivable effect is observed

        :return: The onset_delay of this UserVariableRelationship.
        :rtype: int
        """
        return self._onset_delay

    @onset_delay.setter
    def onset_delay(self, onset_delay):
        """
        Sets the onset_delay of this UserVariableRelationship.
        User estimated (or default number of seconds) after cause measurement before a perceivable effect is observed

        :param onset_delay: The onset_delay of this UserVariableRelationship.
        :type: int
        """

        self._onset_delay = onset_delay

    @property
    def outcome_variable_id(self):
        """
        Gets the outcome_variable_id of this UserVariableRelationship.
        Variable ID for the outcome variable

        :return: The outcome_variable_id of this UserVariableRelationship.
        :rtype: int
        """
        return self._outcome_variable_id

    @outcome_variable_id.setter
    def outcome_variable_id(self, outcome_variable_id):
        """
        Sets the outcome_variable_id of this UserVariableRelationship.
        Variable ID for the outcome variable

        :param outcome_variable_id: The outcome_variable_id of this UserVariableRelationship.
        :type: int
        """

        self._outcome_variable_id = outcome_variable_id

    @property
    def predictor_variable_id(self):
        """
        Gets the predictor_variable_id of this UserVariableRelationship.
        Variable ID for the predictor variable

        :return: The predictor_variable_id of this UserVariableRelationship.
        :rtype: int
        """
        return self._predictor_variable_id

    @predictor_variable_id.setter
    def predictor_variable_id(self, predictor_variable_id):
        """
        Sets the predictor_variable_id of this UserVariableRelationship.
        Variable ID for the predictor variable

        :param predictor_variable_id: The predictor_variable_id of this UserVariableRelationship.
        :type: int
        """

        self._predictor_variable_id = predictor_variable_id

    @property
    def predictor_unit_id(self):
        """
        Gets the predictor_unit_id of this UserVariableRelationship.
        ID for default unit of the predictor variable

        :return: The predictor_unit_id of this UserVariableRelationship.
        :rtype: int
        """
        return self._predictor_unit_id

    @predictor_unit_id.setter
    def predictor_unit_id(self, predictor_unit_id):
        """
        Sets the predictor_unit_id of this UserVariableRelationship.
        ID for default unit of the predictor variable

        :param predictor_unit_id: The predictor_unit_id of this UserVariableRelationship.
        :type: int
        """

        self._predictor_unit_id = predictor_unit_id

    @property
    def sinn_rank(self):
        """
        Gets the sinn_rank of this UserVariableRelationship.
        A value representative of the relevance of this predictor relative to other predictors of this outcome.  Usually used for relevancy sorting.

        :return: The sinn_rank of this UserVariableRelationship.
        :rtype: float
        """
        return self._sinn_rank

    @sinn_rank.setter
    def sinn_rank(self, sinn_rank):
        """
        Sets the sinn_rank of this UserVariableRelationship.
        A value representative of the relevance of this predictor relative to other predictors of this outcome.  Usually used for relevancy sorting.

        :param sinn_rank: The sinn_rank of this UserVariableRelationship.
        :type: float
        """

        self._sinn_rank = sinn_rank

    @property
    def strength_level(self):
        """
        Gets the strength_level of this UserVariableRelationship.
        Can be weak, medium, or strong based on the size of the effect which the predictor appears to have on the outcome relative to other variable relationship strength scores.

        :return: The strength_level of this UserVariableRelationship.
        :rtype: str
        """
        return self._strength_level

    @strength_level.setter
    def strength_level(self, strength_level):
        """
        Sets the strength_level of this UserVariableRelationship.
        Can be weak, medium, or strong based on the size of the effect which the predictor appears to have on the outcome relative to other variable relationship strength scores.

        :param strength_level: The strength_level of this UserVariableRelationship.
        :type: str
        """

        self._strength_level = strength_level

    @property
    def strength_score(self):
        """
        Gets the strength_score of this UserVariableRelationship.
        A value represented to the size of the effect which the predictor appears to have on the outcome.

        :return: The strength_score of this UserVariableRelationship.
        :rtype: float
        """
        return self._strength_score

    @strength_score.setter
    def strength_score(self, strength_score):
        """
        Sets the strength_score of this UserVariableRelationship.
        A value represented to the size of the effect which the predictor appears to have on the outcome.

        :param strength_score: The strength_score of this UserVariableRelationship.
        :type: float
        """

        self._strength_score = strength_score

    @property
    def user_id(self):
        """
        Gets the user_id of this UserVariableRelationship.
        user_id

        :return: The user_id of this UserVariableRelationship.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this UserVariableRelationship.
        user_id

        :param user_id: The user_id of this UserVariableRelationship.
        :type: int
        """

        self._user_id = user_id

    @property
    def vote(self):
        """
        Gets the vote of this UserVariableRelationship.
        vote

        :return: The vote of this UserVariableRelationship.
        :rtype: str
        """
        return self._vote

    @vote.setter
    def vote(self, vote):
        """
        Sets the vote of this UserVariableRelationship.
        vote

        :param vote: The vote of this UserVariableRelationship.
        :type: str
        """

        self._vote = vote

    @property
    def value_predicting_high_outcome(self):
        """
        Gets the value_predicting_high_outcome of this UserVariableRelationship.
        Value for the predictor variable (in it's default unit) which typically precedes an above average outcome value

        :return: The value_predicting_high_outcome of this UserVariableRelationship.
        :rtype: float
        """
        return self._value_predicting_high_outcome

    @value_predicting_high_outcome.setter
    def value_predicting_high_outcome(self, value_predicting_high_outcome):
        """
        Sets the value_predicting_high_outcome of this UserVariableRelationship.
        Value for the predictor variable (in it's default unit) which typically precedes an above average outcome value

        :param value_predicting_high_outcome: The value_predicting_high_outcome of this UserVariableRelationship.
        :type: float
        """

        self._value_predicting_high_outcome = value_predicting_high_outcome

    @property
    def value_predicting_low_outcome(self):
        """
        Gets the value_predicting_low_outcome of this UserVariableRelationship.
        Value for the predictor variable (in it's default unit) which typically precedes a below average outcome value

        :return: The value_predicting_low_outcome of this UserVariableRelationship.
        :rtype: float
        """
        return self._value_predicting_low_outcome

    @value_predicting_low_outcome.setter
    def value_predicting_low_outcome(self, value_predicting_low_outcome):
        """
        Sets the value_predicting_low_outcome of this UserVariableRelationship.
        Value for the predictor variable (in it's default unit) which typically precedes a below average outcome value

        :param value_predicting_low_outcome: The value_predicting_low_outcome of this UserVariableRelationship.
        :type: float
        """

        self._value_predicting_low_outcome = value_predicting_low_outcome

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
