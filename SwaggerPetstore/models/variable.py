#!/usr/bin/env python
# coding: utf-8

"""
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
"""

class Variable(object):
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'name': 'str',
            
            
            'original_name': 'str',
            
            
            'category': 'str',
            
            
            'unit': 'str',
            
            
            'sources': 'str',
            
            
            'minimum_value': 'float',
            
            
            'maximum_value': 'float',
            
            
            'combination_operation': 'str',
            
            
            'filling_value': 'float'
            
        }

        self.attributeMap = {
            
            'name': 'name',
            
            'original_name': 'originalName',
            
            'category': 'category',
            
            'unit': 'unit',
            
            'sources': 'sources',
            
            'minimum_value': 'minimumValue',
            
            'maximum_value': 'maximumValue',
            
            'combination_operation': 'combinationOperation',
            
            'filling_value': 'fillingValue'
            
        }

        
        #User-defined variable display name.
        
        self.name = None # str
        
        #Name used when the variable was originally created in the `variables` table.
        
        self.original_name = None # str
        
        #Variable category like Mood, Sleep, Physical Activity, Treatment, Symptom, etc.
        
        self.category = None # str
        
        #Abbreviated name of the default unit for the variable
        
        self.unit = None # str
        
        #Comma-separated list of source names to limit variables to those sources
        
        self.sources = None # str
        
        #Minimum reasonable value for this variable (uses default unit)
        
        self.minimum_value = None # float
        
        #Maximum reasonable value for this variable (uses default unit)
        
        self.maximum_value = None # float
        
        #How to aggregate measurements over time.
        
        self.combination_operation = None # str
        
        #Value for replacing null measurements
        
        self.filling_value = None # float
        
