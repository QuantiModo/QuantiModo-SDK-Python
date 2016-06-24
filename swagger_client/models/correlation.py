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


class Correlation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, correlation_coefficient=None, cause=None, original_cause=None, effect=None, original_effect=None, onset_delay=None, duration_of_action=None, number_of_pairs=None, effect_size=None, statistical_significance=None, timestamp=None, reverse_correlation=None, causality_factor=None, cause_category=None, effect_category=None, value_predicting_high_outcome=None, value_predicting_low_outcome=None, optimal_pearson_product=None, average_vote=None, user_vote=None, cause_unit=None, cause_unit_id=None):
        """
        Correlation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'correlation_coefficient': 'float',
            'cause': 'str',
            'original_cause': 'str',
            'effect': 'str',
            'original_effect': 'str',
            'onset_delay': 'float',
            'duration_of_action': 'float',
            'number_of_pairs': 'float',
            'effect_size': 'str',
            'statistical_significance': 'str',
            'timestamp': 'float',
            'reverse_correlation': 'float',
            'causality_factor': 'float',
            'cause_category': 'str',
            'effect_category': 'str',
            'value_predicting_high_outcome': 'float',
            'value_predicting_low_outcome': 'float',
            'optimal_pearson_product': 'float',
            'average_vote': 'float',
            'user_vote': 'float',
            'cause_unit': 'str',
            'cause_unit_id': 'int'
        }

        self.attribute_map = {
            'correlation_coefficient': 'correlationCoefficient',
            'cause': 'cause',
            'original_cause': 'originalCause',
            'effect': 'effect',
            'original_effect': 'originalEffect',
            'onset_delay': 'onsetDelay',
            'duration_of_action': 'durationOfAction',
            'number_of_pairs': 'numberOfPairs',
            'effect_size': 'effectSize',
            'statistical_significance': 'statisticalSignificance',
            'timestamp': 'timestamp',
            'reverse_correlation': 'reverseCorrelation',
            'causality_factor': 'causalityFactor',
            'cause_category': 'causeCategory',
            'effect_category': 'effectCategory',
            'value_predicting_high_outcome': 'valuePredictingHighOutcome',
            'value_predicting_low_outcome': 'valuePredictingLowOutcome',
            'optimal_pearson_product': 'optimalPearsonProduct',
            'average_vote': 'averageVote',
            'user_vote': 'userVote',
            'cause_unit': 'causeUnit',
            'cause_unit_id': 'causeUnitId'
        }

        self._correlation_coefficient = correlation_coefficient
        self._cause = cause
        self._original_cause = original_cause
        self._effect = effect
        self._original_effect = original_effect
        self._onset_delay = onset_delay
        self._duration_of_action = duration_of_action
        self._number_of_pairs = number_of_pairs
        self._effect_size = effect_size
        self._statistical_significance = statistical_significance
        self._timestamp = timestamp
        self._reverse_correlation = reverse_correlation
        self._causality_factor = causality_factor
        self._cause_category = cause_category
        self._effect_category = effect_category
        self._value_predicting_high_outcome = value_predicting_high_outcome
        self._value_predicting_low_outcome = value_predicting_low_outcome
        self._optimal_pearson_product = optimal_pearson_product
        self._average_vote = average_vote
        self._user_vote = user_vote
        self._cause_unit = cause_unit
        self._cause_unit_id = cause_unit_id

    @property
    def correlation_coefficient(self):
        """
        Gets the correlation_coefficient of this Correlation.
        Pearson correlation coefficient between cause and effect measurements

        :return: The correlation_coefficient of this Correlation.
        :rtype: float
        """
        return self._correlation_coefficient

    @correlation_coefficient.setter
    def correlation_coefficient(self, correlation_coefficient):
        """
        Sets the correlation_coefficient of this Correlation.
        Pearson correlation coefficient between cause and effect measurements

        :param correlation_coefficient: The correlation_coefficient of this Correlation.
        :type: float
        """

        self._correlation_coefficient = correlation_coefficient

    @property
    def cause(self):
        """
        Gets the cause of this Correlation.
        ORIGINAL variable name of the cause variable for which the user desires correlations.

        :return: The cause of this Correlation.
        :rtype: str
        """
        return self._cause

    @cause.setter
    def cause(self, cause):
        """
        Sets the cause of this Correlation.
        ORIGINAL variable name of the cause variable for which the user desires correlations.

        :param cause: The cause of this Correlation.
        :type: str
        """

        self._cause = cause

    @property
    def original_cause(self):
        """
        Gets the original_cause of this Correlation.
        original name of the cause.

        :return: The original_cause of this Correlation.
        :rtype: str
        """
        return self._original_cause

    @original_cause.setter
    def original_cause(self, original_cause):
        """
        Sets the original_cause of this Correlation.
        original name of the cause.

        :param original_cause: The original_cause of this Correlation.
        :type: str
        """

        self._original_cause = original_cause

    @property
    def effect(self):
        """
        Gets the effect of this Correlation.
        ORIGINAL variable name of the effect variable for which the user desires correlations.

        :return: The effect of this Correlation.
        :rtype: str
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """
        Sets the effect of this Correlation.
        ORIGINAL variable name of the effect variable for which the user desires correlations.

        :param effect: The effect of this Correlation.
        :type: str
        """

        self._effect = effect

    @property
    def original_effect(self):
        """
        Gets the original_effect of this Correlation.
        effect variable original name.

        :return: The original_effect of this Correlation.
        :rtype: str
        """
        return self._original_effect

    @original_effect.setter
    def original_effect(self, original_effect):
        """
        Sets the original_effect of this Correlation.
        effect variable original name.

        :param original_effect: The original_effect of this Correlation.
        :type: str
        """

        self._original_effect = original_effect

    @property
    def onset_delay(self):
        """
        Gets the onset_delay of this Correlation.
        User estimated or default time after cause measurement before a perceivable effect is observed

        :return: The onset_delay of this Correlation.
        :rtype: float
        """
        return self._onset_delay

    @onset_delay.setter
    def onset_delay(self, onset_delay):
        """
        Sets the onset_delay of this Correlation.
        User estimated or default time after cause measurement before a perceivable effect is observed

        :param onset_delay: The onset_delay of this Correlation.
        :type: float
        """

        self._onset_delay = onset_delay

    @property
    def duration_of_action(self):
        """
        Gets the duration_of_action of this Correlation.
        Time over which the cause is expected to produce a perceivable effect following the onset delay

        :return: The duration_of_action of this Correlation.
        :rtype: float
        """
        return self._duration_of_action

    @duration_of_action.setter
    def duration_of_action(self, duration_of_action):
        """
        Sets the duration_of_action of this Correlation.
        Time over which the cause is expected to produce a perceivable effect following the onset delay

        :param duration_of_action: The duration_of_action of this Correlation.
        :type: float
        """

        self._duration_of_action = duration_of_action

    @property
    def number_of_pairs(self):
        """
        Gets the number_of_pairs of this Correlation.
        Number of points that went into the correlation calculation

        :return: The number_of_pairs of this Correlation.
        :rtype: float
        """
        return self._number_of_pairs

    @number_of_pairs.setter
    def number_of_pairs(self, number_of_pairs):
        """
        Sets the number_of_pairs of this Correlation.
        Number of points that went into the correlation calculation

        :param number_of_pairs: The number_of_pairs of this Correlation.
        :type: float
        """

        self._number_of_pairs = number_of_pairs

    @property
    def effect_size(self):
        """
        Gets the effect_size of this Correlation.
        Magnitude of the effects of a cause indicating whether it's practically meaningful.

        :return: The effect_size of this Correlation.
        :rtype: str
        """
        return self._effect_size

    @effect_size.setter
    def effect_size(self, effect_size):
        """
        Sets the effect_size of this Correlation.
        Magnitude of the effects of a cause indicating whether it's practically meaningful.

        :param effect_size: The effect_size of this Correlation.
        :type: str
        """

        self._effect_size = effect_size

    @property
    def statistical_significance(self):
        """
        Gets the statistical_significance of this Correlation.
        A function of the effect size and sample size

        :return: The statistical_significance of this Correlation.
        :rtype: str
        """
        return self._statistical_significance

    @statistical_significance.setter
    def statistical_significance(self, statistical_significance):
        """
        Sets the statistical_significance of this Correlation.
        A function of the effect size and sample size

        :param statistical_significance: The statistical_significance of this Correlation.
        :type: str
        """

        self._statistical_significance = statistical_significance

    @property
    def timestamp(self):
        """
        Gets the timestamp of this Correlation.
        Time at which correlation was calculated

        :return: The timestamp of this Correlation.
        :rtype: float
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this Correlation.
        Time at which correlation was calculated

        :param timestamp: The timestamp of this Correlation.
        :type: float
        """

        self._timestamp = timestamp

    @property
    def reverse_correlation(self):
        """
        Gets the reverse_correlation of this Correlation.
        Correlation when cause and effect are reversed. For any causal relationship, the forward correlation should exceed the reverse correlation.

        :return: The reverse_correlation of this Correlation.
        :rtype: float
        """
        return self._reverse_correlation

    @reverse_correlation.setter
    def reverse_correlation(self, reverse_correlation):
        """
        Sets the reverse_correlation of this Correlation.
        Correlation when cause and effect are reversed. For any causal relationship, the forward correlation should exceed the reverse correlation.

        :param reverse_correlation: The reverse_correlation of this Correlation.
        :type: float
        """

        self._reverse_correlation = reverse_correlation

    @property
    def causality_factor(self):
        """
        Gets the causality_factor of this Correlation.
        

        :return: The causality_factor of this Correlation.
        :rtype: float
        """
        return self._causality_factor

    @causality_factor.setter
    def causality_factor(self, causality_factor):
        """
        Sets the causality_factor of this Correlation.
        

        :param causality_factor: The causality_factor of this Correlation.
        :type: float
        """

        self._causality_factor = causality_factor

    @property
    def cause_category(self):
        """
        Gets the cause_category of this Correlation.
        Variable category of the cause variable.

        :return: The cause_category of this Correlation.
        :rtype: str
        """
        return self._cause_category

    @cause_category.setter
    def cause_category(self, cause_category):
        """
        Sets the cause_category of this Correlation.
        Variable category of the cause variable.

        :param cause_category: The cause_category of this Correlation.
        :type: str
        """

        self._cause_category = cause_category

    @property
    def effect_category(self):
        """
        Gets the effect_category of this Correlation.
        Variable category of the effect variable.

        :return: The effect_category of this Correlation.
        :rtype: str
        """
        return self._effect_category

    @effect_category.setter
    def effect_category(self, effect_category):
        """
        Sets the effect_category of this Correlation.
        Variable category of the effect variable.

        :param effect_category: The effect_category of this Correlation.
        :type: str
        """

        self._effect_category = effect_category

    @property
    def value_predicting_high_outcome(self):
        """
        Gets the value_predicting_high_outcome of this Correlation.
        cause value that predicts an above average effect value (in default unit for cause variable)

        :return: The value_predicting_high_outcome of this Correlation.
        :rtype: float
        """
        return self._value_predicting_high_outcome

    @value_predicting_high_outcome.setter
    def value_predicting_high_outcome(self, value_predicting_high_outcome):
        """
        Sets the value_predicting_high_outcome of this Correlation.
        cause value that predicts an above average effect value (in default unit for cause variable)

        :param value_predicting_high_outcome: The value_predicting_high_outcome of this Correlation.
        :type: float
        """

        self._value_predicting_high_outcome = value_predicting_high_outcome

    @property
    def value_predicting_low_outcome(self):
        """
        Gets the value_predicting_low_outcome of this Correlation.
        cause value that predicts a below average effect value (in default unit for cause variable)

        :return: The value_predicting_low_outcome of this Correlation.
        :rtype: float
        """
        return self._value_predicting_low_outcome

    @value_predicting_low_outcome.setter
    def value_predicting_low_outcome(self, value_predicting_low_outcome):
        """
        Sets the value_predicting_low_outcome of this Correlation.
        cause value that predicts a below average effect value (in default unit for cause variable)

        :param value_predicting_low_outcome: The value_predicting_low_outcome of this Correlation.
        :type: float
        """

        self._value_predicting_low_outcome = value_predicting_low_outcome

    @property
    def optimal_pearson_product(self):
        """
        Gets the optimal_pearson_product of this Correlation.
        Optimal Pearson Product

        :return: The optimal_pearson_product of this Correlation.
        :rtype: float
        """
        return self._optimal_pearson_product

    @optimal_pearson_product.setter
    def optimal_pearson_product(self, optimal_pearson_product):
        """
        Sets the optimal_pearson_product of this Correlation.
        Optimal Pearson Product

        :param optimal_pearson_product: The optimal_pearson_product of this Correlation.
        :type: float
        """

        self._optimal_pearson_product = optimal_pearson_product

    @property
    def average_vote(self):
        """
        Gets the average_vote of this Correlation.
        Average Vote

        :return: The average_vote of this Correlation.
        :rtype: float
        """
        return self._average_vote

    @average_vote.setter
    def average_vote(self, average_vote):
        """
        Sets the average_vote of this Correlation.
        Average Vote

        :param average_vote: The average_vote of this Correlation.
        :type: float
        """

        self._average_vote = average_vote

    @property
    def user_vote(self):
        """
        Gets the user_vote of this Correlation.
        User Vote

        :return: The user_vote of this Correlation.
        :rtype: float
        """
        return self._user_vote

    @user_vote.setter
    def user_vote(self, user_vote):
        """
        Sets the user_vote of this Correlation.
        User Vote

        :param user_vote: The user_vote of this Correlation.
        :type: float
        """

        self._user_vote = user_vote

    @property
    def cause_unit(self):
        """
        Gets the cause_unit of this Correlation.
        Unit of the predictor variable

        :return: The cause_unit of this Correlation.
        :rtype: str
        """
        return self._cause_unit

    @cause_unit.setter
    def cause_unit(self, cause_unit):
        """
        Sets the cause_unit of this Correlation.
        Unit of the predictor variable

        :param cause_unit: The cause_unit of this Correlation.
        :type: str
        """

        self._cause_unit = cause_unit

    @property
    def cause_unit_id(self):
        """
        Gets the cause_unit_id of this Correlation.
        Unit Id of the predictor variable

        :return: The cause_unit_id of this Correlation.
        :rtype: int
        """
        return self._cause_unit_id

    @cause_unit_id.setter
    def cause_unit_id(self, cause_unit_id):
        """
        Sets the cause_unit_id of this Correlation.
        Unit Id of the predictor variable

        :param cause_unit_id: The cause_unit_id of this Correlation.
        :type: int
        """

        self._cause_unit_id = cause_unit_id

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
