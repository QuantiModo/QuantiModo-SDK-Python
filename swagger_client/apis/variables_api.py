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


class VariablesApi(object):
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

    def v1_public_variables_get(self, **kwargs):
        """
        Get public variables
        This endpoint retrieves an array of all public variables. Public variables are things like foods, medications, symptoms, conditions, and anything not unique to a particular user. For instance, a telephone number or name would not be a public variable.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_public_variables_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: Variable
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_public_variables_get_with_http_info(**kwargs)
        else:
            (data) = self.v1_public_variables_get_with_http_info(**kwargs)
            return data

    def v1_public_variables_get_with_http_info(self, **kwargs):
        """
        Get public variables
        This endpoint retrieves an array of all public variables. Public variables are things like foods, medications, symptoms, conditions, and anything not unique to a particular user. For instance, a telephone number or name would not be a public variable.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_public_variables_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: Variable
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
                    " to method v1_public_variables_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/public/variables'.replace('{format}', 'json')
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
                                            response_type='Variable',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v1_public_variables_search_search_get(self, search, **kwargs):
        """
        Get top 5 PUBLIC variables with the most correlations
        Get top 5 PUBLIC variables with the most correlations containing the entered search characters. For example, search for 'mood' as an effect. Since 'Overall Mood' has a lot of correlations with other variables, it should be in the autocomplete list.<br>Supported filter parameters:<br><ul><li><b>category</b> - Category of Variable</li></ul><br>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_public_variables_search_search_get(search, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str search: Search query can be some fraction of a variable name. (required)
        :param str access_token: User's OAuth2 access token
        :param str category_name: Filter variables by category name. The variable categories include Activity, Causes of Illness, Cognitive Performance, Conditions, Environment, Foods, Location, Miscellaneous, Mood, Nutrition, Physical Activity, Physique, Sleep, Social Interactions, Symptoms, Treatments, Vital Signs, and Work.
        :param str source: Specify a data source name to only return variables from a specific data source.
        :param str effect_or_cause: Indicate if you only want variables that have user correlations.  Possible values are effect and cause.
        :param str public_effect_or_cause: Indicate if you only want variables that have aggregated correlations.  Possible values are effect and cause.
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0.
        :param int offset: Now suppose you wanted to show results 11-20. You'd set the offset to 10 and the limit to 10.
        :param int sort: Sort by given field. If the field is prefixed with `-, it will sort in descending order.
        :return: Variable
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_public_variables_search_search_get_with_http_info(search, **kwargs)
        else:
            (data) = self.v1_public_variables_search_search_get_with_http_info(search, **kwargs)
            return data

    def v1_public_variables_search_search_get_with_http_info(self, search, **kwargs):
        """
        Get top 5 PUBLIC variables with the most correlations
        Get top 5 PUBLIC variables with the most correlations containing the entered search characters. For example, search for 'mood' as an effect. Since 'Overall Mood' has a lot of correlations with other variables, it should be in the autocomplete list.<br>Supported filter parameters:<br><ul><li><b>category</b> - Category of Variable</li></ul><br>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_public_variables_search_search_get_with_http_info(search, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str search: Search query can be some fraction of a variable name. (required)
        :param str access_token: User's OAuth2 access token
        :param str category_name: Filter variables by category name. The variable categories include Activity, Causes of Illness, Cognitive Performance, Conditions, Environment, Foods, Location, Miscellaneous, Mood, Nutrition, Physical Activity, Physique, Sleep, Social Interactions, Symptoms, Treatments, Vital Signs, and Work.
        :param str source: Specify a data source name to only return variables from a specific data source.
        :param str effect_or_cause: Indicate if you only want variables that have user correlations.  Possible values are effect and cause.
        :param str public_effect_or_cause: Indicate if you only want variables that have aggregated correlations.  Possible values are effect and cause.
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0.
        :param int offset: Now suppose you wanted to show results 11-20. You'd set the offset to 10 and the limit to 10.
        :param int sort: Sort by given field. If the field is prefixed with `-, it will sort in descending order.
        :return: Variable
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search', 'access_token', 'category_name', 'source', 'effect_or_cause', 'public_effect_or_cause', 'limit', 'offset', 'sort']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_public_variables_search_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search' is set
        if ('search' not in params) or (params['search'] is None):
            raise ValueError("Missing the required parameter `search` when calling `v1_public_variables_search_search_get`")

        resource_path = '/v1/public/variables/search/{search}'.replace('{format}', 'json')
        path_params = {}
        if 'search' in params:
            path_params['search'] = params['search']

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']
        if 'category_name' in params:
            query_params['categoryName'] = params['category_name']
        if 'source' in params:
            query_params['source'] = params['source']
        if 'effect_or_cause' in params:
            query_params['effectOrCause'] = params['effect_or_cause']
        if 'public_effect_or_cause' in params:
            query_params['publicEffectOrCause'] = params['public_effect_or_cause']
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
                                            response_type='Variable',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v1_user_variables_post(self, user_variables, **kwargs):
        """
        Update User Settings for a Variable
        Users can change the parameters used in analysis of that variable such as the expected duration of action for a variable to have an effect, the estimated delay before the onset of action. In order to filter out erroneous data, they are able to set the maximum and minimum reasonable daily values for a variable.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_user_variables_post(user_variables, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UserVariables user_variables: Variable user settings data (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_user_variables_post_with_http_info(user_variables, **kwargs)
        else:
            (data) = self.v1_user_variables_post_with_http_info(user_variables, **kwargs)
            return data

    def v1_user_variables_post_with_http_info(self, user_variables, **kwargs):
        """
        Update User Settings for a Variable
        Users can change the parameters used in analysis of that variable such as the expected duration of action for a variable to have an effect, the estimated delay before the onset of action. In order to filter out erroneous data, they are able to set the maximum and minimum reasonable daily values for a variable.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_user_variables_post_with_http_info(user_variables, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UserVariables user_variables: Variable user settings data (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_variables']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_user_variables_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_variables' is set
        if ('user_variables' not in params) or (params['user_variables'] is None):
            raise ValueError("Missing the required parameter `user_variables` when calling `v1_user_variables_post`")

        resource_path = '/v1/userVariables'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'user_variables' in params:
            body_params = params['user_variables']

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

    def v1_variable_categories_get(self, **kwargs):
        """
        Variable categories
        The variable categories include Activity, Causes of Illness, Cognitive Performance, Conditions, Environment, Foods, Location, Miscellaneous, Mood, Nutrition, Physical Activity, Physique, Sleep, Social Interactions, Symptoms, Treatments, Vital Signs, and Work.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_variable_categories_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[VariableCategory]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_variable_categories_get_with_http_info(**kwargs)
        else:
            (data) = self.v1_variable_categories_get_with_http_info(**kwargs)
            return data

    def v1_variable_categories_get_with_http_info(self, **kwargs):
        """
        Variable categories
        The variable categories include Activity, Causes of Illness, Cognitive Performance, Conditions, Environment, Foods, Location, Miscellaneous, Mood, Nutrition, Physical Activity, Physique, Sleep, Social Interactions, Symptoms, Treatments, Vital Signs, and Work.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_variable_categories_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[VariableCategory]
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
                    " to method v1_variable_categories_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/variableCategories'.replace('{format}', 'json')
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
                                            response_type='list[VariableCategory]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v1_variables_get(self, **kwargs):
        """
        Get variables by the category name
        Get variables by the category name. <br>Supported filter parameters:<br><ul><li><b>name</b> - Original name of the variable (supports exact name match only)</li><li><b>lastUpdated</b> - Filter by the last time any of the properties of the variable were changed. Uses UTC format \"YYYY-MM-DDThh:mm:ss\"</li><li><b>source</b> - The name of the data source that created the variable (supports exact name match only). So if you have a client application and you only want variables that were last updated by your app, you can include the name of your app here</li><li><b>latestMeasurementTime</b> - Filter variables based on the last time a measurement for them was created or updated in the UTC format \"YYYY-MM-DDThh:mm:ss\"</li><li><b>numberOfMeasurements</b> - Filter variables by the total number of measurements that they have. This could be used of you want to filter or sort by popularity.</li><li><b>lastSource</b> - Limit variables to those which measurements were last submitted by a specific source. So if you have a client application and you only want variables that were last updated by your app, you can include the name of your app here. (supports exact name match only)</li></ul><br>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_variables_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: User's OAuth2 access token
        :param int id: Common variable id
        :param int user_id: User id
        :param str category: Filter data by category
        :param str name: Original name of the variable (supports exact name match only)
        :param str last_updated: Filter by the last time any of the properties of the variable were changed. Uses UTC format \"YYYY-MM-DDThh:mm:ss\"
        :param str source: The name of the data source that created the variable (supports exact name match only). So if you have a client application and you only want variables that were last updated by your app, you can include the name of your app here
        :param str latest_measurement_time: Filter variables based on the last time a measurement for them was created or updated in the UTC format \"YYYY-MM-DDThh:mm:ss\"
        :param str number_of_measurements: Filter variables by the total number of measurements that they have. This could be used of you want to filter or sort by popularity.
        :param str last_source: Limit variables to those which measurements were last submitted by a specific source. So if you have a client application and you only want variables that were last updated by your app, you can include the name of your app here. (supports exact name match only)
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0.
        :param int offset: Now suppose you wanted to show results 11-20. You'd set the offset to 10 and the limit to 10.
        :param int sort: Sort by given field. If the field is prefixed with `-, it will sort in descending order.
        :return: Variable
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_variables_get_with_http_info(**kwargs)
        else:
            (data) = self.v1_variables_get_with_http_info(**kwargs)
            return data

    def v1_variables_get_with_http_info(self, **kwargs):
        """
        Get variables by the category name
        Get variables by the category name. <br>Supported filter parameters:<br><ul><li><b>name</b> - Original name of the variable (supports exact name match only)</li><li><b>lastUpdated</b> - Filter by the last time any of the properties of the variable were changed. Uses UTC format \"YYYY-MM-DDThh:mm:ss\"</li><li><b>source</b> - The name of the data source that created the variable (supports exact name match only). So if you have a client application and you only want variables that were last updated by your app, you can include the name of your app here</li><li><b>latestMeasurementTime</b> - Filter variables based on the last time a measurement for them was created or updated in the UTC format \"YYYY-MM-DDThh:mm:ss\"</li><li><b>numberOfMeasurements</b> - Filter variables by the total number of measurements that they have. This could be used of you want to filter or sort by popularity.</li><li><b>lastSource</b> - Limit variables to those which measurements were last submitted by a specific source. So if you have a client application and you only want variables that were last updated by your app, you can include the name of your app here. (supports exact name match only)</li></ul><br>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_variables_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: User's OAuth2 access token
        :param int id: Common variable id
        :param int user_id: User id
        :param str category: Filter data by category
        :param str name: Original name of the variable (supports exact name match only)
        :param str last_updated: Filter by the last time any of the properties of the variable were changed. Uses UTC format \"YYYY-MM-DDThh:mm:ss\"
        :param str source: The name of the data source that created the variable (supports exact name match only). So if you have a client application and you only want variables that were last updated by your app, you can include the name of your app here
        :param str latest_measurement_time: Filter variables based on the last time a measurement for them was created or updated in the UTC format \"YYYY-MM-DDThh:mm:ss\"
        :param str number_of_measurements: Filter variables by the total number of measurements that they have. This could be used of you want to filter or sort by popularity.
        :param str last_source: Limit variables to those which measurements were last submitted by a specific source. So if you have a client application and you only want variables that were last updated by your app, you can include the name of your app here. (supports exact name match only)
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0.
        :param int offset: Now suppose you wanted to show results 11-20. You'd set the offset to 10 and the limit to 10.
        :param int sort: Sort by given field. If the field is prefixed with `-, it will sort in descending order.
        :return: Variable
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token', 'id', 'user_id', 'category', 'name', 'last_updated', 'source', 'latest_measurement_time', 'number_of_measurements', 'last_source', 'limit', 'offset', 'sort']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_variables_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/variables'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']
        if 'id' in params:
            query_params['id'] = params['id']
        if 'user_id' in params:
            query_params['userId'] = params['user_id']
        if 'category' in params:
            query_params['category'] = params['category']
        if 'name' in params:
            query_params['name'] = params['name']
        if 'last_updated' in params:
            query_params['lastUpdated'] = params['last_updated']
        if 'source' in params:
            query_params['source'] = params['source']
        if 'latest_measurement_time' in params:
            query_params['latestMeasurementTime'] = params['latest_measurement_time']
        if 'number_of_measurements' in params:
            query_params['numberOfMeasurements'] = params['number_of_measurements']
        if 'last_source' in params:
            query_params['lastSource'] = params['last_source']
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
        auth_settings = ['oauth2', 'basicAuth']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Variable',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v1_variables_post(self, body, **kwargs):
        """
        Create Variables
        Allows the client to create a new variable in the `variables` table.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_variables_post(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param VariablesNew body: Original name for the variable. (required)
        :param str access_token: User's OAuth2 access token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_variables_post_with_http_info(body, **kwargs)
        else:
            (data) = self.v1_variables_post_with_http_info(body, **kwargs)
            return data

    def v1_variables_post_with_http_info(self, body, **kwargs):
        """
        Create Variables
        Allows the client to create a new variable in the `variables` table.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_variables_post_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param VariablesNew body: Original name for the variable. (required)
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
                    " to method v1_variables_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_variables_post`")

        resource_path = '/v1/variables'.replace('{format}', 'json')
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

    def v1_variables_search_search_get(self, search, **kwargs):
        """
        Get variables by search query
        Get variables containing the search characters for which the currently logged in user has measurements. Used to provide auto-complete function in variable search boxes.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_variables_search_search_get(search, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str search: Search query which may be an entire variable name or a fragment of one. (required)
        :param str access_token: User's OAuth2 access token
        :param str category_name: Filter variables by category name. The variable categories include Activity, Causes of Illness, Cognitive Performance, Conditions, Environment, Foods, Location, Miscellaneous, Mood, Nutrition, Physical Activity, Physique, Sleep, Social Interactions, Symptoms, Treatments, Vital Signs, and Work.
        :param bool include_public: Set to true if you would like to include public variables when no user variables are found.
        :param bool manual_tracking: Set to true if you would like to exlude variables like apps and website names.
        :param str source: Specify a data source name to only return variables from a specific data source.
        :param str effect_or_cause: Indicate if you only want variables that have user correlations.  Possible values are effect and cause.
        :param str public_effect_or_cause: Indicate if you only want variables that have aggregated correlations.  Possible values are effect and cause.
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0.
        :param int offset: Now suppose you wanted to show results 11-20. You'd set the offset to 10 and the limit to 10.
        :return: list[Variable]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_variables_search_search_get_with_http_info(search, **kwargs)
        else:
            (data) = self.v1_variables_search_search_get_with_http_info(search, **kwargs)
            return data

    def v1_variables_search_search_get_with_http_info(self, search, **kwargs):
        """
        Get variables by search query
        Get variables containing the search characters for which the currently logged in user has measurements. Used to provide auto-complete function in variable search boxes.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_variables_search_search_get_with_http_info(search, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str search: Search query which may be an entire variable name or a fragment of one. (required)
        :param str access_token: User's OAuth2 access token
        :param str category_name: Filter variables by category name. The variable categories include Activity, Causes of Illness, Cognitive Performance, Conditions, Environment, Foods, Location, Miscellaneous, Mood, Nutrition, Physical Activity, Physique, Sleep, Social Interactions, Symptoms, Treatments, Vital Signs, and Work.
        :param bool include_public: Set to true if you would like to include public variables when no user variables are found.
        :param bool manual_tracking: Set to true if you would like to exlude variables like apps and website names.
        :param str source: Specify a data source name to only return variables from a specific data source.
        :param str effect_or_cause: Indicate if you only want variables that have user correlations.  Possible values are effect and cause.
        :param str public_effect_or_cause: Indicate if you only want variables that have aggregated correlations.  Possible values are effect and cause.
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0.
        :param int offset: Now suppose you wanted to show results 11-20. You'd set the offset to 10 and the limit to 10.
        :return: list[Variable]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search', 'access_token', 'category_name', 'include_public', 'manual_tracking', 'source', 'effect_or_cause', 'public_effect_or_cause', 'limit', 'offset']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_variables_search_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search' is set
        if ('search' not in params) or (params['search'] is None):
            raise ValueError("Missing the required parameter `search` when calling `v1_variables_search_search_get`")

        resource_path = '/v1/variables/search/{search}'.replace('{format}', 'json')
        path_params = {}
        if 'search' in params:
            path_params['search'] = params['search']

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']
        if 'category_name' in params:
            query_params['categoryName'] = params['category_name']
        if 'include_public' in params:
            query_params['includePublic'] = params['include_public']
        if 'manual_tracking' in params:
            query_params['manualTracking'] = params['manual_tracking']
        if 'source' in params:
            query_params['source'] = params['source']
        if 'effect_or_cause' in params:
            query_params['effectOrCause'] = params['effect_or_cause']
        if 'public_effect_or_cause' in params:
            query_params['publicEffectOrCause'] = params['public_effect_or_cause']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'offset' in params:
            query_params['offset'] = params['offset']

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
                                            response_type='list[Variable]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v1_variables_variable_name_get(self, variable_name, **kwargs):
        """
        Get info about a variable
        Get all of the settings and information about a variable by its name. If the logged in user has modified the settings for the variable, these will be provided instead of the default settings for that variable.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_variables_variable_name_get(variable_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str variable_name: Variable name (required)
        :param str access_token: User's OAuth2 access token
        :return: Variable
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_variables_variable_name_get_with_http_info(variable_name, **kwargs)
        else:
            (data) = self.v1_variables_variable_name_get_with_http_info(variable_name, **kwargs)
            return data

    def v1_variables_variable_name_get_with_http_info(self, variable_name, **kwargs):
        """
        Get info about a variable
        Get all of the settings and information about a variable by its name. If the logged in user has modified the settings for the variable, these will be provided instead of the default settings for that variable.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_variables_variable_name_get_with_http_info(variable_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str variable_name: Variable name (required)
        :param str access_token: User's OAuth2 access token
        :return: Variable
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
                    " to method v1_variables_variable_name_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'variable_name' is set
        if ('variable_name' not in params) or (params['variable_name'] is None):
            raise ValueError("Missing the required parameter `variable_name` when calling `v1_variables_variable_name_get`")

        resource_path = '/v1/variables/{variableName}'.replace('{format}', 'json')
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
                                            response_type='Variable',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
