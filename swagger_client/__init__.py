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

from __future__ import absolute_import

# import models into sdk package
from .models.common_response import CommonResponse
from .models.connection import Connection
from .models.connector import Connector
from .models.connector_info import ConnectorInfo
from .models.connector_info_history_item import ConnectorInfoHistoryItem
from .models.connector_instruction import ConnectorInstruction
from .models.conversion_step import ConversionStep
from .models.correlation import Correlation
from .models.credential import Credential
from .models.human_time import HumanTime
from .models.inline_response_200 import InlineResponse200
from .models.inline_response_200_1 import InlineResponse2001
from .models.inline_response_200_10 import InlineResponse20010
from .models.inline_response_200_11 import InlineResponse20011
from .models.inline_response_200_12 import InlineResponse20012
from .models.inline_response_200_2 import InlineResponse2002
from .models.inline_response_200_3 import InlineResponse2003
from .models.inline_response_200_4 import InlineResponse2004
from .models.inline_response_200_5 import InlineResponse2005
from .models.inline_response_200_6 import InlineResponse2006
from .models.inline_response_200_7 import InlineResponse2007
from .models.inline_response_200_8 import InlineResponse2008
from .models.inline_response_200_9 import InlineResponse2009
from .models.json_error_response import JsonErrorResponse
from .models.measurement import Measurement
from .models.measurement_delete import MeasurementDelete
from .models.measurement_range import MeasurementRange
from .models.measurement_set import MeasurementSet
from .models.measurement_source import MeasurementSource
from .models.pairs import Pairs
from .models.permission import Permission
from .models.post_correlation import PostCorrelation
from .models.post_vote import PostVote
from .models.tracking_reminder import TrackingReminder
from .models.tracking_reminder_delete import TrackingReminderDelete
from .models.tracking_reminder_notification import TrackingReminderNotification
from .models.tracking_reminder_notification_skip import TrackingReminderNotificationSkip
from .models.tracking_reminder_notification_snooze import TrackingReminderNotificationSnooze
from .models.tracking_reminder_notification_track import TrackingReminderNotificationTrack
from .models.unit import Unit
from .models.unit_category import UnitCategory
from .models.update import Update
from .models.user import User
from .models.user_tag import UserTag
from .models.user_token_failed_response import UserTokenFailedResponse
from .models.user_token_request import UserTokenRequest
from .models.user_token_request_inner_user_field import UserTokenRequestInnerUserField
from .models.user_token_successful_response import UserTokenSuccessfulResponse
from .models.user_token_successful_response_inner_user_field import UserTokenSuccessfulResponseInnerUserField
from .models.user_variable import UserVariable
from .models.user_variable_relationship import UserVariableRelationship
from .models.user_variables import UserVariables
from .models.value_object import ValueObject
from .models.variable import Variable
from .models.variable_category import VariableCategory
from .models.variable_new import VariableNew
from .models.variable_user_source import VariableUserSource
from .models.variables_new import VariablesNew
from .models.vote import Vote
from .models.vote_delete import VoteDelete

# import apis into sdk package
from .apis.application_endpoints_api import ApplicationEndpointsApi
from .apis.authentication_api import AuthenticationApi
from .apis.connectors_api import ConnectorsApi
from .apis.correlations_api import CorrelationsApi
from .apis.measurements_api import MeasurementsApi
from .apis.organizations_api import OrganizationsApi
from .apis.pairs_api import PairsApi
from .apis.reminders_api import RemindersApi
from .apis.tags_api import TagsApi
from .apis.units_api import UnitsApi
from .apis.user_api import UserApi
from .apis.variables_api import VariablesApi
from .apis.votes_api import VotesApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
