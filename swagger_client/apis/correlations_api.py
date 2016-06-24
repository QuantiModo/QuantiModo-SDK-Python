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

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class CorrelationsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def v1_aggregated_correlations_get(self, **kwargs):
        """
        Get aggregated correlations
        Get correlations based on the anonymized aggregate data from all QuantiModo users.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_aggregated_correlations_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: User's OAuth2 access token
        :param str effect: ORIGINAL variable name of the effect variable for which the user desires correlations
        :param str cause: ORIGINAL variable name of the cause variable for which the user desires correlations
        :param str correlation_coefficient: Pearson correlation coefficient between cause and effect after lagging by onset delay and grouping by duration of action
        :param str onset_delay: The number of seconds which pass following a cause measurement before an effect would likely be observed.
        :param str duration_of_action: The time in seconds over which the cause would be expected to exert a measurable effect. We have selected a default value for each variable. This default value may be replaced by a user specified by adjusting their variable user settings.
        :param str last_updated: The time that this measurement was last updated in the UTC format \"YYYY-MM-DDThh:mm:ss\"
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0.
        :param int offset: Now suppose you wanted to show results 11-20. You'd set the offset to 10 and the limit to 10.
        :param int sort: Sort by given field. If the field is prefixed with `-, it will sort in descending order.
        :return: list[Correlation]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_aggregated_correlations_get_with_http_info(**kwargs)
        else:
            (data) = self.v1_aggregated_correlations_get_with_http_info(**kwargs)
            return data

    def v1_aggregated_correlations_get_with_http_info(self, **kwargs):
        """
        Get aggregated correlations
        Get correlations based on the anonymized aggregate data from all QuantiModo users.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_aggregated_correlations_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: User's OAuth2 access token
        :param str effect: ORIGINAL variable name of the effect variable for which the user desires correlations
        :param str cause: ORIGINAL variable name of the cause variable for which the user desires correlations
        :param str correlation_coefficient: Pearson correlation coefficient between cause and effect after lagging by onset delay and grouping by duration of action
        :param str onset_delay: The number of seconds which pass following a cause measurement before an effect would likely be observed.
        :param str duration_of_action: The time in seconds over which the cause would be expected to exert a measurable effect. We have selected a default value for each variable. This default value may be replaced by a user specified by adjusting their variable user settings.
        :param str last_updated: The time that this measurement was last updated in the UTC format \"YYYY-MM-DDThh:mm:ss\"
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0.
        :param int offset: Now suppose you wanted to show results 11-20. You'd set the offset to 10 and the limit to 10.
        :param int sort: Sort by given field. If the field is prefixed with `-, it will sort in descending order.
        :return: list[Correlation]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token', 'effect', 'cause', 'correlation_coefficient', 'onset_delay', 'duration_of_action', 'last_updated', 'limit', 'offset', 'sort']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_aggregated_correlations_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/aggregatedCorrelations'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']
        if 'effect' in params:
            query_params['effect'] = params['effect']
        if 'cause' in params:
            query_params['cause'] = params['cause']
        if 'correlation_coefficient' in params:
            query_params['correlationCoefficient'] = params['correlation_coefficient']
        if 'onset_delay' in params:
            query_params['onsetDelay'] = params['onset_delay']
        if 'duration_of_action' in params:
            query_params['durationOfAction'] = params['duration_of_action']
        if 'last_updated' in params:
            query_params['lastUpdated'] = params['last_updated']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'sort' in params:
            query_params['sort'] = params['sort']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Correlation]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v1_aggregated_correlations_post(self, body, **kwargs):
        """
        Store or Update a Correlation
        Add correlation

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_aggregated_correlations_post(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param PostCorrelation body: Provides correlation data (required)
        :param str access_token: User's OAuth2 access token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_aggregated_correlations_post_with_http_info(body, **kwargs)
        else:
            (data) = self.v1_aggregated_correlations_post_with_http_info(body, **kwargs)
            return data

    def v1_aggregated_correlations_post_with_http_info(self, body, **kwargs):
        """
        Store or Update a Correlation
        Add correlation

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_aggregated_correlations_post_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param PostCorrelation body: Provides correlation data (required)
        :param str access_token: User's OAuth2 access token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'access_token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_aggregated_correlations_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_aggregated_correlations_post`")

        resource_path = '/v1/aggregatedCorrelations'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v1_correlations_get(self, **kwargs):
        """
        Get correlations
        Get correlations.<br>Supported filter parameters:<br><ul><li><b>correlationCoefficient</b> - Pearson correlation coefficient between cause and effect after lagging by onset delay and grouping by duration of action</li><li><b>onsetDelay</b> - The number of seconds which pass following a cause measurement before an effect would likely be observed.</li><li><b>durationOfAction</b> - The time in seconds over which the cause would be expected to exert a measurable effect. We have selected a default value for each variable. This default value may be replaced by a user specified by adjusting their variable user settings.</li><li><b>lastUpdated</b> - The time that this measurement was last updated in the UTC format \"YYYY-MM-DDThh:mm:ss\"</li></ul><br>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_correlations_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: User's OAuth2 access token
        :param str effect: ORIGINAL variable name of the effect variable for which the user desires correlations
        :param str cause: ORIGINAL variable name of the cause variable for which the user desires correlations
        :param str correlation_coefficient: Pearson correlation coefficient between cause and effect after lagging by onset delay and grouping by duration of action
        :param str onset_delay: The number of seconds which pass following a cause measurement before an effect would likely be observed.
        :param str duration_of_action: The time in seconds over which the cause would be expected to exert a measurable effect. We have selected a default value for each variable. This default value may be replaced by a user specified by adjusting their variable user settings.
        :param str last_updated: The time that this measurement was last updated in the UTC format \"YYYY-MM-DDThh:mm:ss\"
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0.
        :param int offset: Now suppose you wanted to show results 11-20. You'd set the offset to 10 and the limit to 10.
        :param int sort: Sort by given field. If the field is prefixed with `-, it will sort in descending order.
        :return: list[Correlation]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_correlations_get_with_http_info(**kwargs)
        else:
            (data) = self.v1_correlations_get_with_http_info(**kwargs)
            return data

    def v1_correlations_get_with_http_info(self, **kwargs):
        """
        Get correlations
        Get correlations.<br>Supported filter parameters:<br><ul><li><b>correlationCoefficient</b> - Pearson correlation coefficient between cause and effect after lagging by onset delay and grouping by duration of action</li><li><b>onsetDelay</b> - The number of seconds which pass following a cause measurement before an effect would likely be observed.</li><li><b>durationOfAction</b> - The time in seconds over which the cause would be expected to exert a measurable effect. We have selected a default value for each variable. This default value may be replaced by a user specified by adjusting their variable user settings.</li><li><b>lastUpdated</b> - The time that this measurement was last updated in the UTC format \"YYYY-MM-DDThh:mm:ss\"</li></ul><br>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_correlations_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: User's OAuth2 access token
        :param str effect: ORIGINAL variable name of the effect variable for which the user desires correlations
        :param str cause: ORIGINAL variable name of the cause variable for which the user desires correlations
        :param str correlation_coefficient: Pearson correlation coefficient between cause and effect after lagging by onset delay and grouping by duration of action
        :param str onset_delay: The number of seconds which pass following a cause measurement before an effect would likely be observed.
        :param str duration_of_action: The time in seconds over which the cause would be expected to exert a measurable effect. We have selected a default value for each variable. This default value may be replaced by a user specified by adjusting their variable user settings.
        :param str last_updated: The time that this measurement was last updated in the UTC format \"YYYY-MM-DDThh:mm:ss\"
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0.
        :param int offset: Now suppose you wanted to show results 11-20. You'd set the offset to 10 and the limit to 10.
        :param int sort: Sort by given field. If the field is prefixed with `-, it will sort in descending order.
        :return: list[Correlation]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token', 'effect', 'cause', 'correlation_coefficient', 'onset_delay', 'duration_of_action', 'last_updated', 'limit', 'offset', 'sort']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_correlations_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/correlations'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']
        if 'effect' in params:
            query_params['effect'] = params['effect']
        if 'cause' in params:
            query_params['cause'] = params['cause']
        if 'correlation_coefficient' in params:
            query_params['correlationCoefficient'] = params['correlation_coefficient']
        if 'onset_delay' in params:
            query_params['onsetDelay'] = params['onset_delay']
        if 'duration_of_action' in params:
            query_params['durationOfAction'] = params['duration_of_action']
        if 'last_updated' in params:
            query_params['lastUpdated'] = params['last_updated']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'sort' in params:
            query_params['sort'] = params['sort']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Correlation]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v1_organizations_organization_id_users_user_id_variables_variable_name_causes_get(self, organization_id, user_id, variable_name, organization_token, **kwargs):
        """
        Search user correlations for a given cause
        Returns average of all correlations and votes for all user cause variables for a given cause. If parameter \"include_public\" is used, it also returns public correlations. User correlation overwrites or supersedes public correlation.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_organizations_organization_id_users_user_id_variables_variable_name_causes_get(organization_id, user_id, variable_name, organization_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int organization_id: Organization ID (required)
        :param int user_id: User id (required)
        :param str variable_name: Effect variable name (required)
        :param str organization_token: Organization access token (required)
        :param str access_token: User's OAuth2 access token
        :param str include_public: Include public correlations, Can be \"1\" or empty.
        :return: list[Correlation]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_organizations_organization_id_users_user_id_variables_variable_name_causes_get_with_http_info(organization_id, user_id, variable_name, organization_token, **kwargs)
        else:
            (data) = self.v1_organizations_organization_id_users_user_id_variables_variable_name_causes_get_with_http_info(organization_id, user_id, variable_name, organization_token, **kwargs)
            return data

    def v1_organizations_organization_id_users_user_id_variables_variable_name_causes_get_with_http_info(self, organization_id, user_id, variable_name, organization_token, **kwargs):
        """
        Search user correlations for a given cause
        Returns average of all correlations and votes for all user cause variables for a given cause. If parameter \"include_public\" is used, it also returns public correlations. User correlation overwrites or supersedes public correlation.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_organizations_organization_id_users_user_id_variables_variable_name_causes_get_with_http_info(organization_id, user_id, variable_name, organization_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int organization_id: Organization ID (required)
        :param int user_id: User id (required)
        :param str variable_name: Effect variable name (required)
        :param str organization_token: Organization access token (required)
        :param str access_token: User's OAuth2 access token
        :param str include_public: Include public correlations, Can be \"1\" or empty.
        :return: list[Correlation]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organization_id', 'user_id', 'variable_name', 'organization_token', 'access_token', 'include_public']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_organizations_organization_id_users_user_id_variables_variable_name_causes_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organization_id' is set
        if ('organization_id' not in params) or (params['organization_id'] is None):
            raise ValueError("Missing the required parameter `organization_id` when calling `v1_organizations_organization_id_users_user_id_variables_variable_name_causes_get`")
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `v1_organizations_organization_id_users_user_id_variables_variable_name_causes_get`")
        # verify the required parameter 'variable_name' is set
        if ('variable_name' not in params) or (params['variable_name'] is None):
            raise ValueError("Missing the required parameter `variable_name` when calling `v1_organizations_organization_id_users_user_id_variables_variable_name_causes_get`")
        # verify the required parameter 'organization_token' is set
        if ('organization_token' not in params) or (params['organization_token'] is None):
            raise ValueError("Missing the required parameter `organization_token` when calling `v1_organizations_organization_id_users_user_id_variables_variable_name_causes_get`")

        resource_path = '/v1/organizations/{organizationId}/users/{userId}/variables/{variableName}/causes'.replace('{format}', 'json')
        path_params = {}
        if 'organization_id' in params:
            path_params['organizationId'] = params['organization_id']
        if 'user_id' in params:
            path_params['userId'] = params['user_id']
        if 'variable_name' in params:
            path_params['variableName'] = params['variable_name']

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']
        if 'organization_token' in params:
            query_params['organization_token'] = params['organization_token']
        if 'include_public' in params:
            query_params['includePublic'] = params['include_public']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Correlation]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v1_organizations_organization_id_users_user_id_variables_variable_name_effects_get(self, organization_id, user_id, variable_name, organization_token, **kwargs):
        """
        Search user correlations for a given cause
        Returns average of all correlations and votes for all user cause variables for a given effect. If parameter \"include_public\" is used, it also returns public correlations. User correlation overwrites or supersedes public correlation.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_organizations_organization_id_users_user_id_variables_variable_name_effects_get(organization_id, user_id, variable_name, organization_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int organization_id: Organization ID (required)
        :param int user_id: User id (required)
        :param str variable_name: Cause variable name (required)
        :param str organization_token: Organization access token (required)
        :param str access_token: User's OAuth2 access token
        :param str include_public: Include public correlations, Can be \"1\" or empty.
        :return: list[CommonResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_organizations_organization_id_users_user_id_variables_variable_name_effects_get_with_http_info(organization_id, user_id, variable_name, organization_token, **kwargs)
        else:
            (data) = self.v1_organizations_organization_id_users_user_id_variables_variable_name_effects_get_with_http_info(organization_id, user_id, variable_name, organization_token, **kwargs)
            return data

    def v1_organizations_organization_id_users_user_id_variables_variable_name_effects_get_with_http_info(self, organization_id, user_id, variable_name, organization_token, **kwargs):
        """
        Search user correlations for a given cause
        Returns average of all correlations and votes for all user cause variables for a given effect. If parameter \"include_public\" is used, it also returns public correlations. User correlation overwrites or supersedes public correlation.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_organizations_organization_id_users_user_id_variables_variable_name_effects_get_with_http_info(organization_id, user_id, variable_name, organization_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int organization_id: Organization ID (required)
        :param int user_id: User id (required)
        :param str variable_name: Cause variable name (required)
        :param str organization_token: Organization access token (required)
        :param str access_token: User's OAuth2 access token
        :param str include_public: Include public correlations, Can be \"1\" or empty.
        :return: list[CommonResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organization_id', 'user_id', 'variable_name', 'organization_token', 'access_token', 'include_public']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_organizations_organization_id_users_user_id_variables_variable_name_effects_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organization_id' is set
        if ('organization_id' not in params) or (params['organization_id'] is None):
            raise ValueError("Missing the required parameter `organization_id` when calling `v1_organizations_organization_id_users_user_id_variables_variable_name_effects_get`")
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `v1_organizations_organization_id_users_user_id_variables_variable_name_effects_get`")
        # verify the required parameter 'variable_name' is set
        if ('variable_name' not in params) or (params['variable_name'] is None):
            raise ValueError("Missing the required parameter `variable_name` when calling `v1_organizations_organization_id_users_user_id_variables_variable_name_effects_get`")
        # verify the required parameter 'organization_token' is set
        if ('organization_token' not in params) or (params['organization_token'] is None):
            raise ValueError("Missing the required parameter `organization_token` when calling `v1_organizations_organization_id_users_user_id_variables_variable_name_effects_get`")

        resource_path = '/v1/organizations/{organizationId}/users/{userId}/variables/{variableName}/effects'.replace('{format}', 'json')
        path_params = {}
        if 'organization_id' in params:
            path_params['organizationId'] = params['organization_id']
        if 'user_id' in params:
            path_params['userId'] = params['user_id']
        if 'variable_name' in params:
            path_params['variableName'] = params['variable_name']

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']
        if 'organization_token' in params:
            query_params['organization_token'] = params['organization_token']
        if 'include_public' in params:
            query_params['include_public'] = params['include_public']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[CommonResponse]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v1_public_correlations_search_search_get(self, search, effect_or_cause, **kwargs):
        """
        Get average correlations for variables containing search term
        Returns the average correlations from all users for all public variables that contain the characters in the search query. Returns average of all users public variable correlations with a specified cause or effect.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_public_correlations_search_search_get(search, effect_or_cause, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str search: Name of the variable that you want to know the causes or effects of. (required)
        :param str effect_or_cause: Setting this to effect indicates that the searched variable is the effect and that the causes of this variable should be returned.  cause indicates that the searched variable is the cause and the effects should be returned. (required)
        :param str access_token: User's OAuth2 access token
        :return: list[Correlation]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_public_correlations_search_search_get_with_http_info(search, effect_or_cause, **kwargs)
        else:
            (data) = self.v1_public_correlations_search_search_get_with_http_info(search, effect_or_cause, **kwargs)
            return data

    def v1_public_correlations_search_search_get_with_http_info(self, search, effect_or_cause, **kwargs):
        """
        Get average correlations for variables containing search term
        Returns the average correlations from all users for all public variables that contain the characters in the search query. Returns average of all users public variable correlations with a specified cause or effect.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_public_correlations_search_search_get_with_http_info(search, effect_or_cause, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str search: Name of the variable that you want to know the causes or effects of. (required)
        :param str effect_or_cause: Setting this to effect indicates that the searched variable is the effect and that the causes of this variable should be returned.  cause indicates that the searched variable is the cause and the effects should be returned. (required)
        :param str access_token: User's OAuth2 access token
        :return: list[Correlation]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search', 'effect_or_cause', 'access_token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_public_correlations_search_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search' is set
        if ('search' not in params) or (params['search'] is None):
            raise ValueError("Missing the required parameter `search` when calling `v1_public_correlations_search_search_get`")
        # verify the required parameter 'effect_or_cause' is set
        if ('effect_or_cause' not in params) or (params['effect_or_cause'] is None):
            raise ValueError("Missing the required parameter `effect_or_cause` when calling `v1_public_correlations_search_search_get`")

        resource_path = '/v1/public/correlations/search/{search}'.replace('{format}', 'json')
        path_params = {}
        if 'search' in params:
            path_params['search'] = params['search']

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']
        if 'effect_or_cause' in params:
            query_params['effectOrCause'] = params['effect_or_cause']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Correlation]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v1_variables_variable_name_causes_get(self, variable_name, **kwargs):
        """
        Search user correlations for a given effect
        Returns average of all correlations and votes for all user cause variables for a given effect

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_variables_variable_name_causes_get(variable_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str variable_name: Effect variable name (required)
        :return: list[Correlation]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_variables_variable_name_causes_get_with_http_info(variable_name, **kwargs)
        else:
            (data) = self.v1_variables_variable_name_causes_get_with_http_info(variable_name, **kwargs)
            return data

    def v1_variables_variable_name_causes_get_with_http_info(self, variable_name, **kwargs):
        """
        Search user correlations for a given effect
        Returns average of all correlations and votes for all user cause variables for a given effect

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_variables_variable_name_causes_get_with_http_info(variable_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str variable_name: Effect variable name (required)
        :return: list[Correlation]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['variable_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_variables_variable_name_causes_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'variable_name' is set
        if ('variable_name' not in params) or (params['variable_name'] is None):
            raise ValueError("Missing the required parameter `variable_name` when calling `v1_variables_variable_name_causes_get`")

        resource_path = '/v1/variables/{variableName}/causes'.replace('{format}', 'json')
        path_params = {}
        if 'variable_name' in params:
            path_params['variableName'] = params['variable_name']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Correlation]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v1_variables_variable_name_effects_get(self, variable_name, **kwargs):
        """
        Search user correlations for a given cause
        Returns average of all correlations and votes for all user effect variables for a given cause

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_variables_variable_name_effects_get(variable_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str variable_name: Cause variable name (required)
        :param str access_token: User's OAuth2 access token
        :return: list[Correlation]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_variables_variable_name_effects_get_with_http_info(variable_name, **kwargs)
        else:
            (data) = self.v1_variables_variable_name_effects_get_with_http_info(variable_name, **kwargs)
            return data

    def v1_variables_variable_name_effects_get_with_http_info(self, variable_name, **kwargs):
        """
        Search user correlations for a given cause
        Returns average of all correlations and votes for all user effect variables for a given cause

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_variables_variable_name_effects_get_with_http_info(variable_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str variable_name: Cause variable name (required)
        :param str access_token: User's OAuth2 access token
        :return: list[Correlation]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['variable_name', 'access_token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_variables_variable_name_effects_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'variable_name' is set
        if ('variable_name' not in params) or (params['variable_name'] is None):
            raise ValueError("Missing the required parameter `variable_name` when calling `v1_variables_variable_name_effects_get`")

        resource_path = '/v1/variables/{variableName}/effects'.replace('{format}', 'json')
        path_params = {}
        if 'variable_name' in params:
            path_params['variableName'] = params['variable_name']

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Correlation]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v1_variables_variable_name_public_causes_get(self, variable_name, **kwargs):
        """
        Search public correlations for a given effect
        Returns average of all correlations and votes for all public cause variables for a given effect

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_variables_variable_name_public_causes_get(variable_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str variable_name: Effect variable name (required)
        :param str access_token: User's OAuth2 access token
        :return: list[Correlation]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_variables_variable_name_public_causes_get_with_http_info(variable_name, **kwargs)
        else:
            (data) = self.v1_variables_variable_name_public_causes_get_with_http_info(variable_name, **kwargs)
            return data

    def v1_variables_variable_name_public_causes_get_with_http_info(self, variable_name, **kwargs):
        """
        Search public correlations for a given effect
        Returns average of all correlations and votes for all public cause variables for a given effect

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_variables_variable_name_public_causes_get_with_http_info(variable_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str variable_name: Effect variable name (required)
        :param str access_token: User's OAuth2 access token
        :return: list[Correlation]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['variable_name', 'access_token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_variables_variable_name_public_causes_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'variable_name' is set
        if ('variable_name' not in params) or (params['variable_name'] is None):
            raise ValueError("Missing the required parameter `variable_name` when calling `v1_variables_variable_name_public_causes_get`")

        resource_path = '/v1/variables/{variableName}/public/causes'.replace('{format}', 'json')
        path_params = {}
        if 'variable_name' in params:
            path_params['variableName'] = params['variable_name']

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Correlation]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v1_variables_variable_name_public_effects_get(self, variable_name, **kwargs):
        """
        Search public correlations for a given cause
        Returns average of all correlations and votes for all public cause variables for a given cause

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_variables_variable_name_public_effects_get(variable_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str variable_name: Cause variable name (required)
        :param str access_token: User's OAuth2 access token
        :return: list[Correlation]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_variables_variable_name_public_effects_get_with_http_info(variable_name, **kwargs)
        else:
            (data) = self.v1_variables_variable_name_public_effects_get_with_http_info(variable_name, **kwargs)
            return data

    def v1_variables_variable_name_public_effects_get_with_http_info(self, variable_name, **kwargs):
        """
        Search public correlations for a given cause
        Returns average of all correlations and votes for all public cause variables for a given cause

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_variables_variable_name_public_effects_get_with_http_info(variable_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str variable_name: Cause variable name (required)
        :param str access_token: User's OAuth2 access token
        :return: list[Correlation]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['variable_name', 'access_token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_variables_variable_name_public_effects_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'variable_name' is set
        if ('variable_name' not in params) or (params['variable_name'] is None):
            raise ValueError("Missing the required parameter `variable_name` when calling `v1_variables_variable_name_public_effects_get`")

        resource_path = '/v1/variables/{variableName}/public/effects'.replace('{format}', 'json')
        path_params = {}
        if 'variable_name' in params:
            path_params['variableName'] = params['variable_name']

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Correlation]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v1_votes_delete_post(self, body, **kwargs):
        """
        Delete vote
        Delete previously posted vote

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_votes_delete_post(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param VoteDelete body: The cause and effect variable names for the predictor vote to be deleted. (required)
        :param str access_token: User's OAuth2 access token
        :return: CommonResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_votes_delete_post_with_http_info(body, **kwargs)
        else:
            (data) = self.v1_votes_delete_post_with_http_info(body, **kwargs)
            return data

    def v1_votes_delete_post_with_http_info(self, body, **kwargs):
        """
        Delete vote
        Delete previously posted vote

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_votes_delete_post_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param VoteDelete body: The cause and effect variable names for the predictor vote to be deleted. (required)
        :param str access_token: User's OAuth2 access token
        :return: CommonResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'access_token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_votes_delete_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_votes_delete_post`")

        resource_path = '/v1/votes/delete'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CommonResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v1_votes_post(self, body, **kwargs):
        """
        Post or update vote
        This is to enable users to indicate their opinion on the plausibility of a causal relationship between a treatment and outcome. QuantiModo incorporates crowd-sourced plausibility estimations into their algorithm. This is done allowing user to indicate their view of the plausibility of each relationship with thumbs up/down buttons placed next to each prediction.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_votes_post(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param PostVote body: Contains the cause variable, effect variable, and vote value. (required)
        :param str access_token: User's OAuth2 access token
        :return: CommonResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_votes_post_with_http_info(body, **kwargs)
        else:
            (data) = self.v1_votes_post_with_http_info(body, **kwargs)
            return data

    def v1_votes_post_with_http_info(self, body, **kwargs):
        """
        Post or update vote
        This is to enable users to indicate their opinion on the plausibility of a causal relationship between a treatment and outcome. QuantiModo incorporates crowd-sourced plausibility estimations into their algorithm. This is done allowing user to indicate their view of the plausibility of each relationship with thumbs up/down buttons placed next to each prediction.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_votes_post_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param PostVote body: Contains the cause variable, effect variable, and vote value. (required)
        :param str access_token: User's OAuth2 access token
        :return: CommonResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'access_token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_votes_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_votes_post`")

        resource_path = '/v1/votes'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CommonResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
