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


class TrackingReminder(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, client_id=None, user_id=None, variable_id=None, default_value=None, reminder_start_time=None, reminder_end_time=None, reminder_sound=None, reminder_frequency=None, pop_up=None, sms=None, email=None, notification_bar=None, last_reminded=None, last_tracked=None, first_daily_reminder_time=None, second_daily_reminder_time=None, third_daily_reminder_time=None, start_tracking_date=None, stop_tracking_date=None, updated_at=None, variable_name=None, variable_category_name=None, abbreviated_unit_name=None, combination_operation=None):
        """
        TrackingReminder - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'client_id': 'str',
            'user_id': 'int',
            'variable_id': 'int',
            'default_value': 'float',
            'reminder_start_time': 'str',
            'reminder_end_time': 'str',
            'reminder_sound': 'str',
            'reminder_frequency': 'int',
            'pop_up': 'bool',
            'sms': 'bool',
            'email': 'bool',
            'notification_bar': 'bool',
            'last_reminded': 'datetime',
            'last_tracked': 'datetime',
            'first_daily_reminder_time': 'str',
            'second_daily_reminder_time': 'str',
            'third_daily_reminder_time': 'str',
            'start_tracking_date': 'str',
            'stop_tracking_date': 'str',
            'updated_at': 'datetime',
            'variable_name': 'str',
            'variable_category_name': 'str',
            'abbreviated_unit_name': 'str',
            'combination_operation': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'client_id': 'clientId',
            'user_id': 'userId',
            'variable_id': 'variableId',
            'default_value': 'defaultValue',
            'reminder_start_time': 'reminderStartTime',
            'reminder_end_time': 'reminderEndTime',
            'reminder_sound': 'reminderSound',
            'reminder_frequency': 'reminderFrequency',
            'pop_up': 'popUp',
            'sms': 'sms',
            'email': 'email',
            'notification_bar': 'notificationBar',
            'last_reminded': 'lastReminded',
            'last_tracked': 'lastTracked',
            'first_daily_reminder_time': 'firstDailyReminderTime',
            'second_daily_reminder_time': 'secondDailyReminderTime',
            'third_daily_reminder_time': 'thirdDailyReminderTime',
            'start_tracking_date': 'startTrackingDate',
            'stop_tracking_date': 'stopTrackingDate',
            'updated_at': 'updatedAt',
            'variable_name': 'variableName',
            'variable_category_name': 'variableCategoryName',
            'abbreviated_unit_name': 'abbreviatedUnitName',
            'combination_operation': 'combinationOperation'
        }

        self._id = id
        self._client_id = client_id
        self._user_id = user_id
        self._variable_id = variable_id
        self._default_value = default_value
        self._reminder_start_time = reminder_start_time
        self._reminder_end_time = reminder_end_time
        self._reminder_sound = reminder_sound
        self._reminder_frequency = reminder_frequency
        self._pop_up = pop_up
        self._sms = sms
        self._email = email
        self._notification_bar = notification_bar
        self._last_reminded = last_reminded
        self._last_tracked = last_tracked
        self._first_daily_reminder_time = first_daily_reminder_time
        self._second_daily_reminder_time = second_daily_reminder_time
        self._third_daily_reminder_time = third_daily_reminder_time
        self._start_tracking_date = start_tracking_date
        self._stop_tracking_date = stop_tracking_date
        self._updated_at = updated_at
        self._variable_name = variable_name
        self._variable_category_name = variable_category_name
        self._abbreviated_unit_name = abbreviated_unit_name
        self._combination_operation = combination_operation

    @property
    def id(self):
        """
        Gets the id of this TrackingReminder.
        id

        :return: The id of this TrackingReminder.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TrackingReminder.
        id

        :param id: The id of this TrackingReminder.
        :type: int
        """

        self._id = id

    @property
    def client_id(self):
        """
        Gets the client_id of this TrackingReminder.
        clientId

        :return: The client_id of this TrackingReminder.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this TrackingReminder.
        clientId

        :param client_id: The client_id of this TrackingReminder.
        :type: str
        """

        self._client_id = client_id

    @property
    def user_id(self):
        """
        Gets the user_id of this TrackingReminder.
        ID of User

        :return: The user_id of this TrackingReminder.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this TrackingReminder.
        ID of User

        :param user_id: The user_id of this TrackingReminder.
        :type: int
        """

        self._user_id = user_id

    @property
    def variable_id(self):
        """
        Gets the variable_id of this TrackingReminder.
        Id for the variable to be tracked

        :return: The variable_id of this TrackingReminder.
        :rtype: int
        """
        return self._variable_id

    @variable_id.setter
    def variable_id(self, variable_id):
        """
        Sets the variable_id of this TrackingReminder.
        Id for the variable to be tracked

        :param variable_id: The variable_id of this TrackingReminder.
        :type: int
        """

        self._variable_id = variable_id

    @property
    def default_value(self):
        """
        Gets the default_value of this TrackingReminder.
        Default value to use for the measurement when tracking

        :return: The default_value of this TrackingReminder.
        :rtype: float
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """
        Sets the default_value of this TrackingReminder.
        Default value to use for the measurement when tracking

        :param default_value: The default_value of this TrackingReminder.
        :type: float
        """

        self._default_value = default_value

    @property
    def reminder_start_time(self):
        """
        Gets the reminder_start_time of this TrackingReminder.
        Earliest time of day at which reminders should appear in UTC HH:MM:SS format

        :return: The reminder_start_time of this TrackingReminder.
        :rtype: str
        """
        return self._reminder_start_time

    @reminder_start_time.setter
    def reminder_start_time(self, reminder_start_time):
        """
        Sets the reminder_start_time of this TrackingReminder.
        Earliest time of day at which reminders should appear in UTC HH:MM:SS format

        :param reminder_start_time: The reminder_start_time of this TrackingReminder.
        :type: str
        """

        self._reminder_start_time = reminder_start_time

    @property
    def reminder_end_time(self):
        """
        Gets the reminder_end_time of this TrackingReminder.
        Latest time of day at which reminders should appear in UTC HH:MM:SS format

        :return: The reminder_end_time of this TrackingReminder.
        :rtype: str
        """
        return self._reminder_end_time

    @reminder_end_time.setter
    def reminder_end_time(self, reminder_end_time):
        """
        Sets the reminder_end_time of this TrackingReminder.
        Latest time of day at which reminders should appear in UTC HH:MM:SS format

        :param reminder_end_time: The reminder_end_time of this TrackingReminder.
        :type: str
        """

        self._reminder_end_time = reminder_end_time

    @property
    def reminder_sound(self):
        """
        Gets the reminder_sound of this TrackingReminder.
        String identifier for the sound to accompany the reminder

        :return: The reminder_sound of this TrackingReminder.
        :rtype: str
        """
        return self._reminder_sound

    @reminder_sound.setter
    def reminder_sound(self, reminder_sound):
        """
        Sets the reminder_sound of this TrackingReminder.
        String identifier for the sound to accompany the reminder

        :param reminder_sound: The reminder_sound of this TrackingReminder.
        :type: str
        """

        self._reminder_sound = reminder_sound

    @property
    def reminder_frequency(self):
        """
        Gets the reminder_frequency of this TrackingReminder.
        Number of seconds between one reminder and the next

        :return: The reminder_frequency of this TrackingReminder.
        :rtype: int
        """
        return self._reminder_frequency

    @reminder_frequency.setter
    def reminder_frequency(self, reminder_frequency):
        """
        Sets the reminder_frequency of this TrackingReminder.
        Number of seconds between one reminder and the next

        :param reminder_frequency: The reminder_frequency of this TrackingReminder.
        :type: int
        """

        self._reminder_frequency = reminder_frequency

    @property
    def pop_up(self):
        """
        Gets the pop_up of this TrackingReminder.
        True if the reminders should appear as a popup notification

        :return: The pop_up of this TrackingReminder.
        :rtype: bool
        """
        return self._pop_up

    @pop_up.setter
    def pop_up(self, pop_up):
        """
        Sets the pop_up of this TrackingReminder.
        True if the reminders should appear as a popup notification

        :param pop_up: The pop_up of this TrackingReminder.
        :type: bool
        """

        self._pop_up = pop_up

    @property
    def sms(self):
        """
        Gets the sms of this TrackingReminder.
        True if the reminders should be delivered via SMS

        :return: The sms of this TrackingReminder.
        :rtype: bool
        """
        return self._sms

    @sms.setter
    def sms(self, sms):
        """
        Sets the sms of this TrackingReminder.
        True if the reminders should be delivered via SMS

        :param sms: The sms of this TrackingReminder.
        :type: bool
        """

        self._sms = sms

    @property
    def email(self):
        """
        Gets the email of this TrackingReminder.
        True if the reminders should be delivered via email

        :return: The email of this TrackingReminder.
        :rtype: bool
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this TrackingReminder.
        True if the reminders should be delivered via email

        :param email: The email of this TrackingReminder.
        :type: bool
        """

        self._email = email

    @property
    def notification_bar(self):
        """
        Gets the notification_bar of this TrackingReminder.
        True if the reminders should appear in the notification bar

        :return: The notification_bar of this TrackingReminder.
        :rtype: bool
        """
        return self._notification_bar

    @notification_bar.setter
    def notification_bar(self, notification_bar):
        """
        Sets the notification_bar of this TrackingReminder.
        True if the reminders should appear in the notification bar

        :param notification_bar: The notification_bar of this TrackingReminder.
        :type: bool
        """

        self._notification_bar = notification_bar

    @property
    def last_reminded(self):
        """
        Gets the last_reminded of this TrackingReminder.
        ISO 8601 timestamp for the last time a reminder was sent

        :return: The last_reminded of this TrackingReminder.
        :rtype: datetime
        """
        return self._last_reminded

    @last_reminded.setter
    def last_reminded(self, last_reminded):
        """
        Sets the last_reminded of this TrackingReminder.
        ISO 8601 timestamp for the last time a reminder was sent

        :param last_reminded: The last_reminded of this TrackingReminder.
        :type: datetime
        """

        self._last_reminded = last_reminded

    @property
    def last_tracked(self):
        """
        Gets the last_tracked of this TrackingReminder.
        ISO 8601 timestamp for the last time a measurement was received for this user and variable

        :return: The last_tracked of this TrackingReminder.
        :rtype: datetime
        """
        return self._last_tracked

    @last_tracked.setter
    def last_tracked(self, last_tracked):
        """
        Sets the last_tracked of this TrackingReminder.
        ISO 8601 timestamp for the last time a measurement was received for this user and variable

        :param last_tracked: The last_tracked of this TrackingReminder.
        :type: datetime
        """

        self._last_tracked = last_tracked

    @property
    def first_daily_reminder_time(self):
        """
        Gets the first_daily_reminder_time of this TrackingReminder.
        Specific first time of day that the user should be reminded to track in UTC HH:MM:SS format

        :return: The first_daily_reminder_time of this TrackingReminder.
        :rtype: str
        """
        return self._first_daily_reminder_time

    @first_daily_reminder_time.setter
    def first_daily_reminder_time(self, first_daily_reminder_time):
        """
        Sets the first_daily_reminder_time of this TrackingReminder.
        Specific first time of day that the user should be reminded to track in UTC HH:MM:SS format

        :param first_daily_reminder_time: The first_daily_reminder_time of this TrackingReminder.
        :type: str
        """

        self._first_daily_reminder_time = first_daily_reminder_time

    @property
    def second_daily_reminder_time(self):
        """
        Gets the second_daily_reminder_time of this TrackingReminder.
        Specific second time of day that the user should be reminded to track in UTC HH:MM:SS format

        :return: The second_daily_reminder_time of this TrackingReminder.
        :rtype: str
        """
        return self._second_daily_reminder_time

    @second_daily_reminder_time.setter
    def second_daily_reminder_time(self, second_daily_reminder_time):
        """
        Sets the second_daily_reminder_time of this TrackingReminder.
        Specific second time of day that the user should be reminded to track in UTC HH:MM:SS format

        :param second_daily_reminder_time: The second_daily_reminder_time of this TrackingReminder.
        :type: str
        """

        self._second_daily_reminder_time = second_daily_reminder_time

    @property
    def third_daily_reminder_time(self):
        """
        Gets the third_daily_reminder_time of this TrackingReminder.
        Specific third time of day that the user should be reminded to track in UTC HH:MM:SS format

        :return: The third_daily_reminder_time of this TrackingReminder.
        :rtype: str
        """
        return self._third_daily_reminder_time

    @third_daily_reminder_time.setter
    def third_daily_reminder_time(self, third_daily_reminder_time):
        """
        Sets the third_daily_reminder_time of this TrackingReminder.
        Specific third time of day that the user should be reminded to track in UTC HH:MM:SS format

        :param third_daily_reminder_time: The third_daily_reminder_time of this TrackingReminder.
        :type: str
        """

        self._third_daily_reminder_time = third_daily_reminder_time

    @property
    def start_tracking_date(self):
        """
        Gets the start_tracking_date of this TrackingReminder.
        Earliest date on which the user should be reminded to track in YYYY-MM-DD format

        :return: The start_tracking_date of this TrackingReminder.
        :rtype: str
        """
        return self._start_tracking_date

    @start_tracking_date.setter
    def start_tracking_date(self, start_tracking_date):
        """
        Sets the start_tracking_date of this TrackingReminder.
        Earliest date on which the user should be reminded to track in YYYY-MM-DD format

        :param start_tracking_date: The start_tracking_date of this TrackingReminder.
        :type: str
        """

        self._start_tracking_date = start_tracking_date

    @property
    def stop_tracking_date(self):
        """
        Gets the stop_tracking_date of this TrackingReminder.
        Latest date on which the user should be reminded to track in YYYY-MM-DD format

        :return: The stop_tracking_date of this TrackingReminder.
        :rtype: str
        """
        return self._stop_tracking_date

    @stop_tracking_date.setter
    def stop_tracking_date(self, stop_tracking_date):
        """
        Sets the stop_tracking_date of this TrackingReminder.
        Latest date on which the user should be reminded to track in YYYY-MM-DD format

        :param stop_tracking_date: The stop_tracking_date of this TrackingReminder.
        :type: str
        """

        self._stop_tracking_date = stop_tracking_date

    @property
    def updated_at(self):
        """
        Gets the updated_at of this TrackingReminder.
        When the record in the database was last updated. Use ISO 8601 datetime format. Time zone should be UTC and not local.

        :return: The updated_at of this TrackingReminder.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this TrackingReminder.
        When the record in the database was last updated. Use ISO 8601 datetime format. Time zone should be UTC and not local.

        :param updated_at: The updated_at of this TrackingReminder.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def variable_name(self):
        """
        Gets the variable_name of this TrackingReminder.
        Name of the variable to be used when sending measurements

        :return: The variable_name of this TrackingReminder.
        :rtype: str
        """
        return self._variable_name

    @variable_name.setter
    def variable_name(self, variable_name):
        """
        Sets the variable_name of this TrackingReminder.
        Name of the variable to be used when sending measurements

        :param variable_name: The variable_name of this TrackingReminder.
        :type: str
        """

        self._variable_name = variable_name

    @property
    def variable_category_name(self):
        """
        Gets the variable_category_name of this TrackingReminder.
        Name of the variable category to be used when sending measurements

        :return: The variable_category_name of this TrackingReminder.
        :rtype: str
        """
        return self._variable_category_name

    @variable_category_name.setter
    def variable_category_name(self, variable_category_name):
        """
        Sets the variable_category_name of this TrackingReminder.
        Name of the variable category to be used when sending measurements

        :param variable_category_name: The variable_category_name of this TrackingReminder.
        :type: str
        """

        self._variable_category_name = variable_category_name

    @property
    def abbreviated_unit_name(self):
        """
        Gets the abbreviated_unit_name of this TrackingReminder.
        Abbreviated name of the unit to be used when sending measurements

        :return: The abbreviated_unit_name of this TrackingReminder.
        :rtype: str
        """
        return self._abbreviated_unit_name

    @abbreviated_unit_name.setter
    def abbreviated_unit_name(self, abbreviated_unit_name):
        """
        Sets the abbreviated_unit_name of this TrackingReminder.
        Abbreviated name of the unit to be used when sending measurements

        :param abbreviated_unit_name: The abbreviated_unit_name of this TrackingReminder.
        :type: str
        """

        self._abbreviated_unit_name = abbreviated_unit_name

    @property
    def combination_operation(self):
        """
        Gets the combination_operation of this TrackingReminder.
        The way multiple measurements are aggregated over time

        :return: The combination_operation of this TrackingReminder.
        :rtype: str
        """
        return self._combination_operation

    @combination_operation.setter
    def combination_operation(self, combination_operation):
        """
        Sets the combination_operation of this TrackingReminder.
        The way multiple measurements are aggregated over time

        :param combination_operation: The combination_operation of this TrackingReminder.
        :type: str
        """
        allowed_values = ["MEAN", "SUM"]
        if combination_operation not in allowed_values:
            raise ValueError(
                "Invalid value for `combination_operation`, must be one of {0}"
                .format(allowed_values)
            )

        self._combination_operation = combination_operation

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
