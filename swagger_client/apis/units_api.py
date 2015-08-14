#!/usr/bin/env python
# coding: utf-8

"""
UnitsApi.py
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


class UnitsApi(object):

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient('https://localhost/api')
            self.api_client = config.api_client

    def unit_categories_get(self, **kwargs):
        """
        Get unit categories
        Get a list of the categories of measurement units such as 'Distance', 'Duration', 'Energy', 'Frequency', 'Miscellany', 'Pressure', 'Proportion', 'Rating', 'Temperature', 'Volume', and 'Weight'.

        This method makes a synchronous HTTP request by default.To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.unit_categories_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: UnitCategory
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
                    " to method unit_categories_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/unitCategories'.replace('{format}', 'json')
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
                                            response_type='UnitCategory',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def units_get(self, **kwargs):
        """
        Get all available units
        Get all available units

        This method makes a synchronous HTTP request by default.To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.units_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str unit_name: Unit name
        :param str abbreviated_unit_name: Restrict the results to a specific unit by providing the unit abbreviation.
        :param str category_name: Restrict the results to a specific unit category by providing the unit category name.
        :return: list[Unit]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['unit_name', 'abbreviated_unit_name', 'category_name']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method units_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/units'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}

        query_params = {}
        if 'unit_name' in params:
            query_params['unitName'] = params['unit_name']
        if 'abbreviated_unit_name' in params:
            query_params['abbreviatedUnitName'] = params['abbreviated_unit_name']
        if 'category_name' in params:
            query_params['categoryName'] = params['category_name']

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
                                            response_type='list[Unit]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def units_variable_get(self, **kwargs):
        """
        Units for Variable
        Get a list of all possible units to use for a given variable

        This method makes a synchronous HTTP request by default.To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.units_variable_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str unit_name: Name of Unit you want to retrieve
        :param str abbreviated_unit_name: Abbreviated Unit Name of the unit you want
        :param str category_name: Name of the category you want units for
        :param str variable: Name of the variable you want units for
        :return: list[Unit]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['unit_name', 'abbreviated_unit_name', 'category_name', 'variable']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method units_variable_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/unitsVariable'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}

        query_params = {}
        if 'unit_name' in params:
            query_params['unitName'] = params['unit_name']
        if 'abbreviated_unit_name' in params:
            query_params['abbreviatedUnitName'] = params['abbreviated_unit_name']
        if 'category_name' in params:
            query_params['categoryName'] = params['category_name']
        if 'variable' in params:
            query_params['variable'] = params['variable']

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
                                            response_type='list[Unit]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
