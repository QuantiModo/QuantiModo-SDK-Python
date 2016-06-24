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


class PairsApi(object):
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

    def v1_pairs_csv_get(self, cause, effect, **kwargs):
        """
        Get pairs
        Pairs cause measurements with effect measurements grouped over the duration of action after the onset delay.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_pairs_csv_get(cause, effect, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str cause: Original variable name for the explanatory or independent variable (required)
        :param str effect: Original variable name for the outcome or dependent variable (required)
        :param str access_token: User's OAuth2 access token
        :param str cause_source: Name of data source that the cause measurements should come from
        :param str cause_unit: Abbreviated name for the unit cause measurements to be returned in
        :param str delay: Delay before onset of action (in seconds) from the cause variable settings.
        :param str duration: Duration of action (in seconds) from the cause variable settings.
        :param str effect_source: Name of data source that the effectmeasurements should come from
        :param str effect_unit: Abbreviated name for the unit effect measurements to be returned in
        :param str end_time: The most recent date (in epoch time) for which we should return measurements
        :param str start_time: The earliest date (in epoch time) for which we should return measurements
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0.
        :param int offset: Now suppose you wanted to show results 11-20. You'd set the offset to 10 and the limit to 10.
        :param int sort: Sort by given field. If the field is prefixed with `-, it will sort in descending order.
        :return: list[Pairs]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_pairs_csv_get_with_http_info(cause, effect, **kwargs)
        else:
            (data) = self.v1_pairs_csv_get_with_http_info(cause, effect, **kwargs)
            return data

    def v1_pairs_csv_get_with_http_info(self, cause, effect, **kwargs):
        """
        Get pairs
        Pairs cause measurements with effect measurements grouped over the duration of action after the onset delay.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_pairs_csv_get_with_http_info(cause, effect, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str cause: Original variable name for the explanatory or independent variable (required)
        :param str effect: Original variable name for the outcome or dependent variable (required)
        :param str access_token: User's OAuth2 access token
        :param str cause_source: Name of data source that the cause measurements should come from
        :param str cause_unit: Abbreviated name for the unit cause measurements to be returned in
        :param str delay: Delay before onset of action (in seconds) from the cause variable settings.
        :param str duration: Duration of action (in seconds) from the cause variable settings.
        :param str effect_source: Name of data source that the effectmeasurements should come from
        :param str effect_unit: Abbreviated name for the unit effect measurements to be returned in
        :param str end_time: The most recent date (in epoch time) for which we should return measurements
        :param str start_time: The earliest date (in epoch time) for which we should return measurements
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0.
        :param int offset: Now suppose you wanted to show results 11-20. You'd set the offset to 10 and the limit to 10.
        :param int sort: Sort by given field. If the field is prefixed with `-, it will sort in descending order.
        :return: list[Pairs]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cause', 'effect', 'access_token', 'cause_source', 'cause_unit', 'delay', 'duration', 'effect_source', 'effect_unit', 'end_time', 'start_time', 'limit', 'offset', 'sort']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_pairs_csv_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cause' is set
        if ('cause' not in params) or (params['cause'] is None):
            raise ValueError("Missing the required parameter `cause` when calling `v1_pairs_csv_get`")
        # verify the required parameter 'effect' is set
        if ('effect' not in params) or (params['effect'] is None):
            raise ValueError("Missing the required parameter `effect` when calling `v1_pairs_csv_get`")

        resource_path = '/v1/pairsCsv'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']
        if 'cause' in params:
            query_params['cause'] = params['cause']
        if 'cause_source' in params:
            query_params['causeSource'] = params['cause_source']
        if 'cause_unit' in params:
            query_params['causeUnit'] = params['cause_unit']
        if 'delay' in params:
            query_params['delay'] = params['delay']
        if 'duration' in params:
            query_params['duration'] = params['duration']
        if 'effect' in params:
            query_params['effect'] = params['effect']
        if 'effect_source' in params:
            query_params['effectSource'] = params['effect_source']
        if 'effect_unit' in params:
            query_params['effectUnit'] = params['effect_unit']
        if 'end_time' in params:
            query_params['endTime'] = params['end_time']
        if 'start_time' in params:
            query_params['startTime'] = params['start_time']
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
                                            response_type='list[Pairs]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v1_pairs_get(self, cause, effect, **kwargs):
        """
        Get pairs
        Pairs cause measurements with effect measurements grouped over the duration of action after the onset delay.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_pairs_get(cause, effect, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str cause: Original variable name for the explanatory or independent variable (required)
        :param str effect: Original variable name for the outcome or dependent variable (required)
        :param str access_token: User's OAuth2 access token
        :param str cause_source: Name of data source that the cause measurements should come from
        :param str cause_unit: Abbreviated name for the unit cause measurements to be returned in
        :param str delay: Delay before onset of action (in seconds) from the cause variable settings.
        :param str duration: Duration of action (in seconds) from the cause variable settings.
        :param str effect_source: Name of data source that the effectmeasurements should come from
        :param str effect_unit: Abbreviated name for the unit effect measurements to be returned in
        :param str end_time: The most recent date (in epoch time) for which we should return measurements
        :param str start_time: The earliest date (in epoch time) for which we should return measurements
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0.
        :param int offset: Now suppose you wanted to show results 11-20. You'd set the offset to 10 and the limit to 10.
        :param int sort: Sort by given field. If the field is prefixed with `-, it will sort in descending order.
        :return: list[Pairs]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_pairs_get_with_http_info(cause, effect, **kwargs)
        else:
            (data) = self.v1_pairs_get_with_http_info(cause, effect, **kwargs)
            return data

    def v1_pairs_get_with_http_info(self, cause, effect, **kwargs):
        """
        Get pairs
        Pairs cause measurements with effect measurements grouped over the duration of action after the onset delay.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_pairs_get_with_http_info(cause, effect, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str cause: Original variable name for the explanatory or independent variable (required)
        :param str effect: Original variable name for the outcome or dependent variable (required)
        :param str access_token: User's OAuth2 access token
        :param str cause_source: Name of data source that the cause measurements should come from
        :param str cause_unit: Abbreviated name for the unit cause measurements to be returned in
        :param str delay: Delay before onset of action (in seconds) from the cause variable settings.
        :param str duration: Duration of action (in seconds) from the cause variable settings.
        :param str effect_source: Name of data source that the effectmeasurements should come from
        :param str effect_unit: Abbreviated name for the unit effect measurements to be returned in
        :param str end_time: The most recent date (in epoch time) for which we should return measurements
        :param str start_time: The earliest date (in epoch time) for which we should return measurements
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0.
        :param int offset: Now suppose you wanted to show results 11-20. You'd set the offset to 10 and the limit to 10.
        :param int sort: Sort by given field. If the field is prefixed with `-, it will sort in descending order.
        :return: list[Pairs]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cause', 'effect', 'access_token', 'cause_source', 'cause_unit', 'delay', 'duration', 'effect_source', 'effect_unit', 'end_time', 'start_time', 'limit', 'offset', 'sort']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_pairs_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cause' is set
        if ('cause' not in params) or (params['cause'] is None):
            raise ValueError("Missing the required parameter `cause` when calling `v1_pairs_get`")
        # verify the required parameter 'effect' is set
        if ('effect' not in params) or (params['effect'] is None):
            raise ValueError("Missing the required parameter `effect` when calling `v1_pairs_get`")

        resource_path = '/v1/pairs'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']
        if 'cause' in params:
            query_params['cause'] = params['cause']
        if 'cause_source' in params:
            query_params['causeSource'] = params['cause_source']
        if 'cause_unit' in params:
            query_params['causeUnit'] = params['cause_unit']
        if 'delay' in params:
            query_params['delay'] = params['delay']
        if 'duration' in params:
            query_params['duration'] = params['duration']
        if 'effect' in params:
            query_params['effect'] = params['effect']
        if 'effect_source' in params:
            query_params['effectSource'] = params['effect_source']
        if 'effect_unit' in params:
            query_params['effectUnit'] = params['effect_unit']
        if 'end_time' in params:
            query_params['endTime'] = params['end_time']
        if 'start_time' in params:
            query_params['startTime'] = params['start_time']
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
                                            response_type='list[Pairs]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
