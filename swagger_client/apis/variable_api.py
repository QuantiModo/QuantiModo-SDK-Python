# coding: utf-8

"""
VariableApi.py
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


class VariableApi(object):
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

    def variables_get(self, **kwargs):
        """
        Get all Variables
        Get all Variables

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.variables_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: id
        :param str client_id: client_id
        :param int parent_id: parent_id
        :param str name: name
        :param int variable_category_id: variable_category_id
        :param int default_unit_id: default_unit_id
        :param str combination_operation: combination_operation
        :param float filling_value: filling_value
        :param float maximum_allowed_value: maximum_allowed_value
        :param float minimum_allowed_value: minimum_allowed_value
        :param int onset_delay: onset_delay
        :param int duration_of_action: duration_of_action
        :param int public: public
        :param bool cause_only: cause_only
        :param float most_common_value: most_common_value
        :param int most_common_unit_id: most_common_unit_id
        :param float standard_deviation: standard_deviation
        :param float variance: variance
        :param float mean: mean
        :param float median: median
        :param float number_of_measurements: number_of_measurements
        :param float number_of_unique_values: number_of_unique_values
        :param float skewness: skewness
        :param float kurtosis: kurtosis
        :param float latitude: latitude
        :param float longitude: longitude
        :param str location: location
        :param str status: status
        :param str error_message: error_message
        :param str last_successful_update_time: last_successful_update_time
        :param str created_at: created_at
        :param str updated_at: updated_at
        :param str product_url: product_url
        :param str image_url: image_url
        :param float price: price
        :param int number_of_user_variables: number_of_user_variables
        :param bool outcome: outcome
        :param float minimum_recorded_value: minimum_recorded_value
        :param float maximum_recorded_value: maximum_recorded_value
        :param int limit: limit
        :param int offset: offset
        :param str sort: sort
        :return: InlineResponse20027
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'client_id', 'parent_id', 'name', 'variable_category_id', 'default_unit_id', 'combination_operation', 'filling_value', 'maximum_allowed_value', 'minimum_allowed_value', 'onset_delay', 'duration_of_action', 'public', 'cause_only', 'most_common_value', 'most_common_unit_id', 'standard_deviation', 'variance', 'mean', 'median', 'number_of_measurements', 'number_of_unique_values', 'skewness', 'kurtosis', 'latitude', 'longitude', 'location', 'status', 'error_message', 'last_successful_update_time', 'created_at', 'updated_at', 'product_url', 'image_url', 'price', 'number_of_user_variables', 'outcome', 'minimum_recorded_value', 'maximum_recorded_value', 'limit', 'offset', 'sort']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method variables_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/variables'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}

        query_params = {}
        if 'id' in params:
            query_params['id'] = params['id']
        if 'client_id' in params:
            query_params['client_id'] = params['client_id']
        if 'parent_id' in params:
            query_params['parent_id'] = params['parent_id']
        if 'name' in params:
            query_params['name'] = params['name']
        if 'variable_category_id' in params:
            query_params['variable_category_id'] = params['variable_category_id']
        if 'default_unit_id' in params:
            query_params['default_unit_id'] = params['default_unit_id']
        if 'combination_operation' in params:
            query_params['combination_operation'] = params['combination_operation']
        if 'filling_value' in params:
            query_params['filling_value'] = params['filling_value']
        if 'maximum_allowed_value' in params:
            query_params['maximum_allowed_value'] = params['maximum_allowed_value']
        if 'minimum_allowed_value' in params:
            query_params['minimum_allowed_value'] = params['minimum_allowed_value']
        if 'onset_delay' in params:
            query_params['onset_delay'] = params['onset_delay']
        if 'duration_of_action' in params:
            query_params['duration_of_action'] = params['duration_of_action']
        if 'public' in params:
            query_params['public'] = params['public']
        if 'cause_only' in params:
            query_params['cause_only'] = params['cause_only']
        if 'most_common_value' in params:
            query_params['most_common_value'] = params['most_common_value']
        if 'most_common_unit_id' in params:
            query_params['most_common_unit_id'] = params['most_common_unit_id']
        if 'standard_deviation' in params:
            query_params['standard_deviation'] = params['standard_deviation']
        if 'variance' in params:
            query_params['variance'] = params['variance']
        if 'mean' in params:
            query_params['mean'] = params['mean']
        if 'median' in params:
            query_params['median'] = params['median']
        if 'number_of_measurements' in params:
            query_params['number_of_measurements'] = params['number_of_measurements']
        if 'number_of_unique_values' in params:
            query_params['number_of_unique_values'] = params['number_of_unique_values']
        if 'skewness' in params:
            query_params['skewness'] = params['skewness']
        if 'kurtosis' in params:
            query_params['kurtosis'] = params['kurtosis']
        if 'latitude' in params:
            query_params['latitude'] = params['latitude']
        if 'longitude' in params:
            query_params['longitude'] = params['longitude']
        if 'location' in params:
            query_params['location'] = params['location']
        if 'status' in params:
            query_params['status'] = params['status']
        if 'error_message' in params:
            query_params['error_message'] = params['error_message']
        if 'last_successful_update_time' in params:
            query_params['last_successful_update_time'] = params['last_successful_update_time']
        if 'created_at' in params:
            query_params['created_at'] = params['created_at']
        if 'updated_at' in params:
            query_params['updated_at'] = params['updated_at']
        if 'product_url' in params:
            query_params['product_url'] = params['product_url']
        if 'image_url' in params:
            query_params['image_url'] = params['image_url']
        if 'price' in params:
            query_params['price'] = params['price']
        if 'number_of_user_variables' in params:
            query_params['number_of_user_variables'] = params['number_of_user_variables']
        if 'outcome' in params:
            query_params['outcome'] = params['outcome']
        if 'minimum_recorded_value' in params:
            query_params['minimum_recorded_value'] = params['minimum_recorded_value']
        if 'maximum_recorded_value' in params:
            query_params['maximum_recorded_value'] = params['maximum_recorded_value']
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
                                            response_type='InlineResponse20027',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def variables_post(self, **kwargs):
        """
        Store Variable
        Store Variable

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.variables_post(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Variable body: Variable that should be stored
        :return: InlineResponse20028
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
                    " to method variables_post" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/variables'.replace('{format}', 'json')
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
                                            response_type='InlineResponse20028',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def variables_id_get(self, id, **kwargs):
        """
        Get Variable
        Get Variable

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.variables_id_get(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: id of Variable (required)
        :return: InlineResponse20028
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # verify the required parameter 'id' is set
        if id is None:
            raise ValueError("Missing the required parameter `id` when calling `variables_id_get`")

        all_params = ['id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method variables_id_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/variables/{id}'.replace('{format}', 'json')
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
                                            response_type='InlineResponse20028',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def variables_id_put(self, id, **kwargs):
        """
        Update Variable
        Update Variable

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.variables_id_put(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: id of Variable (required)
        :param Variable body: Variable that should be updated
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # verify the required parameter 'id' is set
        if id is None:
            raise ValueError("Missing the required parameter `id` when calling `variables_id_put`")

        all_params = ['id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method variables_id_put" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/variables/{id}'.replace('{format}', 'json')
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

    def variables_id_delete(self, id, **kwargs):
        """
        Delete Variable
        Delete Variable

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.variables_id_delete(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: id of Variable (required)
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # verify the required parameter 'id' is set
        if id is None:
            raise ValueError("Missing the required parameter `id` when calling `variables_id_delete`")

        all_params = ['id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method variables_id_delete" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/variables/{id}'.replace('{format}', 'json')
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