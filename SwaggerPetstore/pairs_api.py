#!/usr/bin/env python
# coding: utf-8

"""
PairsApi.py
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


class PairsApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def pairsGet(self, **kwargs):
        """Get pairs

        Args:
            
            cause, str: Original variable name for the explanatory or independent variable (required)
            
            
            effect, str: Original variable name for the outcome or dependent variable (required)
            
            
            duration, str: Duration of action (in seconds) from the cause variable settings. (required)
            
            
            delay, str: Delay before onset of action (in seconds) from the cause variable settings. (required)
            
            
            start_time, str: The earliest date (in epoch time) for which we should return measurements (required)
            
            
            end_time, str: The most recent date (in epoch time) for which we should return measurements (required)
            
            
            cause_source, str: Name of data source that the cause measurements should come from (required)
            
            
            effect_source, str: Name of data source that the effectmeasurements should come from (required)
            
            
            cause_unit, str: Abbreviated name for the unit cause measurements to be returned in (required)
            
            
            effect_unit, str: Abbreviated name for the unit effect measurements to be returned in (required)
            
            
        
        Returns: 
        """

        allParams = ['cause', 'effect', 'duration', 'delay', 'start_time', 'end_time', 'cause_source', 'effect_source', 'cause_unit', 'effect_unit']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method pairsGet" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pairs'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = ''

        
        if ('cause' in params):
            queryParams['cause'] = self.apiClient.toPathValue(params['cause'])
        
        if ('effect' in params):
            queryParams['effect'] = self.apiClient.toPathValue(params['effect'])
        
        if ('duration' in params):
            queryParams['duration'] = self.apiClient.toPathValue(params['duration'])
        
        if ('delay' in params):
            queryParams['delay'] = self.apiClient.toPathValue(params['delay'])
        
        if ('start_time' in params):
            queryParams['startTime'] = self.apiClient.toPathValue(params['start_time'])
        
        if ('end_time' in params):
            queryParams['endTime'] = self.apiClient.toPathValue(params['end_time'])
        
        if ('cause_source' in params):
            queryParams['causeSource'] = self.apiClient.toPathValue(params['cause_source'])
        
        if ('effect_source' in params):
            queryParams['effectSource'] = self.apiClient.toPathValue(params['effect_source'])
        
        if ('cause_unit' in params):
            queryParams['causeUnit'] = self.apiClient.toPathValue(params['cause_unit'])
        
        if ('effect_unit' in params):
            queryParams['effectUnit'] = self.apiClient.toPathValue(params['effect_unit'])
        

        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        
        
    

