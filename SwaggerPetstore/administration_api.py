#!/usr/bin/env python
# coding: utf-8

"""
AdministrationApi.py
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


class AdministrationApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def administrationCacheClearGet(self, **kwargs):
        """getCacheClear

        Args:
            
        
        Returns: 
        """

        allParams = []

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method administrationCacheClearGet" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/administration/cache/clear'
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

        
        
        
    
    def administrationCorrelationsUpdateGet(self, **kwargs):
        """getCorrelationsUpdate

        Args:
            
            modified_variable, str: Original name of variable for which correlations are to be calculated (varchar) (required)
            
            
            user_id, int: ID for user for whom the correlations should be recalculated. (required)
            
            
        
        Returns: 
        """

        allParams = ['modified_variable', 'user_id']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method administrationCorrelationsUpdateGet" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/administration/correlations/update'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = ''

        
        if ('modified_variable' in params):
            queryParams['modifiedVariable'] = self.apiClient.toPathValue(params['modified_variable'])
        
        if ('user_id' in params):
            queryParams['userId'] = self.apiClient.toPathValue(params['user_id'])
        

        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        
        
    
    def administrationCorrelationsUpdateAllUsersGet(self, **kwargs):
        """getCorrelationsUpdateAllUsers

        Args:
            
        
        Returns: 
        """

        allParams = []

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method administrationCorrelationsUpdateAllUsersGet" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/administration/correlations/updateAllUsers'
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

        
        
        
    
    def administrationCorrelationsUpdateAllVariablesGet(self, **kwargs):
        """getCorrelationsUpdateAllVariables

        Args:
            
            user_id, int: ID for user for whom the correlations should be recalculated. If empty, uses currently logged in user. (required)
            
            
        
        Returns: 
        """

        allParams = ['user_id']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method administrationCorrelationsUpdateAllVariablesGet" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/administration/correlations/updateAllVariables'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = ''

        
        if ('user_id' in params):
            queryParams['userId'] = self.apiClient.toPathValue(params['user_id'])
        

        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        
        
    


