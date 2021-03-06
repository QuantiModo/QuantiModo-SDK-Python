# coding: utf-8

"""
VariableCategoryApi.py
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
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class VariableCategoryApi(object):
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

    def variable_categories_get(self, **kwargs):
        """
        Get all VariableCategories
        Get all VariableCategories

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.variable_categories_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: name
        :param float filling_value: filling_value
        :param float maximum_allowed_value: maximum_allowed_value
        :param float minimum_allowed_value: minimum_allowed_value
        :param int duration_of_action: duration_of_action
        :param int onset_delay: onset_delay
        :param str combination_operation: combination_operation
        :param int updated: updated
        :param bool cause_only: cause_only
        :param int public: public
        :param bool outcome: outcome
        :param str created_at: created_at
        :param str updated_at: updated_at
        :param str image_url: image_url
        :param int default_unit_id: default_unit_id
        :param int limit: limit
        :param int offset: offset
        :param str sort: sort
        :return: InlineResponse20023
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'filling_value', 'maximum_allowed_value', 'minimum_allowed_value', 'duration_of_action', 'onset_delay', 'combination_operation', 'updated', 'cause_only', 'public', 'outcome', 'created_at', 'updated_at', 'image_url', 'default_unit_id', 'limit', 'offset', 'sort']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method variable_categories_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/variableCategories'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}

        query_params = {}
        if 'name' in params:
            query_params['name'] = params['name']
        if 'filling_value' in params:
            query_params['filling_value'] = params['filling_value']
        if 'maximum_allowed_value' in params:
            query_params['maximum_allowed_value'] = params['maximum_allowed_value']
        if 'minimum_allowed_value' in params:
            query_params['minimum_allowed_value'] = params['minimum_allowed_value']
        if 'duration_of_action' in params:
            query_params['duration_of_action'] = params['duration_of_action']
        if 'onset_delay' in params:
            query_params['onset_delay'] = params['onset_delay']
        if 'combination_operation' in params:
            query_params['combination_operation'] = params['combination_operation']
        if 'updated' in params:
            query_params['updated'] = params['updated']
        if 'cause_only' in params:
            query_params['cause_only'] = params['cause_only']
        if 'public' in params:
            query_params['public'] = params['public']
        if 'outcome' in params:
            query_params['outcome'] = params['outcome']
        if 'created_at' in params:
            query_params['created_at'] = params['created_at']
        if 'updated_at' in params:
            query_params['updated_at'] = params['updated_at']
        if 'image_url' in params:
            query_params['image_url'] = params['image_url']
        if 'default_unit_id' in params:
            query_params['default_unit_id'] = params['default_unit_id']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'sort' in params:
            query_params['sort'] = params['sort']

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
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='InlineResponse20023',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def variable_categories_post(self, **kwargs):
        """
        Store VariableCategory
        Store VariableCategory

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.variable_categories_post(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param VariableCategory body: VariableCategory that should be stored
        :return: InlineResponse20024
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method variable_categories_post" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/variableCategories'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

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
        auth_settings = []

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='InlineResponse20024',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def variable_categories_id_get(self, id, **kwargs):
        """
        Get VariableCategory
        Get VariableCategory

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.variable_categories_id_get(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: id of VariableCategory (required)
        :return: InlineResponse20024
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # verify the required parameter 'id' is set
        if id is None:
            raise ValueError("Missing the required parameter `id` when calling `variable_categories_id_get`")

        all_params = ['id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method variable_categories_id_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/variableCategories/{id}'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='InlineResponse20024',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def variable_categories_id_put(self, id, **kwargs):
        """
        Update VariableCategory
        Update VariableCategory

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.variable_categories_id_put(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: id of VariableCategory (required)
        :param VariableCategory body: VariableCategory that should be updated
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # verify the required parameter 'id' is set
        if id is None:
            raise ValueError("Missing the required parameter `id` when calling `variable_categories_id_put`")

        all_params = ['id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method variable_categories_id_put" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/variableCategories/{id}'.replace('{format}', 'json')
        method = 'PUT'

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

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
        auth_settings = []

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='InlineResponse2002',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def variable_categories_id_delete(self, id, **kwargs):
        """
        Delete VariableCategory
        Delete VariableCategory

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.variable_categories_id_delete(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: id of VariableCategory (required)
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # verify the required parameter 'id' is set
        if id is None:
            raise ValueError("Missing the required parameter `id` when calling `variable_categories_id_delete`")

        all_params = ['id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method variable_categories_id_delete" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/variableCategories/{id}'.replace('{format}', 'json')
        method = 'DELETE'

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='InlineResponse2002',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
