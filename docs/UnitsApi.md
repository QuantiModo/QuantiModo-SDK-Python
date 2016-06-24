# swagger_client.UnitsApi

All URIs are relative to *https://app.quantimo.do/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_unit_categories_get**](UnitsApi.md#v1_unit_categories_get) | **GET** /v1/unitCategories | Get unit categories
[**v1_units_get**](UnitsApi.md#v1_units_get) | **GET** /v1/units | Get all available units
[**v1_units_variable_get**](UnitsApi.md#v1_units_variable_get) | **GET** /v1/unitsVariable | Units for Variable


# **v1_unit_categories_get**
> UnitCategory v1_unit_categories_get()

Get unit categories

Get a list of the categories of measurement units such as 'Distance', 'Duration', 'Energy', 'Frequency', 'Miscellany', 'Pressure', 'Proportion', 'Rating', 'Temperature', 'Volume', and 'Weight'.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UnitsApi()

try: 
    # Get unit categories
    api_response = api_instance.v1_unit_categories_get()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UnitsApi->v1_unit_categories_get: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UnitCategory**](UnitCategory.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_units_get**
> list[Unit] v1_units_get(access_token=access_token, id=id, unit_name=unit_name, abbreviated_unit_name=abbreviated_unit_name, category_name=category_name)

Get all available units

Get all available units

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UnitsApi()
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
id = 56 # int | Unit id (optional)
unit_name = 'unit_name_example' # str | Unit name (optional)
abbreviated_unit_name = 'abbreviated_unit_name_example' # str | Restrict the results to a specific unit by providing the unit abbreviation. (optional)
category_name = 'category_name_example' # str | Restrict the results to a specific unit category by providing the unit category name. (optional)

try: 
    # Get all available units
    api_response = api_instance.v1_units_get(access_token=access_token, id=id, unit_name=unit_name, abbreviated_unit_name=abbreviated_unit_name, category_name=category_name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UnitsApi->v1_units_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **id** | **int**| Unit id | [optional] 
 **unit_name** | **str**| Unit name | [optional] 
 **abbreviated_unit_name** | **str**| Restrict the results to a specific unit by providing the unit abbreviation. | [optional] 
 **category_name** | **str**| Restrict the results to a specific unit category by providing the unit category name. | [optional] 

### Return type

[**list[Unit]**](Unit.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_units_variable_get**
> list[Unit] v1_units_variable_get(access_token=access_token, unit_name=unit_name, abbreviated_unit_name=abbreviated_unit_name, category_name=category_name, variable=variable)

Units for Variable

Get a list of all possible units to use for a given variable

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UnitsApi()
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
unit_name = 'unit_name_example' # str | Name of Unit you want to retrieve (optional)
abbreviated_unit_name = 'abbreviated_unit_name_example' # str | Abbreviated Unit Name of the unit you want (optional)
category_name = 'category_name_example' # str | Name of the category you want units for (optional)
variable = 'variable_example' # str | Name of the variable you want units for (optional)

try: 
    # Units for Variable
    api_response = api_instance.v1_units_variable_get(access_token=access_token, unit_name=unit_name, abbreviated_unit_name=abbreviated_unit_name, category_name=category_name, variable=variable)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UnitsApi->v1_units_variable_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **unit_name** | **str**| Name of Unit you want to retrieve | [optional] 
 **abbreviated_unit_name** | **str**| Abbreviated Unit Name of the unit you want | [optional] 
 **category_name** | **str**| Name of the category you want units for | [optional] 
 **variable** | **str**| Name of the variable you want units for | [optional] 

### Return type

[**list[Unit]**](Unit.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

