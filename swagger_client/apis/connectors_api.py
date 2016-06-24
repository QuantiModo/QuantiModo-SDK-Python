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


class ConnectorsApi(object):
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

    def v1_connect_js_get(self, **kwargs):
        """
        Get embeddable connect javascript
        Get embeddable connect javascript. Usage:    - Embedding in applications with popups for 3rd-party authentication windows.      Use `qmSetupInPopup` function after connecting `connect.js`.    - Embedding in applications with popups for 3rd-party authentication windows.      Requires a selector to block. It will be embedded in this block.      Use `qmSetupOnPage` function after connecting `connect.js`.    - Embedding in mobile applications without popups for 3rd-party authentication.      Use `qmSetupOnMobile` function after connecting `connect.js`.      if using the MoodiModo Clones, Use `qmSetupOnIonic` function after connecting `connect.js`. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_connect_js_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: User's OAuth2 access token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_connect_js_get_with_http_info(**kwargs)
        else:
            (data) = self.v1_connect_js_get_with_http_info(**kwargs)
            return data

    def v1_connect_js_get_with_http_info(self, **kwargs):
        """
        Get embeddable connect javascript
        Get embeddable connect javascript. Usage:    - Embedding in applications with popups for 3rd-party authentication windows.      Use `qmSetupInPopup` function after connecting `connect.js`.    - Embedding in applications with popups for 3rd-party authentication windows.      Requires a selector to block. It will be embedded in this block.      Use `qmSetupOnPage` function after connecting `connect.js`.    - Embedding in mobile applications without popups for 3rd-party authentication.      Use `qmSetupOnMobile` function after connecting `connect.js`.      if using the MoodiModo Clones, Use `qmSetupOnIonic` function after connecting `connect.js`. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_connect_js_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: User's OAuth2 access token
        :return: None
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
                    " to method v1_connect_js_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/connect.js'.replace('{format}', 'json')
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
            select_header_accept(['application/x-javascript'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2', 'internalApiKey']

        return self.api_client.call_api(resource_path, 'GET',
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

    def v1_connect_mobile_get(self, access_token, **kwargs):
        """
        Mobile connect page
        This page is designed to be opened in a webview.  Instead of using popup authentication boxes, it uses redirection. You can include the user's access_token as a URL parameter like https://app.quantimo.do/api/v1/connect/mobile?access_token=123

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_connect_mobile_get(access_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: User OAuth access token (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_connect_mobile_get_with_http_info(access_token, **kwargs)
        else:
            (data) = self.v1_connect_mobile_get_with_http_info(access_token, **kwargs)
            return data

    def v1_connect_mobile_get_with_http_info(self, access_token, **kwargs):
        """
        Mobile connect page
        This page is designed to be opened in a webview.  Instead of using popup authentication boxes, it uses redirection. You can include the user's access_token as a URL parameter like https://app.quantimo.do/api/v1/connect/mobile?access_token=123

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_connect_mobile_get_with_http_info(access_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: User OAuth access token (required)
        :return: None
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
                    " to method v1_connect_mobile_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `v1_connect_mobile_get`")

        resource_path = '/v1/connect/mobile'.replace('{format}', 'json')
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
            select_header_accept(['text/html'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2', 'internalApiKey']

        return self.api_client.call_api(resource_path, 'GET',
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

    def v1_connectors_connector_connect_get(self, connector, **kwargs):
        """
        Obtain a token from 3rd party data source
        Attempt to obtain a token from the data provider, store it in the database. With this, the connector to continue to obtain new user data until the token is revoked.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_connectors_connector_connect_get(connector, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str connector: Lowercase system name of the source application or device. Get a list of available connectors from the /connectors/list endpoint. (required)
        :param str access_token: User's OAuth2 access token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_connectors_connector_connect_get_with_http_info(connector, **kwargs)
        else:
            (data) = self.v1_connectors_connector_connect_get_with_http_info(connector, **kwargs)
            return data

    def v1_connectors_connector_connect_get_with_http_info(self, connector, **kwargs):
        """
        Obtain a token from 3rd party data source
        Attempt to obtain a token from the data provider, store it in the database. With this, the connector to continue to obtain new user data until the token is revoked.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_connectors_connector_connect_get_with_http_info(connector, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str connector: Lowercase system name of the source application or device. Get a list of available connectors from the /connectors/list endpoint. (required)
        :param str access_token: User's OAuth2 access token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['connector', 'access_token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_connectors_connector_connect_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'connector' is set
        if ('connector' not in params) or (params['connector'] is None):
            raise ValueError("Missing the required parameter `connector` when calling `v1_connectors_connector_connect_get`")

        resource_path = '/v1/connectors/{connector}/connect'.replace('{format}', 'json')
        path_params = {}
        if 'connector' in params:
            path_params['connector'] = params['connector']

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
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v1_connectors_connector_connect_instructions_get(self, connector, parameters, url, use_popup, **kwargs):
        """
        Connection Instructions
        Returns instructions that describe what parameters and endpoint to use to connect to the given data provider.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_connectors_connector_connect_instructions_get(connector, parameters, url, use_popup, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str connector: Lowercase system name of the source application or device. Get a list of available connectors from the /connectors/list endpoint. (required)
        :param str parameters: JSON Array of Parameters for the request to enable connector. (required)
        :param str url: URL which should be used to enable the connector. (required)
        :param bool use_popup: Should use popup when enabling connector (required)
        :param str access_token: User's OAuth2 access token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_connectors_connector_connect_instructions_get_with_http_info(connector, parameters, url, use_popup, **kwargs)
        else:
            (data) = self.v1_connectors_connector_connect_instructions_get_with_http_info(connector, parameters, url, use_popup, **kwargs)
            return data

    def v1_connectors_connector_connect_instructions_get_with_http_info(self, connector, parameters, url, use_popup, **kwargs):
        """
        Connection Instructions
        Returns instructions that describe what parameters and endpoint to use to connect to the given data provider.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_connectors_connector_connect_instructions_get_with_http_info(connector, parameters, url, use_popup, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str connector: Lowercase system name of the source application or device. Get a list of available connectors from the /connectors/list endpoint. (required)
        :param str parameters: JSON Array of Parameters for the request to enable connector. (required)
        :param str url: URL which should be used to enable the connector. (required)
        :param bool use_popup: Should use popup when enabling connector (required)
        :param str access_token: User's OAuth2 access token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['connector', 'parameters', 'url', 'use_popup', 'access_token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_connectors_connector_connect_instructions_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'connector' is set
        if ('connector' not in params) or (params['connector'] is None):
            raise ValueError("Missing the required parameter `connector` when calling `v1_connectors_connector_connect_instructions_get`")
        # verify the required parameter 'parameters' is set
        if ('parameters' not in params) or (params['parameters'] is None):
            raise ValueError("Missing the required parameter `parameters` when calling `v1_connectors_connector_connect_instructions_get`")
        # verify the required parameter 'url' is set
        if ('url' not in params) or (params['url'] is None):
            raise ValueError("Missing the required parameter `url` when calling `v1_connectors_connector_connect_instructions_get`")
        # verify the required parameter 'use_popup' is set
        if ('use_popup' not in params) or (params['use_popup'] is None):
            raise ValueError("Missing the required parameter `use_popup` when calling `v1_connectors_connector_connect_instructions_get`")

        resource_path = '/v1/connectors/{connector}/connectInstructions'.replace('{format}', 'json')
        path_params = {}
        if 'connector' in params:
            path_params['connector'] = params['connector']

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']
        if 'parameters' in params:
            query_params['parameters'] = params['parameters']
        if 'url' in params:
            query_params['url'] = params['url']
        if 'use_popup' in params:
            query_params['usePopup'] = params['use_popup']

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
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v1_connectors_connector_connect_parameter_get(self, connector, display_name, key, placeholder, type, use_popup, **kwargs):
        """
        Connect Parameter
        Returns instructions that describe what parameters and endpoint to use to connect to the given data provider.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_connectors_connector_connect_parameter_get(connector, display_name, key, placeholder, type, use_popup, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str connector: Lowercase system name of the source application or device. Get a list of available connectors from the /connectors/list endpoint. (required)
        :param str display_name: Name of the parameter that is user visible in the form (required)
        :param str key: Name of the property that the user has to enter such as username or password Connector (used in HTTP request) (required)
        :param str placeholder: Placeholder hint value for the parameter input tag. (required)
        :param str type: Type of input field such as those found here http://www.w3schools.com/tags/tag_input.asp (required)
        :param bool use_popup: Should use popup when enabling connector (required)
        :param str access_token: User's OAuth2 access token
        :param str default_value: Default parameter value
        :return: ConnectorInstruction
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_connectors_connector_connect_parameter_get_with_http_info(connector, display_name, key, placeholder, type, use_popup, **kwargs)
        else:
            (data) = self.v1_connectors_connector_connect_parameter_get_with_http_info(connector, display_name, key, placeholder, type, use_popup, **kwargs)
            return data

    def v1_connectors_connector_connect_parameter_get_with_http_info(self, connector, display_name, key, placeholder, type, use_popup, **kwargs):
        """
        Connect Parameter
        Returns instructions that describe what parameters and endpoint to use to connect to the given data provider.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_connectors_connector_connect_parameter_get_with_http_info(connector, display_name, key, placeholder, type, use_popup, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str connector: Lowercase system name of the source application or device. Get a list of available connectors from the /connectors/list endpoint. (required)
        :param str display_name: Name of the parameter that is user visible in the form (required)
        :param str key: Name of the property that the user has to enter such as username or password Connector (used in HTTP request) (required)
        :param str placeholder: Placeholder hint value for the parameter input tag. (required)
        :param str type: Type of input field such as those found here http://www.w3schools.com/tags/tag_input.asp (required)
        :param bool use_popup: Should use popup when enabling connector (required)
        :param str access_token: User's OAuth2 access token
        :param str default_value: Default parameter value
        :return: ConnectorInstruction
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['connector', 'display_name', 'key', 'placeholder', 'type', 'use_popup', 'access_token', 'default_value']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_connectors_connector_connect_parameter_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'connector' is set
        if ('connector' not in params) or (params['connector'] is None):
            raise ValueError("Missing the required parameter `connector` when calling `v1_connectors_connector_connect_parameter_get`")
        # verify the required parameter 'display_name' is set
        if ('display_name' not in params) or (params['display_name'] is None):
            raise ValueError("Missing the required parameter `display_name` when calling `v1_connectors_connector_connect_parameter_get`")
        # verify the required parameter 'key' is set
        if ('key' not in params) or (params['key'] is None):
            raise ValueError("Missing the required parameter `key` when calling `v1_connectors_connector_connect_parameter_get`")
        # verify the required parameter 'placeholder' is set
        if ('placeholder' not in params) or (params['placeholder'] is None):
            raise ValueError("Missing the required parameter `placeholder` when calling `v1_connectors_connector_connect_parameter_get`")
        # verify the required parameter 'type' is set
        if ('type' not in params) or (params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `v1_connectors_connector_connect_parameter_get`")
        # verify the required parameter 'use_popup' is set
        if ('use_popup' not in params) or (params['use_popup'] is None):
            raise ValueError("Missing the required parameter `use_popup` when calling `v1_connectors_connector_connect_parameter_get`")

        resource_path = '/v1/connectors/{connector}/connectParameter'.replace('{format}', 'json')
        path_params = {}
        if 'connector' in params:
            path_params['connector'] = params['connector']

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']
        if 'default_value' in params:
            query_params['defaultValue'] = params['default_value']
        if 'display_name' in params:
            query_params['displayName'] = params['display_name']
        if 'key' in params:
            query_params['key'] = params['key']
        if 'placeholder' in params:
            query_params['placeholder'] = params['placeholder']
        if 'type' in params:
            query_params['type'] = params['type']
        if 'use_popup' in params:
            query_params['usePopup'] = params['use_popup']

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
                                            response_type='ConnectorInstruction',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v1_connectors_connector_disconnect_get(self, connector, **kwargs):
        """
        Delete stored connection info
        The disconnect method deletes any stored tokens or connection information from the connectors database.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_connectors_connector_disconnect_get(connector, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str connector: Lowercase system name of the source application or device. Get a list of available connectors from the /connectors/list endpoint. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_connectors_connector_disconnect_get_with_http_info(connector, **kwargs)
        else:
            (data) = self.v1_connectors_connector_disconnect_get_with_http_info(connector, **kwargs)
            return data

    def v1_connectors_connector_disconnect_get_with_http_info(self, connector, **kwargs):
        """
        Delete stored connection info
        The disconnect method deletes any stored tokens or connection information from the connectors database.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_connectors_connector_disconnect_get_with_http_info(connector, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str connector: Lowercase system name of the source application or device. Get a list of available connectors from the /connectors/list endpoint. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['connector']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_connectors_connector_disconnect_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'connector' is set
        if ('connector' not in params) or (params['connector'] is None):
            raise ValueError("Missing the required parameter `connector` when calling `v1_connectors_connector_disconnect_get`")

        resource_path = '/v1/connectors/{connector}/disconnect'.replace('{format}', 'json')
        path_params = {}
        if 'connector' in params:
            path_params['connector'] = params['connector']

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
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v1_connectors_connector_info_get(self, connector, **kwargs):
        """
        Get connector info for user
        Returns information about the connector such as the connector id, whether or not is connected for this user (i.e. we have a token or credentials), and its update history for the user.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_connectors_connector_info_get(connector, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str connector: Lowercase system name of the source application or device. Get a list of available connectors from the /connectors/list endpoint. (required)
        :param str access_token: User's OAuth2 access token
        :return: ConnectorInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_connectors_connector_info_get_with_http_info(connector, **kwargs)
        else:
            (data) = self.v1_connectors_connector_info_get_with_http_info(connector, **kwargs)
            return data

    def v1_connectors_connector_info_get_with_http_info(self, connector, **kwargs):
        """
        Get connector info for user
        Returns information about the connector such as the connector id, whether or not is connected for this user (i.e. we have a token or credentials), and its update history for the user.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_connectors_connector_info_get_with_http_info(connector, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str connector: Lowercase system name of the source application or device. Get a list of available connectors from the /connectors/list endpoint. (required)
        :param str access_token: User's OAuth2 access token
        :return: ConnectorInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['connector', 'access_token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_connectors_connector_info_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'connector' is set
        if ('connector' not in params) or (params['connector'] is None):
            raise ValueError("Missing the required parameter `connector` when calling `v1_connectors_connector_info_get`")

        resource_path = '/v1/connectors/{connector}/info'.replace('{format}', 'json')
        path_params = {}
        if 'connector' in params:
            path_params['connector'] = params['connector']

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
                                            response_type='ConnectorInfo',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v1_connectors_connector_update_get(self, connector, **kwargs):
        """
        Sync with data source
        The update method tells the QM Connector Framework to check with the data provider (such as Fitbit or MyFitnessPal) and retrieve any new measurements available.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_connectors_connector_update_get(connector, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str connector: Lowercase system name of the source application or device (required)
        :param str access_token: User's OAuth2 access token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_connectors_connector_update_get_with_http_info(connector, **kwargs)
        else:
            (data) = self.v1_connectors_connector_update_get_with_http_info(connector, **kwargs)
            return data

    def v1_connectors_connector_update_get_with_http_info(self, connector, **kwargs):
        """
        Sync with data source
        The update method tells the QM Connector Framework to check with the data provider (such as Fitbit or MyFitnessPal) and retrieve any new measurements available.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_connectors_connector_update_get_with_http_info(connector, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str connector: Lowercase system name of the source application or device (required)
        :param str access_token: User's OAuth2 access token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['connector', 'access_token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_connectors_connector_update_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'connector' is set
        if ('connector' not in params) or (params['connector'] is None):
            raise ValueError("Missing the required parameter `connector` when calling `v1_connectors_connector_update_get`")

        resource_path = '/v1/connectors/{connector}/update'.replace('{format}', 'json')
        path_params = {}
        if 'connector' in params:
            path_params['connector'] = params['connector']

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
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v1_connectors_list_get(self, **kwargs):
        """
        List of Connectors
        A connector pulls data from other data providers using their API or a screenscraper. Returns a list of all available connectors and information about them such as their id, name, whether the user has provided access, logo url, connection instructions, and the update history.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_connectors_list_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[Connector]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_connectors_list_get_with_http_info(**kwargs)
        else:
            (data) = self.v1_connectors_list_get_with_http_info(**kwargs)
            return data

    def v1_connectors_list_get_with_http_info(self, **kwargs):
        """
        List of Connectors
        A connector pulls data from other data providers using their API or a screenscraper. Returns a list of all available connectors and information about them such as their id, name, whether the user has provided access, logo url, connection instructions, and the update history.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_connectors_list_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[Connector]
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
                    " to method v1_connectors_list_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/connectors/list'.replace('{format}', 'json')
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
                                            response_type='list[Connector]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
