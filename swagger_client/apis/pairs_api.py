# coding: utf-8

"""
PairsApi.py
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
        # verify the required parameter 'cause' is set
        if cause is None:
            raise ValueError("Missing the required parameter `cause` when calling `v1_pairs_get`")
        # verify the required parameter 'effect' is set
        if effect is None:
            raise ValueError("Missing the required parameter `effect` when calling `v1_pairs_get`")

        all_params = ['cause', 'effect', 'cause_source', 'cause_unit', 'delay', 'duration', 'effect_source', 'effect_unit', 'end_time', 'start_time', 'limit', 'offset', 'sort']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_pairs_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/pairs'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}

        query_params = {}
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
                                            response_type='list[Pairs]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
