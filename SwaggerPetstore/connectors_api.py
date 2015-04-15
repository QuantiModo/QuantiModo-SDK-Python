#!/usr/bin/env python
# coding: utf-8

"""
ConnectorsApi.py
Copyright 2015 Reverb Technologies, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
"""
import sys
import os
import urllib

from models import *


class ConnectorsApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def connectorsListGet(self, **kwargs):
        """List of Connectors

        Args:
            
        
        Returns: list[Connector]
        """

        allParams = []

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method connectorsListGet" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/connectors/list'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = ''

        

        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'list[Connector]')
        return responseObject
        
        
        
    
    def connectorsConnectorConnectGet(self, **kwargs):
        """Obtain a token from 3rd party data source

        Args:
            
            connector, str: Lowercase system name of the source application or device (required)
            
            
        
        Returns: 
        """

        allParams = ['connector']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method connectorsConnectorConnectGet" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/connectors/{connector}/connect'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = ''

        

        

        
        if ('connector' in params):
            replacement = str(self.apiClient.toPathValue(params['connector']))
            replacement = urllib.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'connector' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        
        
    
    def connectorsConnectorConnectInstructionsGet(self, **kwargs):
        """Get connection parameters

        Args:
            
            connector, str: Lowercase system name of the source application or device (required)
            
            
        
        Returns: 
        """

        allParams = ['connector']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method connectorsConnectorConnectInstructionsGet" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/connectors/{connector}/connectInstructions'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = ''

        

        

        
        if ('connector' in params):
            replacement = str(self.apiClient.toPathValue(params['connector']))
            replacement = urllib.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'connector' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        
        
    
    def connectorsConnectorDisconnectGet(self, **kwargs):
        """Delete stored connection info

        Args:
            
            connector, str: Lowercase system name of the source application or device (required)
            
            
        
        Returns: 
        """

        allParams = ['connector']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method connectorsConnectorDisconnectGet" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/connectors/{connector}/disconnect'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = ''

        

        

        
        if ('connector' in params):
            replacement = str(self.apiClient.toPathValue(params['connector']))
            replacement = urllib.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'connector' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        
        
    
    def connectorsConnectorInfoGet(self, **kwargs):
        """Get connector info for user

        Args:
            
            connector, str: Lowercase system name of the source application or device (required)
            
            
        
        Returns: 
        """

        allParams = ['connector']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method connectorsConnectorInfoGet" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/connectors/{connector}/info'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = ''

        

        

        
        if ('connector' in params):
            replacement = str(self.apiClient.toPathValue(params['connector']))
            replacement = urllib.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'connector' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        
        
    
    def connectorsConnectorUpdateGet(self, **kwargs):
        """Sync with data source

        Args:
            
            connector, str: Lowercase system name of the source application or device (required)
            
            
        
        Returns: 
        """

        allParams = ['connector']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method connectorsConnectorUpdateGet" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/connectors/{connector}/update'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = ''

        

        

        
        if ('connector' in params):
            replacement = str(self.apiClient.toPathValue(params['connector']))
            replacement = urllib.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'connector' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        
        
    


