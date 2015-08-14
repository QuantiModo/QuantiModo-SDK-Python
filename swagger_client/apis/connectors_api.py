#!/usr/bin/env python
# coding: utf-8

"""
ConnectorsApi.py
Copyright 2015 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

NOTE: This class is auto generated by the swagger code generator program.
      Do not edit the class manually.
"""
from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class ConnectorsApi(object):

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient('https://localhost/api')
            self.api_client = config.api_client

    def connectors_list_get(self, **kwargs):
        """
        List of Connectors
        Returns a list of all available connectors. A connector pulls data from other data providers using their API or a screenscraper.

        This method makes a synchronous HTTP request by default.To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.connectors_list_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[Connector]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method connectors_list_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/connectors/list'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['oauth2']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='list[Connector]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def connectors_connector_connect_get(self, connector, **kwargs):
        """
        Obtain a token from 3rd party data source
        Attempt to obtain a token from the data provider, store it in the database. With this, the connector to continue to obtain new user data until the token is revoked.

        This method makes a synchronous HTTP request by default.To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.connectors_connector_connect_get(connector, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str connector: Lowercase system name of the source application or device. Get a list of available connectors from the /connectors/list endpoint. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # verify the required parameter 'connector' is set
        if connector is None:
            raise ValueError("Missing the required parameter `connector` when calling `connectors_connector_connect_get`")

        all_params = ['connector']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method connectors_connector_connect_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/connectors/{connector}/connect'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        if 'connector' in params:
            path_params['connector'] = params['connector']

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['oauth2']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def connectors_connector_connect_instructions_get(self, connector, url, parameters, use_popup, **kwargs):
        """
        Get connection parameters
        Returns instructions that describe what parameters and endpoint to use to connect to the given data provider.

        This method makes a synchronous HTTP request by default.To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.connectors_connector_connect_instructions_get(connector, url, parameters, use_popup, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str connector: Lowercase system name of the source application or device. Get a list of available connectors from the /connectors/list endpoint. (required)
        :param str url: URL which should be used to enable the connector (required)
        :param list[str] parameters: Array of Parameters for the request to enable connector (required)
        :param bool use_popup: Should use popup when enabling connector (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # verify the required parameter 'connector' is set
        if connector is None:
            raise ValueError("Missing the required parameter `connector` when calling `connectors_connector_connect_instructions_get`")
        # verify the required parameter 'url' is set
        if url is None:
            raise ValueError("Missing the required parameter `url` when calling `connectors_connector_connect_instructions_get`")
        # verify the required parameter 'parameters' is set
        if parameters is None:
            raise ValueError("Missing the required parameter `parameters` when calling `connectors_connector_connect_instructions_get`")
        # verify the required parameter 'use_popup' is set
        if use_popup is None:
            raise ValueError("Missing the required parameter `use_popup` when calling `connectors_connector_connect_instructions_get`")

        all_params = ['connector', 'url', 'parameters', 'use_popup']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method connectors_connector_connect_instructions_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/connectors/{connector}/connectInstructions'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        if 'connector' in params:
            path_params['connector'] = params['connector']

        query_params = {}
        if 'url' in params:
            query_params['url'] = params['url']
        if 'parameters' in params:
            query_params['parameters'] = params['parameters']
        if 'use_popup' in params:
            query_params['usePopup'] = params['use_popup']

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['oauth2']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def connectors_connector_connect_parameter_get(self, connector, display_name, key, use_popup, type, placeholder, default_value, **kwargs):
        """
        Get connection parameters
        Returns instructions that describe what parameters and endpoint to use to connect to the given data provider.

        This method makes a synchronous HTTP request by default.To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.connectors_connector_connect_parameter_get(connector, display_name, key, use_popup, type, placeholder, default_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str connector: Lowercase system name of the source application or device. Get a list of available connectors from the /connectors/list endpoint. (required)
        :param str display_name: Name of the parameter that is user visible in the form (required)
        :param str key: Name of the property that the user has to enter such as username or password Connector (used in HTTP request) TODO What's a connector key? (required)
        :param bool use_popup: Should use popup when enabling connector (required)
        :param str type: Type of input field such as those found here http://www.w3schools.com/tags/tag_input.asp (required)
        :param str placeholder: Placeholder hint value for the parameter input tag (required)
        :param str default_value: Default parameter value (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # verify the required parameter 'connector' is set
        if connector is None:
            raise ValueError("Missing the required parameter `connector` when calling `connectors_connector_connect_parameter_get`")
        # verify the required parameter 'display_name' is set
        if display_name is None:
            raise ValueError("Missing the required parameter `display_name` when calling `connectors_connector_connect_parameter_get`")
        # verify the required parameter 'key' is set
        if key is None:
            raise ValueError("Missing the required parameter `key` when calling `connectors_connector_connect_parameter_get`")
        # verify the required parameter 'use_popup' is set
        if use_popup is None:
            raise ValueError("Missing the required parameter `use_popup` when calling `connectors_connector_connect_parameter_get`")
        # verify the required parameter 'type' is set
        if type is None:
            raise ValueError("Missing the required parameter `type` when calling `connectors_connector_connect_parameter_get`")
        # verify the required parameter 'placeholder' is set
        if placeholder is None:
            raise ValueError("Missing the required parameter `placeholder` when calling `connectors_connector_connect_parameter_get`")
        # verify the required parameter 'default_value' is set
        if default_value is None:
            raise ValueError("Missing the required parameter `default_value` when calling `connectors_connector_connect_parameter_get`")

        all_params = ['connector', 'display_name', 'key', 'use_popup', 'type', 'placeholder', 'default_value']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method connectors_connector_connect_parameter_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/connectors/{connector}/connectParameter'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        if 'connector' in params:
            path_params['connector'] = params['connector']

        query_params = {}
        if 'display_name' in params:
            query_params['displayName'] = params['display_name']
        if 'key' in params:
            query_params['key'] = params['key']
        if 'use_popup' in params:
            query_params['usePopup'] = params['use_popup']
        if 'type' in params:
            query_params['type'] = params['type']
        if 'placeholder' in params:
            query_params['placeholder'] = params['placeholder']
        if 'default_value' in params:
            query_params['defaultValue'] = params['default_value']

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['oauth2']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def connectors_connector_disconnect_get(self, connector, **kwargs):
        """
        Delete stored connection info
        The disconnect method deletes any stored tokens or connection information from the connectors database.

        This method makes a synchronous HTTP request by default.To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.connectors_connector_disconnect_get(connector, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str connector: Lowercase system name of the source application or device. Get a list of available connectors from the /connectors/list endpoint. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # verify the required parameter 'connector' is set
        if connector is None:
            raise ValueError("Missing the required parameter `connector` when calling `connectors_connector_disconnect_get`")

        all_params = ['connector']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method connectors_connector_disconnect_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/connectors/{connector}/disconnect'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        if 'connector' in params:
            path_params['connector'] = params['connector']

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['oauth2']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def connectors_connector_info_get(self, connector, **kwargs):
        """
        Get connector info for user
        Returns information about the connector such as the connector id, whether or not is connected for this user (i.e. we have a token or credentials), and its update history for the user.

        This method makes a synchronous HTTP request by default.To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.connectors_connector_info_get(connector, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str connector: Lowercase system name of the source application or device. Get a list of available connectors from the /connectors/list endpoint. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # verify the required parameter 'connector' is set
        if connector is None:
            raise ValueError("Missing the required parameter `connector` when calling `connectors_connector_info_get`")

        all_params = ['connector']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method connectors_connector_info_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/connectors/{connector}/info'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        if 'connector' in params:
            path_params['connector'] = params['connector']

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['oauth2']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def connectors_connector_update_get(self, connector, **kwargs):
        """
        Sync with data source
        The update method tells the QM Connector Framework to check with the data provider (such as Fitbit or MyFitnessPal) and retrieve any new measurements available.

        This method makes a synchronous HTTP request by default.To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.connectors_connector_update_get(connector, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str connector: Lowercase system name of the source application or device (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # verify the required parameter 'connector' is set
        if connector is None:
            raise ValueError("Missing the required parameter `connector` when calling `connectors_connector_update_get`")

        all_params = ['connector']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method connectors_connector_update_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/connectors/{connector}/update'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        if 'connector' in params:
            path_params['connector'] = params['connector']

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['oauth2']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
