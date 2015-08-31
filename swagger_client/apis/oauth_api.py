# coding: utf-8

"""
OauthApi.py
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


class OauthApi(object):
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
                config.api_client = ApiClient('https://localhost/api')
            self.api_client = config.api_client

    def oauth2_accesstoken_get(self, client_id, client_secret, grant_type, **kwargs):
        """
        Access Token
        Client provides authorization token obtained from /api/oauth2/authorize to this endpoint and receives an access token. Access token can then be used to query different API endpoints of QuantiModo.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.oauth2_accesstoken_get(client_id, client_secret, grant_type, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str client_id: Client id (required)
        :param str client_secret: Client secret (required)
        :param str grant_type: Grant Type can be 'authorization_code' or 'refresh_token' (required)
        :param str response_type: Response type
        :param str scope: Scope
        :param str redirect_uri: Redirect uri
        :param str state: State
        :param str realm: Realm
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # verify the required parameter 'client_id' is set
        if client_id is None:
            raise ValueError("Missing the required parameter `client_id` when calling `oauth2_accesstoken_get`")
        # verify the required parameter 'client_secret' is set
        if client_secret is None:
            raise ValueError("Missing the required parameter `client_secret` when calling `oauth2_accesstoken_get`")
        # verify the required parameter 'grant_type' is set
        if grant_type is None:
            raise ValueError("Missing the required parameter `grant_type` when calling `oauth2_accesstoken_get`")

        all_params = ['client_id', 'client_secret', 'grant_type', 'response_type', 'scope', 'redirect_uri', 'state', 'realm']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method oauth2_accesstoken_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/oauth2/accesstoken'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}

        query_params = {}
        if 'client_id' in params:
            query_params['client_id'] = params['client_id']
        if 'client_secret' in params:
            query_params['client_secret'] = params['client_secret']
        if 'grant_type' in params:
            query_params['grant_type'] = params['grant_type']
        if 'response_type' in params:
            query_params['response_type'] = params['response_type']
        if 'scope' in params:
            query_params['scope'] = params['scope']
        if 'redirect_uri' in params:
            query_params['redirect_uri'] = params['redirect_uri']
        if 'state' in params:
            query_params['state'] = params['state']
        if 'realm' in params:
            query_params['realm'] = params['realm']

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

    def oauth2_authorize_get(self, client_id, client_secret, response_type, scope, **kwargs):
        """
        Authorize
        Ask the user if they want to allow a client applications to submit or obtain data from their QM account. It will redirect the user to the url provided by the client application with the code as a query parameter or error in case of an error.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.oauth2_authorize_get(client_id, client_secret, response_type, scope, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str client_id: This is the unique ID that QuantiModo uses to identify your application. Obtain a client id by emailing info@quantimo.do. (required)
        :param str client_secret: This is the secret for your obtained clietn_id. QuantiModo uses this to validate that only your application uses the client_id. (required)
        :param str response_type: If the value is code, launches a Basic flow, requiring a POST to the token endpoint to obtain the tokens. If the value is token id_token or id_token token, launches an Implicit flow, requiring the use of Javascript at the redirect URI to retrieve tokens from the URI #fragment. (required)
        :param str scope: Scopes include basic, readmeasurements, and writemeasurements. The \"basic\" scope allows you to read user info (displayname, email, etc). The \"readmeasurements\" scope allows one to read a user's data. The \"writemeasurements\" scope allows you to write user data. Separate multiple scopes by a space. (required)
        :param str redirect_uri: The redirect URI is the URL within your client application that will receive the OAuth2 credentials.
        :param str state: An opaque string that is round-tripped in the protocol; that is to say, it is returned as a URI parameter in the Basic flow, and in the URI
        :param str realm: Name of the realm representing the users of your distributed applications and services. A \"realm\" attribute MAY be included to indicate the scope of protection.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # verify the required parameter 'client_id' is set
        if client_id is None:
            raise ValueError("Missing the required parameter `client_id` when calling `oauth2_authorize_get`")
        # verify the required parameter 'client_secret' is set
        if client_secret is None:
            raise ValueError("Missing the required parameter `client_secret` when calling `oauth2_authorize_get`")
        # verify the required parameter 'response_type' is set
        if response_type is None:
            raise ValueError("Missing the required parameter `response_type` when calling `oauth2_authorize_get`")
        # verify the required parameter 'scope' is set
        if scope is None:
            raise ValueError("Missing the required parameter `scope` when calling `oauth2_authorize_get`")

        all_params = ['client_id', 'client_secret', 'response_type', 'scope', 'redirect_uri', 'state', 'realm']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method oauth2_authorize_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/oauth2/authorize'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}

        query_params = {}
        if 'client_id' in params:
            query_params['client_id'] = params['client_id']
        if 'client_secret' in params:
            query_params['client_secret'] = params['client_secret']
        if 'response_type' in params:
            query_params['response_type'] = params['response_type']
        if 'scope' in params:
            query_params['scope'] = params['scope']
        if 'redirect_uri' in params:
            query_params['redirect_uri'] = params['redirect_uri']
        if 'state' in params:
            query_params['state'] = params['state']
        if 'realm' in params:
            query_params['realm'] = params['realm']

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