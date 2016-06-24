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


class MeasurementsApi(object):
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

    def v1_measurement_sources_get(self, **kwargs):
        """
        Get measurement sources
        Returns a list of all the apps from which measurement data is obtained.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_measurement_sources_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: MeasurementSource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_measurement_sources_get_with_http_info(**kwargs)
        else:
            (data) = self.v1_measurement_sources_get_with_http_info(**kwargs)
            return data

    def v1_measurement_sources_get_with_http_info(self, **kwargs):
        """
        Get measurement sources
        Returns a list of all the apps from which measurement data is obtained.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_measurement_sources_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: MeasurementSource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_measurement_sources_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/measurementSources'.replace('{format}', 'json')
        path_params = {}

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
                                            response_type='MeasurementSource',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v1_measurement_sources_post(self, body, **kwargs):
        """
        Add a data source
        Add a life-tracking app or device to the QuantiModo list of data sources.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_measurement_sources_post(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param MeasurementSource body: An array of names of data sources you want to add. (required)
        :param str access_token: User's OAuth2 access token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_measurement_sources_post_with_http_info(body, **kwargs)
        else:
            (data) = self.v1_measurement_sources_post_with_http_info(body, **kwargs)
            return data

    def v1_measurement_sources_post_with_http_info(self, body, **kwargs):
        """
        Add a data source
        Add a life-tracking app or device to the QuantiModo list of data sources.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_measurement_sources_post_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param MeasurementSource body: An array of names of data sources you want to add. (required)
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
                    " to method v1_measurement_sources_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_measurement_sources_post`")

        resource_path = '/v1/measurementSources'.replace('{format}', 'json')
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

    def v1_measurements_daily_get(self, variable_name, **kwargs):
        """
        Get daily measurements for this user
        Measurements are any value that can be recorded like daily steps, a mood rating, or apples eaten. <br>Supported filter parameters:<br><ul><li><b>value</b> - Value of measurement</li><li><b>lastUpdated</b> - The time that this measurement was created or last updated in the UTC format \"YYYY-MM-DDThh:mm:ss\"</li></ul><br>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_measurements_daily_get(variable_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str variable_name: Name of the variable you want measurements for (required)
        :param str access_token: User's OAuth2 access token
        :param str abbreviated_unit_name: The unit your want the measurements in
        :param str start_time: The lower limit of measurements returned (Iso8601)
        :param str end_time: The upper limit of measurements returned (Iso8601)
        :param int grouping_width: The time (in seconds) over which measurements are grouped together
        :param str grouping_timezone: The time (in seconds) over which measurements are grouped together
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0.
        :param int offset: Now suppose you wanted to show results 11-20. You'd set the offset to 10 and the limit to 10.
        :param int sort: Sort by given field. If the field is prefixed with `-, it will sort in descending order.
        :return: Measurement
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_measurements_daily_get_with_http_info(variable_name, **kwargs)
        else:
            (data) = self.v1_measurements_daily_get_with_http_info(variable_name, **kwargs)
            return data

    def v1_measurements_daily_get_with_http_info(self, variable_name, **kwargs):
        """
        Get daily measurements for this user
        Measurements are any value that can be recorded like daily steps, a mood rating, or apples eaten. <br>Supported filter parameters:<br><ul><li><b>value</b> - Value of measurement</li><li><b>lastUpdated</b> - The time that this measurement was created or last updated in the UTC format \"YYYY-MM-DDThh:mm:ss\"</li></ul><br>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_measurements_daily_get_with_http_info(variable_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str variable_name: Name of the variable you want measurements for (required)
        :param str access_token: User's OAuth2 access token
        :param str abbreviated_unit_name: The unit your want the measurements in
        :param str start_time: The lower limit of measurements returned (Iso8601)
        :param str end_time: The upper limit of measurements returned (Iso8601)
        :param int grouping_width: The time (in seconds) over which measurements are grouped together
        :param str grouping_timezone: The time (in seconds) over which measurements are grouped together
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0.
        :param int offset: Now suppose you wanted to show results 11-20. You'd set the offset to 10 and the limit to 10.
        :param int sort: Sort by given field. If the field is prefixed with `-, it will sort in descending order.
        :return: Measurement
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['variable_name', 'access_token', 'abbreviated_unit_name', 'start_time', 'end_time', 'grouping_width', 'grouping_timezone', 'limit', 'offset', 'sort']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_measurements_daily_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'variable_name' is set
        if ('variable_name' not in params) or (params['variable_name'] is None):
            raise ValueError("Missing the required parameter `variable_name` when calling `v1_measurements_daily_get`")

        resource_path = '/v1/measurements/daily'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']
        if 'variable_name' in params:
            query_params['variableName'] = params['variable_name']
        if 'abbreviated_unit_name' in params:
            query_params['abbreviatedUnitName'] = params['abbreviated_unit_name']
        if 'start_time' in params:
            query_params['startTime'] = params['start_time']
        if 'end_time' in params:
            query_params['endTime'] = params['end_time']
        if 'grouping_width' in params:
            query_params['groupingWidth'] = params['grouping_width']
        if 'grouping_timezone' in params:
            query_params['groupingTimezone'] = params['grouping_timezone']
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
                                            response_type='Measurement',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v1_measurements_delete_post(self, body, **kwargs):
        """
        Delete a measurement
        Delete a previously submitted measurement

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_measurements_delete_post(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param MeasurementDelete body: The startTime and variableId of the measurement to be deleted. (required)
        :return: CommonResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_measurements_delete_post_with_http_info(body, **kwargs)
        else:
            (data) = self.v1_measurements_delete_post_with_http_info(body, **kwargs)
            return data

    def v1_measurements_delete_post_with_http_info(self, body, **kwargs):
        """
        Delete a measurement
        Delete a previously submitted measurement

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_measurements_delete_post_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param MeasurementDelete body: The startTime and variableId of the measurement to be deleted. (required)
        :return: CommonResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_measurements_delete_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_measurements_delete_post`")

        resource_path = '/v1/measurements/delete'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

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

    def v1_measurements_get(self, **kwargs):
        """
        Get measurements for this user
        Measurements are any value that can be recorded like daily steps, a mood rating, or apples eaten. <br>Supported filter parameters:<br><ul><li><b>value</b> - Value of measurement</li><li><b>lastUpdated</b> - The time that this measurement was created or last updated in the UTC format \"YYYY-MM-DDThh:mm:ss\"</li></ul><br>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_measurements_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: User's OAuth2 access token
        :param str variable_name: Name of the variable you want measurements for
        :param str variable_category_name: Name of the variable category you want measurements for
        :param str source: Name of the source you want measurements for (supports exact name match only)
        :param str value: Value of measurement
        :param str last_updated: The time that this measurement was created or last updated in the format \"YYYY-MM-DDThh:mm:ss\"
        :param str unit: The unit you want the measurements returned in
        :param str start_time: The lower limit of measurements returned (Epoch)
        :param str created_at: The time the measurement record was first created in the format YYYY-MM-DDThh:mm:ss. Time zone should be UTC and not local.
        :param str updated_at: The time the measurement record was last changed in the format YYYY-MM-DDThh:mm:ss. Time zone should be UTC and not local.
        :param str end_time: The upper limit of measurements returned (Epoch)
        :param int grouping_width: The time (in seconds) over which measurements are grouped together
        :param str grouping_timezone: The time (in seconds) over which measurements are grouped together
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0.
        :param int offset: Now suppose you wanted to show results 11-20. You'd set the offset to 10 and the limit to 10.
        :param int sort: Sort by given field. If the field is prefixed with `-, it will sort in descending order.
        :return: Measurement
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_measurements_get_with_http_info(**kwargs)
        else:
            (data) = self.v1_measurements_get_with_http_info(**kwargs)
            return data

    def v1_measurements_get_with_http_info(self, **kwargs):
        """
        Get measurements for this user
        Measurements are any value that can be recorded like daily steps, a mood rating, or apples eaten. <br>Supported filter parameters:<br><ul><li><b>value</b> - Value of measurement</li><li><b>lastUpdated</b> - The time that this measurement was created or last updated in the UTC format \"YYYY-MM-DDThh:mm:ss\"</li></ul><br>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_measurements_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: User's OAuth2 access token
        :param str variable_name: Name of the variable you want measurements for
        :param str variable_category_name: Name of the variable category you want measurements for
        :param str source: Name of the source you want measurements for (supports exact name match only)
        :param str value: Value of measurement
        :param str last_updated: The time that this measurement was created or last updated in the format \"YYYY-MM-DDThh:mm:ss\"
        :param str unit: The unit you want the measurements returned in
        :param str start_time: The lower limit of measurements returned (Epoch)
        :param str created_at: The time the measurement record was first created in the format YYYY-MM-DDThh:mm:ss. Time zone should be UTC and not local.
        :param str updated_at: The time the measurement record was last changed in the format YYYY-MM-DDThh:mm:ss. Time zone should be UTC and not local.
        :param str end_time: The upper limit of measurements returned (Epoch)
        :param int grouping_width: The time (in seconds) over which measurements are grouped together
        :param str grouping_timezone: The time (in seconds) over which measurements are grouped together
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0.
        :param int offset: Now suppose you wanted to show results 11-20. You'd set the offset to 10 and the limit to 10.
        :param int sort: Sort by given field. If the field is prefixed with `-, it will sort in descending order.
        :return: Measurement
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token', 'variable_name', 'variable_category_name', 'source', 'value', 'last_updated', 'unit', 'start_time', 'created_at', 'updated_at', 'end_time', 'grouping_width', 'grouping_timezone', 'limit', 'offset', 'sort']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_measurements_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/measurements'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']
        if 'variable_name' in params:
            query_params['variableName'] = params['variable_name']
        if 'variable_category_name' in params:
            query_params['variableCategoryName'] = params['variable_category_name']
        if 'source' in params:
            query_params['source'] = params['source']
        if 'value' in params:
            query_params['value'] = params['value']
        if 'last_updated' in params:
            query_params['lastUpdated'] = params['last_updated']
        if 'unit' in params:
            query_params['unit'] = params['unit']
        if 'start_time' in params:
            query_params['startTime'] = params['start_time']
        if 'created_at' in params:
            query_params['createdAt'] = params['created_at']
        if 'updated_at' in params:
            query_params['updatedAt'] = params['updated_at']
        if 'end_time' in params:
            query_params['endTime'] = params['end_time']
        if 'grouping_width' in params:
            query_params['groupingWidth'] = params['grouping_width']
        if 'grouping_timezone' in params:
            query_params['groupingTimezone'] = params['grouping_timezone']
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
                                            response_type='Measurement',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v1_measurements_post(self, body, **kwargs):
        """
        Post a new set or update existing measurements to the database
        You can submit or update multiple measurements in a \"measurements\" sub-array.  If the variable these measurements correspond to does not already exist in the database, it will be automatically added.  The request body should look something like [{\"measurements\":[{\"startTime\":1439389320,\"value\":\"3\"}, {\"startTime\":1439389319,\"value\":\"2\"}],\"name\":\"Acne (out of 5)\",\"source\":\"QuantiModo\",\"category\":\"Symptoms\",\"combinationOperation\":\"MEAN\",\"unit\":\"/5\"}]

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_measurements_post(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param MeasurementSet body: An array of measurements you want to insert. (required)
        :param str access_token: User's OAuth2 access token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_measurements_post_with_http_info(body, **kwargs)
        else:
            (data) = self.v1_measurements_post_with_http_info(body, **kwargs)
            return data

    def v1_measurements_post_with_http_info(self, body, **kwargs):
        """
        Post a new set or update existing measurements to the database
        You can submit or update multiple measurements in a \"measurements\" sub-array.  If the variable these measurements correspond to does not already exist in the database, it will be automatically added.  The request body should look something like [{\"measurements\":[{\"startTime\":1439389320,\"value\":\"3\"}, {\"startTime\":1439389319,\"value\":\"2\"}],\"name\":\"Acne (out of 5)\",\"source\":\"QuantiModo\",\"category\":\"Symptoms\",\"combinationOperation\":\"MEAN\",\"unit\":\"/5\"}]

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_measurements_post_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param MeasurementSet body: An array of measurements you want to insert. (required)
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
                    " to method v1_measurements_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_measurements_post`")

        resource_path = '/v1/measurements'.replace('{format}', 'json')
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

    def v1_measurements_range_get(self, **kwargs):
        """
        Get measurements range for this user
        Get Unix time-stamp (epoch time) of the user's first and last measurements taken.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_measurements_range_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sources: Enter source name to limit to specific source (varchar)
        :param int user: If not specified, uses currently logged in user (bigint)
        :return: MeasurementRange
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_measurements_range_get_with_http_info(**kwargs)
        else:
            (data) = self.v1_measurements_range_get_with_http_info(**kwargs)
            return data

    def v1_measurements_range_get_with_http_info(self, **kwargs):
        """
        Get measurements range for this user
        Get Unix time-stamp (epoch time) of the user's first and last measurements taken.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_measurements_range_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sources: Enter source name to limit to specific source (varchar)
        :param int user: If not specified, uses currently logged in user (bigint)
        :return: MeasurementRange
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sources', 'user']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_measurements_range_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/measurementsRange'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'sources' in params:
            query_params['sources'] = params['sources']
        if 'user' in params:
            query_params['user'] = params['user']

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
                                            response_type='MeasurementRange',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v2_measurements_csv_get(self, **kwargs):
        """
        Get Measurements CSV
        Download a CSV containing all user measurements

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_measurements_csv_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: User's OAuth2 access token
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v2_measurements_csv_get_with_http_info(**kwargs)
        else:
            (data) = self.v2_measurements_csv_get_with_http_info(**kwargs)
            return data

    def v2_measurements_csv_get_with_http_info(self, **kwargs):
        """
        Get Measurements CSV
        Download a CSV containing all user measurements

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_measurements_csv_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: User's OAuth2 access token
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_measurements_csv_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v2/measurements/csv'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/csv'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['quantimodo_oauth2']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='file',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v2_measurements_id_delete(self, id, **kwargs):
        """
        Delete Measurement
        Delete Measurement

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_measurements_id_delete(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: id of Measurement (required)
        :param str access_token: User's OAuth2 access token
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v2_measurements_id_delete_with_http_info(id, **kwargs)
        else:
            (data) = self.v2_measurements_id_delete_with_http_info(id, **kwargs)
            return data

    def v2_measurements_id_delete_with_http_info(self, id, **kwargs):
        """
        Delete Measurement
        Delete Measurement

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_measurements_id_delete_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: id of Measurement (required)
        :param str access_token: User's OAuth2 access token
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'access_token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_measurements_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `v2_measurements_id_delete`")

        resource_path = '/v2/measurements/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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
        auth_settings = ['quantimodo_oauth2']

        return self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InlineResponse20012',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v2_measurements_id_get(self, id, **kwargs):
        """
        Get Measurement
        Get Measurement

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_measurements_id_get(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: id of Measurement (required)
        :param str access_token: User's OAuth2 access token
        :return: InlineResponse20011
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v2_measurements_id_get_with_http_info(id, **kwargs)
        else:
            (data) = self.v2_measurements_id_get_with_http_info(id, **kwargs)
            return data

    def v2_measurements_id_get_with_http_info(self, id, **kwargs):
        """
        Get Measurement
        Get Measurement

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_measurements_id_get_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: id of Measurement (required)
        :param str access_token: User's OAuth2 access token
        :return: InlineResponse20011
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'access_token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_measurements_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `v2_measurements_id_get`")

        resource_path = '/v2/measurements/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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
        auth_settings = ['quantimodo_oauth2']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InlineResponse20011',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v2_measurements_id_put(self, id, **kwargs):
        """
        Update Measurement
        Update Measurement

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_measurements_id_put(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: id of Measurement (required)
        :param str access_token: User's OAuth2 access token
        :param Measurement body: Measurement that should be updated
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v2_measurements_id_put_with_http_info(id, **kwargs)
        else:
            (data) = self.v2_measurements_id_put_with_http_info(id, **kwargs)
            return data

    def v2_measurements_id_put_with_http_info(self, id, **kwargs):
        """
        Update Measurement
        Update Measurement

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_measurements_id_put_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: id of Measurement (required)
        :param str access_token: User's OAuth2 access token
        :param Measurement body: Measurement that should be updated
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'access_token', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_measurements_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `v2_measurements_id_put`")

        resource_path = '/v2/measurements/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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
        auth_settings = ['quantimodo_oauth2']

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InlineResponse20012',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v2_measurements_request_csv_post(self, **kwargs):
        """
        Post Request for Measurements CSV
        Use this endpoint to schedule a CSV export containing all user measurements to be emailed to the user within 24 hours.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_measurements_request_csv_post(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: User's OAuth2 access token
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v2_measurements_request_csv_post_with_http_info(**kwargs)
        else:
            (data) = self.v2_measurements_request_csv_post_with_http_info(**kwargs)
            return data

    def v2_measurements_request_csv_post_with_http_info(self, **kwargs):
        """
        Post Request for Measurements CSV
        Use this endpoint to schedule a CSV export containing all user measurements to be emailed to the user within 24 hours.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_measurements_request_csv_post_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: User's OAuth2 access token
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_measurements_request_csv_post" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v2/measurements/request_csv'.replace('{format}', 'json')
        path_params = {}

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
        auth_settings = ['quantimodo_oauth2']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='int',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v2_measurements_request_pdf_post(self, **kwargs):
        """
        Post Request for Measurements PDF
        Use this endpoint to schedule a PDF export containing all user measurements to be emailed to the user within 24 hours.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_measurements_request_pdf_post(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: User's OAuth2 access token
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v2_measurements_request_pdf_post_with_http_info(**kwargs)
        else:
            (data) = self.v2_measurements_request_pdf_post_with_http_info(**kwargs)
            return data

    def v2_measurements_request_pdf_post_with_http_info(self, **kwargs):
        """
        Post Request for Measurements PDF
        Use this endpoint to schedule a PDF export containing all user measurements to be emailed to the user within 24 hours.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_measurements_request_pdf_post_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: User's OAuth2 access token
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_measurements_request_pdf_post" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v2/measurements/request_pdf'.replace('{format}', 'json')
        path_params = {}

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
        auth_settings = ['quantimodo_oauth2']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='int',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v2_measurements_request_xls_post(self, **kwargs):
        """
        Post Request for Measurements XLS
        Use this endpoint to schedule a XLS export containing all user measurements to be emailed to the user within 24 hours.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_measurements_request_xls_post(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: User's OAuth2 access token
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v2_measurements_request_xls_post_with_http_info(**kwargs)
        else:
            (data) = self.v2_measurements_request_xls_post_with_http_info(**kwargs)
            return data

    def v2_measurements_request_xls_post_with_http_info(self, **kwargs):
        """
        Post Request for Measurements XLS
        Use this endpoint to schedule a XLS export containing all user measurements to be emailed to the user within 24 hours.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_measurements_request_xls_post_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: User's OAuth2 access token
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_measurements_request_xls_post" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v2/measurements/request_xls'.replace('{format}', 'json')
        path_params = {}

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
        auth_settings = ['quantimodo_oauth2']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='int',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
