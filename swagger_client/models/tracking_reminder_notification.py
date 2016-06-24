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


class TrackingReminderNotification(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, tracking_reminder_id=None, client_id=None, user_id=None, variable_id=None, pending_reminder_time=None, default_value=None, reminder_sound=None, pop_up=None, sms=None, email=None, notification_bar=None, updated_at=None, variable_name=None, variable_category_name=None, abbreviated_unit_name=None, combination_operation=None):
        """
        TrackingReminderNotification - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'tracking_reminder_id': 'int',
            'client_id': 'str',
            'user_id': 'int',
            'variable_id': 'int',
            'pending_reminder_time': 'datetime',
            'default_value': 'float',
            'reminder_sound': 'str',
            'pop_up': 'bool',
            'sms': 'bool',
            'email': 'bool',
            'notification_bar': 'bool',
            'updated_at': 'datetime',
            'variable_name': 'str',
            'variable_category_name': 'str',
            'abbreviated_unit_name': 'str',
            'combination_operation': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'tracking_reminder_id': 'trackingReminderId',
            'client_id': 'clientId',
            'user_id': 'userId',
            'variable_id': 'variableId',
            'pending_reminder_time': 'pendingReminderTime',
            'default_value': 'defaultValue',
            'reminder_sound': 'reminderSound',
            'pop_up': 'popUp',
            'sms': 'sms',
            'email': 'email',
            'notification_bar': 'notificationBar',
            'updated_at': 'updatedAt',
            'variable_name': 'variableName',
            'variable_category_name': 'variableCategoryName',
            'abbreviated_unit_name': 'abbreviatedUnitName',
            'combination_operation': 'combinationOperation'
        }

        self._id = id
        self._tracking_reminder_id = tracking_reminder_id
        self._client_id = client_id
        self._user_id = user_id
        self._variable_id = variable_id
        self._pending_reminder_time = pending_reminder_time
        self._default_value = default_value
        self._reminder_sound = reminder_sound
        self._pop_up = pop_up
        self._sms = sms
        self._email = email
        self._notification_bar = notification_bar
        self._updated_at = updated_at
        self._variable_name = variable_name
        self._variable_category_name = variable_category_name
        self._abbreviated_unit_name = abbreviated_unit_name
        self._combination_operation = combination_operation

    @property
    def id(self):
        """
        Gets the id of this TrackingReminderNotification.
        id for the specific PENDING tracking remidner

        :return: The id of this TrackingReminderNotification.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TrackingReminderNotification.
        id for the specific PENDING tracking remidner

        :param id: The id of this TrackingReminderNotification.
        :type: int
        """

        self._id = id

    @property
    def tracking_reminder_id(self):
        """
        Gets the tracking_reminder_id of this TrackingReminderNotification.
        id for the repeating tracking remidner

        :return: The tracking_reminder_id of this TrackingReminderNotification.
        :rtype: int
        """
        return self._tracking_reminder_id

    @tracking_reminder_id.setter
    def tracking_reminder_id(self, tracking_reminder_id):
        """
        Sets the tracking_reminder_id of this TrackingReminderNotification.
        id for the repeating tracking remidner

        :param tracking_reminder_id: The tracking_reminder_id of this TrackingReminderNotification.
        :type: int
        """

        self._tracking_reminder_id = tracking_reminder_id

    @property
    def client_id(self):
        """
        Gets the client_id of this TrackingReminderNotification.
        clientId

        :return: The client_id of this TrackingReminderNotification.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this TrackingReminderNotification.
        clientId

        :param client_id: The client_id of this TrackingReminderNotification.
        :type: str
        """

        self._client_id = client_id

    @property
    def user_id(self):
        """
        Gets the user_id of this TrackingReminderNotification.
        ID of User

        :return: The user_id of this TrackingReminderNotification.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this TrackingReminderNotification.
        ID of User

        :param user_id: The user_id of this TrackingReminderNotification.
        :type: int
        """

        self._user_id = user_id

    @property
    def variable_id(self):
        """
        Gets the variable_id of this TrackingReminderNotification.
        Id for the variable to be tracked

        :return: The variable_id of this TrackingReminderNotification.
        :rtype: int
        """
        return self._variable_id

    @variable_id.setter
    def variable_id(self, variable_id):
        """
        Sets the variable_id of this TrackingReminderNotification.
        Id for the variable to be tracked

        :param variable_id: The variable_id of this TrackingReminderNotification.
        :type: int
        """

        self._variable_id = variable_id

    @property
    def pending_reminder_time(self):
        """
        Gets the pending_reminder_time of this TrackingReminderNotification.
        ISO 8601 timestamp for the specific time the variable should be tracked in UTC.  This will be used for the measurement startTime if the track endpoint is used.

        :return: The pending_reminder_time of this TrackingReminderNotification.
        :rtype: datetime
        """
        return self._pending_reminder_time

    @pending_reminder_time.setter
    def pending_reminder_time(self, pending_reminder_time):
        """
        Sets the pending_reminder_time of this TrackingReminderNotification.
        ISO 8601 timestamp for the specific time the variable should be tracked in UTC.  This will be used for the measurement startTime if the track endpoint is used.

        :param pending_reminder_time: The pending_reminder_time of this TrackingReminderNotification.
        :type: datetime
        """

        self._pending_reminder_time = pending_reminder_time

    @property
    def default_value(self):
        """
        Gets the default_value of this TrackingReminderNotification.
        Default value to use for the measurement when tracking

        :return: The default_value of this TrackingReminderNotification.
        :rtype: float
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """
        Sets the default_value of this TrackingReminderNotification.
        Default value to use for the measurement when tracking

        :param default_value: The default_value of this TrackingReminderNotification.
        :type: float
        """

        self._default_value = default_value

    @property
    def reminder_sound(self):
        """
        Gets the reminder_sound of this TrackingReminderNotification.
        String identifier for the sound to accompany the reminder

        :return: The reminder_sound of this TrackingReminderNotification.
        :rtype: str
        """
        return self._reminder_sound

    @reminder_sound.setter
    def reminder_sound(self, reminder_sound):
        """
        Sets the reminder_sound of this TrackingReminderNotification.
        String identifier for the sound to accompany the reminder

        :param reminder_sound: The reminder_sound of this TrackingReminderNotification.
        :type: str
        """

        self._reminder_sound = reminder_sound

    @property
    def pop_up(self):
        """
        Gets the pop_up of this TrackingReminderNotification.
        True if the reminders should appear as a popup notification

        :return: The pop_up of this TrackingReminderNotification.
        :rtype: bool
        """
        return self._pop_up

    @pop_up.setter
    def pop_up(self, pop_up):
        """
        Sets the pop_up of this TrackingReminderNotification.
        True if the reminders should appear as a popup notification

        :param pop_up: The pop_up of this TrackingReminderNotification.
        :type: bool
        """

        self._pop_up = pop_up

    @property
    def sms(self):
        """
        Gets the sms of this TrackingReminderNotification.
        True if the reminders should be delivered via SMS

        :return: The sms of this TrackingReminderNotification.
        :rtype: bool
        """
        return self._sms

    @sms.setter
    def sms(self, sms):
        """
        Sets the sms of this TrackingReminderNotification.
        True if the reminders should be delivered via SMS

        :param sms: The sms of this TrackingReminderNotification.
        :type: bool
        """

        self._sms = sms

    @property
    def email(self):
        """
        Gets the email of this TrackingReminderNotification.
        True if the reminders should be delivered via email

        :return: The email of this TrackingReminderNotification.
        :rtype: bool
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this TrackingReminderNotification.
        True if the reminders should be delivered via email

        :param email: The email of this TrackingReminderNotification.
        :type: bool
        """

        self._email = email

    @property
    def notification_bar(self):
        """
        Gets the notification_bar of this TrackingReminderNotification.
        True if the reminders should appear in the notification bar

        :return: The notification_bar of this TrackingReminderNotification.
        :rtype: bool
        """
        return self._notification_bar

    @notification_bar.setter
    def notification_bar(self, notification_bar):
        """
        Sets the notification_bar of this TrackingReminderNotification.
        True if the reminders should appear in the notification bar

        :param notification_bar: The notification_bar of this TrackingReminderNotification.
        :type: bool
        """

        self._notification_bar = notification_bar

    @property
    def updated_at(self):
        """
        Gets the updated_at of this TrackingReminderNotification.
        When the record in the database was last updated. Use ISO 8601 datetime format. Time zone should be UTC and not local.

        :return: The updated_at of this TrackingReminderNotification.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this TrackingReminderNotification.
        When the record in the database was last updated. Use ISO 8601 datetime format. Time zone should be UTC and not local.

        :param updated_at: The updated_at of this TrackingReminderNotification.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def variable_name(self):
        """
        Gets the variable_name of this TrackingReminderNotification.
        Name of the variable to be used when sending measurements

        :return: The variable_name of this TrackingReminderNotification.
        :rtype: str
        """
        return self._variable_name

    @variable_name.setter
    def variable_name(self, variable_name):
        """
        Sets the variable_name of this TrackingReminderNotification.
        Name of the variable to be used when sending measurements

        :param variable_name: The variable_name of this TrackingReminderNotification.
        :type: str
        """

        self._variable_name = variable_name

    @property
    def variable_category_name(self):
        """
        Gets the variable_category_name of this TrackingReminderNotification.
        Name of the variable category to be used when sending measurements

        :return: The variable_category_name of this TrackingReminderNotification.
        :rtype: str
        """
        return self._variable_category_name

    @variable_category_name.setter
    def variable_category_name(self, variable_category_name):
        """
        Sets the variable_category_name of this TrackingReminderNotification.
        Name of the variable category to be used when sending measurements

        :param variable_category_name: The variable_category_name of this TrackingReminderNotification.
        :type: str
        """

        self._variable_category_name = variable_category_name

    @property
    def abbreviated_unit_name(self):
        """
        Gets the abbreviated_unit_name of this TrackingReminderNotification.
        Abbreviated name of the unit to be used when sending measurements

        :return: The abbreviated_unit_name of this TrackingReminderNotification.
        :rtype: str
        """
        return self._abbreviated_unit_name

    @abbreviated_unit_name.setter
    def abbreviated_unit_name(self, abbreviated_unit_name):
        """
        Sets the abbreviated_unit_name of this TrackingReminderNotification.
        Abbreviated name of the unit to be used when sending measurements

        :param abbreviated_unit_name: The abbreviated_unit_name of this TrackingReminderNotification.
        :type: str
        """

        self._abbreviated_unit_name = abbreviated_unit_name

    @property
    def combination_operation(self):
        """
        Gets the combination_operation of this TrackingReminderNotification.
        The way multiple measurements are aggregated over time

        :return: The combination_operation of this TrackingReminderNotification.
        :rtype: str
        """
        return self._combination_operation

    @combination_operation.setter
    def combination_operation(self, combination_operation):
        """
        Sets the combination_operation of this TrackingReminderNotification.
        The way multiple measurements are aggregated over time

        :param combination_operation: The combination_operation of this TrackingReminderNotification.
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
