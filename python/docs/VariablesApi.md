# swagger_client.VariablesApi

All URIs are relative to *https://app.quantimo.do/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_public_variables_get**](VariablesApi.md#v1_public_variables_get) | **GET** /v1/public/variables | Get public variables
[**v1_public_variables_search_search_get**](VariablesApi.md#v1_public_variables_search_search_get) | **GET** /v1/public/variables/search/{search} | Get top 5 PUBLIC variables with the most correlations
[**v1_user_variables_delete_post**](VariablesApi.md#v1_user_variables_delete_post) | **POST** /v1/userVariables/delete | Delete All Measurements For Variable
[**v1_user_variables_post**](VariablesApi.md#v1_user_variables_post) | **POST** /v1/userVariables | Update User Settings for a Variable
[**v1_user_variables_reset_post**](VariablesApi.md#v1_user_variables_reset_post) | **POST** /v1/userVariables/reset | Reset user settings for a variable to defaults
[**v1_variable_categories_get**](VariablesApi.md#v1_variable_categories_get) | **GET** /v1/variableCategories | Variable categories
[**v1_variables_get**](VariablesApi.md#v1_variables_get) | **GET** /v1/variables | Get variables with user&#39;s settings
[**v1_variables_post**](VariablesApi.md#v1_variables_post) | **POST** /v1/variables | Create Variables
[**v1_variables_search_search_get**](VariablesApi.md#v1_variables_search_search_get) | **GET** /v1/variables/search/{search} | Get variables by search query
[**v1_variables_variable_name_get**](VariablesApi.md#v1_variables_variable_name_get) | **GET** /v1/variables/{variableName} | Get info about a variable


# **v1_public_variables_get**
> Variable v1_public_variables_get(access_token=access_token, user_id=user_id, id=id, category=category, name=name, updated_at=updated_at, source=source, latest_measurement_time=latest_measurement_time, number_of_raw_measurements=number_of_raw_measurements, last_source=last_source, limit=limit, offset=offset, sort=sort)

Get public variables

This endpoint retrieves an array of all public variables. Public variables are things like foods, medications, symptoms, conditions, and anything not unique to a particular user. For instance, a telephone number or name would not be a public variable.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
swagger_client.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure OAuth2 access token for authorization: quantimodo_oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.VariablesApi()
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
user_id = 56 # int | User's id (optional)
id = 56 # int | Common variable id (optional)
category = 'category_example' # str | Filter data by category (optional)
name = 'name_example' # str | Original name of the variable (supports exact name match only) (optional)
updated_at = 'updated_at_example' # str | Filter by the last time any of the properties of the variable were changed. Uses UTC format \"YYYY-MM-DDThh:mm:ss\" (optional)
source = 'source_example' # str | The name of the data source that created the variable (supports exact name match only). So if you have a client application and you only want variables that were last updated by your app, you can include the name of your app here (optional)
latest_measurement_time = 'latest_measurement_time_example' # str | Filter variables based on the last time a measurement for them was created or updated in the UTC format \"YYYY-MM-DDThh:mm:ss\" (optional)
number_of_raw_measurements = 'number_of_raw_measurements_example' # str | Filter variables by the total number of measurements that they have. This could be used of you want to filter or sort by popularity. (optional)
last_source = 'last_source_example' # str | Limit variables to those which measurements were last submitted by a specific source. So if you have a client application and you only want variables that were last updated by your app, you can include the name of your app here. (supports exact name match only) (optional)
limit = 56 # int | The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. (optional)
offset = 56 # int | Since the maximum limit is 200 records, to get more than that you'll have to make multiple API calls and page through the results. To retrieve all the data, you can iterate through data by using the `limit` and `offset` query parameters.  For example, if you want to retrieve data from 61-80 then you can use a query with the following parameters, `imit=20&offset=60`. (optional)
sort = 56 # int | Sort by given field. If the field is prefixed with `-, it will sort in descending order. (optional)

try: 
    # Get public variables
    api_response = api_instance.v1_public_variables_get(access_token=access_token, user_id=user_id, id=id, category=category, name=name, updated_at=updated_at, source=source, latest_measurement_time=latest_measurement_time, number_of_raw_measurements=number_of_raw_measurements, last_source=last_source, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->v1_public_variables_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **user_id** | **int**| User&#39;s id | [optional] 
 **id** | **int**| Common variable id | [optional] 
 **category** | **str**| Filter data by category | [optional] 
 **name** | **str**| Original name of the variable (supports exact name match only) | [optional] 
 **updated_at** | **str**| Filter by the last time any of the properties of the variable were changed. Uses UTC format \&quot;YYYY-MM-DDThh:mm:ss\&quot; | [optional] 
 **source** | **str**| The name of the data source that created the variable (supports exact name match only). So if you have a client application and you only want variables that were last updated by your app, you can include the name of your app here | [optional] 
 **latest_measurement_time** | **str**| Filter variables based on the last time a measurement for them was created or updated in the UTC format \&quot;YYYY-MM-DDThh:mm:ss\&quot; | [optional] 
 **number_of_raw_measurements** | **str**| Filter variables by the total number of measurements that they have. This could be used of you want to filter or sort by popularity. | [optional] 
 **last_source** | **str**| Limit variables to those which measurements were last submitted by a specific source. So if you have a client application and you only want variables that were last updated by your app, you can include the name of your app here. (supports exact name match only) | [optional] 
 **limit** | **int**| The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. | [optional] 
 **offset** | **int**| Since the maximum limit is 200 records, to get more than that you&#39;ll have to make multiple API calls and page through the results. To retrieve all the data, you can iterate through data by using the &#x60;limit&#x60; and &#x60;offset&#x60; query parameters.  For example, if you want to retrieve data from 61-80 then you can use a query with the following parameters, &#x60;imit&#x3D;20&amp;offset&#x3D;60&#x60;. | [optional] 
 **sort** | **int**| Sort by given field. If the field is prefixed with &#x60;-, it will sort in descending order. | [optional] 

### Return type

[**Variable**](Variable.md)

### Authorization

[access_token](../README.md#access_token), [quantimodo_oauth2](../README.md#quantimodo_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_public_variables_search_search_get**
> Variable v1_public_variables_search_search_get(search, access_token=access_token, user_id=user_id, variable_category_name=variable_category_name, source=source, effect_or_cause=effect_or_cause, public_effect_or_cause=public_effect_or_cause, limit=limit, offset=offset, sort=sort)

Get top 5 PUBLIC variables with the most correlations

Get top 5 PUBLIC variables with the most correlations containing the entered search characters. For example, search for 'mood' as an effect. Since 'Overall Mood' has a lot of correlations with other variables, it should be in the autocomplete list.Supported filter parameters:<ul><li><b>category</b> - Category of Variable</li></ul>

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
swagger_client.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure OAuth2 access token for authorization: quantimodo_oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.VariablesApi()
search = 'search_example' # str | Search query can be some fraction of a variable name.
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
user_id = 56 # int | User's id (optional)
variable_category_name = 'variable_category_name_example' # str | Filter variables by category name. The variable categories include Activity, Causes of Illness, Cognitive Performance, Conditions, Environment, Foods, Location, Miscellaneous, Mood, Nutrition, Physical Activity, Physique, Sleep, Social Interactions, Symptoms, Treatments, Vital Signs, and Work. (optional)
source = 'source_example' # str | Specify a data source name to only return variables from a specific data source. (optional)
effect_or_cause = 'effect_or_cause_example' # str | Indicate if you only want variables that have user correlations. Possible values are effect and cause. (optional)
public_effect_or_cause = 'public_effect_or_cause_example' # str | Indicate if you only want variables that have aggregated correlations.  Possible values are effect and cause. (optional)
limit = 56 # int | The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. (optional)
offset = 56 # int | Since the maximum limit is 200 records, to get more than that you'll have to make multiple API calls and page through the results. To retrieve all the data, you can iterate through data by using the `limit` and `offset` query parameters.  For example, if you want to retrieve data from 61-80 then you can use a query with the following parameters, `imit=20&offset=60`. (optional)
sort = 56 # int | Sort by given field. If the field is prefixed with `-, it will sort in descending order. (optional)

try: 
    # Get top 5 PUBLIC variables with the most correlations
    api_response = api_instance.v1_public_variables_search_search_get(search, access_token=access_token, user_id=user_id, variable_category_name=variable_category_name, source=source, effect_or_cause=effect_or_cause, public_effect_or_cause=public_effect_or_cause, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->v1_public_variables_search_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search query can be some fraction of a variable name. | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **user_id** | **int**| User&#39;s id | [optional] 
 **variable_category_name** | **str**| Filter variables by category name. The variable categories include Activity, Causes of Illness, Cognitive Performance, Conditions, Environment, Foods, Location, Miscellaneous, Mood, Nutrition, Physical Activity, Physique, Sleep, Social Interactions, Symptoms, Treatments, Vital Signs, and Work. | [optional] 
 **source** | **str**| Specify a data source name to only return variables from a specific data source. | [optional] 
 **effect_or_cause** | **str**| Indicate if you only want variables that have user correlations. Possible values are effect and cause. | [optional] 
 **public_effect_or_cause** | **str**| Indicate if you only want variables that have aggregated correlations.  Possible values are effect and cause. | [optional] 
 **limit** | **int**| The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. | [optional] 
 **offset** | **int**| Since the maximum limit is 200 records, to get more than that you&#39;ll have to make multiple API calls and page through the results. To retrieve all the data, you can iterate through data by using the &#x60;limit&#x60; and &#x60;offset&#x60; query parameters.  For example, if you want to retrieve data from 61-80 then you can use a query with the following parameters, &#x60;imit&#x3D;20&amp;offset&#x3D;60&#x60;. | [optional] 
 **sort** | **int**| Sort by given field. If the field is prefixed with &#x60;-, it will sort in descending order. | [optional] 

### Return type

[**Variable**](Variable.md)

### Authorization

[access_token](../README.md#access_token), [quantimodo_oauth2](../README.md#quantimodo_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_user_variables_delete_post**
> v1_user_variables_delete_post(variable_id)

Delete All Measurements For Variable

Users can delete all of their measurements for a variable

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
swagger_client.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure OAuth2 access token for authorization: quantimodo_oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.VariablesApi()
variable_id = swagger_client.UserVariableDelete() # UserVariableDelete | Id of the variable whose measurements should be deleted

try: 
    # Delete All Measurements For Variable
    api_instance.v1_user_variables_delete_post(variable_id)
except ApiException as e:
    print("Exception when calling VariablesApi->v1_user_variables_delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_id** | [**UserVariableDelete**](UserVariableDelete.md)| Id of the variable whose measurements should be deleted | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token), [quantimodo_oauth2](../README.md#quantimodo_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_user_variables_post**
> v1_user_variables_post(user_variables)

Update User Settings for a Variable

Users can change the parameters used in analysis of that variable such as the expected duration of action for a variable to have an effect, the estimated delay before the onset of action. In order to filter out erroneous data, they are able to set the maximum and minimum reasonable daily values for a variable.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
swagger_client.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure OAuth2 access token for authorization: quantimodo_oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.VariablesApi()
user_variables = swagger_client.UserVariables() # UserVariables | Variable user settings data

try: 
    # Update User Settings for a Variable
    api_instance.v1_user_variables_post(user_variables)
except ApiException as e:
    print("Exception when calling VariablesApi->v1_user_variables_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_variables** | [**UserVariables**](UserVariables.md)| Variable user settings data | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token), [quantimodo_oauth2](../README.md#quantimodo_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_user_variables_reset_post**
> v1_user_variables_reset_post(variable_id)

Reset user settings for a variable to defaults

Reset user settings for a variable to defaults

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
swagger_client.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure OAuth2 access token for authorization: quantimodo_oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.VariablesApi()
variable_id = swagger_client.UserVariableDelete() # UserVariableDelete | Id of the variable that should be reset

try: 
    # Reset user settings for a variable to defaults
    api_instance.v1_user_variables_reset_post(variable_id)
except ApiException as e:
    print("Exception when calling VariablesApi->v1_user_variables_reset_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_id** | [**UserVariableDelete**](UserVariableDelete.md)| Id of the variable that should be reset | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token), [quantimodo_oauth2](../README.md#quantimodo_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_variable_categories_get**
> list[VariableCategory] v1_variable_categories_get()

Variable categories

The variable categories include Activity, Causes of Illness, Cognitive Performance, Conditions, Environment, Foods, Location, Miscellaneous, Mood, Nutrition, Physical Activity, Physique, Sleep, Social Interactions, Symptoms, Treatments, Vital Signs, and Work.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
swagger_client.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure OAuth2 access token for authorization: quantimodo_oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.VariablesApi()

try: 
    # Variable categories
    api_response = api_instance.v1_variable_categories_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->v1_variable_categories_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[VariableCategory]**](VariableCategory.md)

### Authorization

[access_token](../README.md#access_token), [quantimodo_oauth2](../README.md#quantimodo_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_variables_get**
> Variable v1_variables_get(access_token=access_token, user_id=user_id, id=id, category=category, name=name, updated_at=updated_at, source=source, latest_measurement_time=latest_measurement_time, number_of_raw_measurements=number_of_raw_measurements, last_source=last_source, limit=limit, offset=offset, sort=sort)

Get variables with user's settings

Get variables for which the user has measurements. If the user has specified variable settings, these are provided instead of the common variable defaults.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
swagger_client.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure OAuth2 access token for authorization: quantimodo_oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.VariablesApi()
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
user_id = 56 # int | User's id (optional)
id = 56 # int | Common variable id (optional)
category = 'category_example' # str | Filter data by category (optional)
name = 'name_example' # str | Original name of the variable (supports exact name match only) (optional)
updated_at = 'updated_at_example' # str | Filter by the last time any of the properties of the variable were changed. Uses UTC format \"YYYY-MM-DDThh:mm:ss\" (optional)
source = 'source_example' # str | The name of the data source that created the variable (supports exact name match only). So if you have a client application and you only want variables that were last updated by your app, you can include the name of your app here (optional)
latest_measurement_time = 'latest_measurement_time_example' # str | Filter variables based on the last time a measurement for them was created or updated in the UTC format \"YYYY-MM-DDThh:mm:ss\" (optional)
number_of_raw_measurements = 'number_of_raw_measurements_example' # str | Filter variables by the total number of measurements that they have. This could be used of you want to filter or sort by popularity. (optional)
last_source = 'last_source_example' # str | Limit variables to those which measurements were last submitted by a specific source. So if you have a client application and you only want variables that were last updated by your app, you can include the name of your app here. (supports exact name match only) (optional)
limit = 56 # int | The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. (optional)
offset = 56 # int | Since the maximum limit is 200 records, to get more than that you'll have to make multiple API calls and page through the results. To retrieve all the data, you can iterate through data by using the `limit` and `offset` query parameters.  For example, if you want to retrieve data from 61-80 then you can use a query with the following parameters, `imit=20&offset=60`. (optional)
sort = 56 # int | Sort by given field. If the field is prefixed with `-, it will sort in descending order. (optional)

try: 
    # Get variables with user's settings
    api_response = api_instance.v1_variables_get(access_token=access_token, user_id=user_id, id=id, category=category, name=name, updated_at=updated_at, source=source, latest_measurement_time=latest_measurement_time, number_of_raw_measurements=number_of_raw_measurements, last_source=last_source, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->v1_variables_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **user_id** | **int**| User&#39;s id | [optional] 
 **id** | **int**| Common variable id | [optional] 
 **category** | **str**| Filter data by category | [optional] 
 **name** | **str**| Original name of the variable (supports exact name match only) | [optional] 
 **updated_at** | **str**| Filter by the last time any of the properties of the variable were changed. Uses UTC format \&quot;YYYY-MM-DDThh:mm:ss\&quot; | [optional] 
 **source** | **str**| The name of the data source that created the variable (supports exact name match only). So if you have a client application and you only want variables that were last updated by your app, you can include the name of your app here | [optional] 
 **latest_measurement_time** | **str**| Filter variables based on the last time a measurement for them was created or updated in the UTC format \&quot;YYYY-MM-DDThh:mm:ss\&quot; | [optional] 
 **number_of_raw_measurements** | **str**| Filter variables by the total number of measurements that they have. This could be used of you want to filter or sort by popularity. | [optional] 
 **last_source** | **str**| Limit variables to those which measurements were last submitted by a specific source. So if you have a client application and you only want variables that were last updated by your app, you can include the name of your app here. (supports exact name match only) | [optional] 
 **limit** | **int**| The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. | [optional] 
 **offset** | **int**| Since the maximum limit is 200 records, to get more than that you&#39;ll have to make multiple API calls and page through the results. To retrieve all the data, you can iterate through data by using the &#x60;limit&#x60; and &#x60;offset&#x60; query parameters.  For example, if you want to retrieve data from 61-80 then you can use a query with the following parameters, &#x60;imit&#x3D;20&amp;offset&#x3D;60&#x60;. | [optional] 
 **sort** | **int**| Sort by given field. If the field is prefixed with &#x60;-, it will sort in descending order. | [optional] 

### Return type

[**Variable**](Variable.md)

### Authorization

[access_token](../README.md#access_token), [quantimodo_oauth2](../README.md#quantimodo_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_variables_post**
> v1_variables_post(body, access_token=access_token, user_id=user_id)

Create Variables

Allows the client to create a new variable in the `variables` table.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
swagger_client.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure OAuth2 access token for authorization: quantimodo_oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.VariablesApi()
body = swagger_client.VariablesNew() # VariablesNew | Original name for the variable.
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
user_id = 56 # int | User's id (optional)

try: 
    # Create Variables
    api_instance.v1_variables_post(body, access_token=access_token, user_id=user_id)
except ApiException as e:
    print("Exception when calling VariablesApi->v1_variables_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VariablesNew**](VariablesNew.md)| Original name for the variable. | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **user_id** | **int**| User&#39;s id | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token), [quantimodo_oauth2](../README.md#quantimodo_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_variables_search_search_get**
> list[Variable] v1_variables_search_search_get(search, access_token=access_token, user_id=user_id, variable_category_name=variable_category_name, include_public=include_public, manual_tracking=manual_tracking, source=source, effect_or_cause=effect_or_cause, public_effect_or_cause=public_effect_or_cause, limit=limit, offset=offset)

Get variables by search query

Get variables containing the search characters for which the currently logged in user has measurements. Used to provide auto-complete function in variable search boxes.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
swagger_client.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure OAuth2 access token for authorization: quantimodo_oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.VariablesApi()
search = 'search_example' # str | Search query which may be an entire variable name or a fragment of one.
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
user_id = 56 # int | User's id (optional)
variable_category_name = 'variable_category_name_example' # str | Filter variables by category name. The variable categories include Activity, Causes of Illness, Cognitive Performance, Conditions, Environment, Foods, Location, Miscellaneous, Mood, Nutrition, Physical Activity, Physique, Sleep, Social Interactions, Symptoms, Treatments, Vital Signs, and Work. (optional)
include_public = true # bool | Set to true if you would like to include public variables when no user variables are found. (optional)
manual_tracking = true # bool | Set to true if you would like to exlude variables like apps and website names. (optional)
source = 'source_example' # str | Specify a data source name to only return variables from a specific data source. (optional)
effect_or_cause = 'effect_or_cause_example' # str | Indicate if you only want variables that have user correlations. Possible values are effect and cause. (optional)
public_effect_or_cause = 'public_effect_or_cause_example' # str | Indicate if you only want variables that have aggregated correlations.  Possible values are effect and cause. (optional)
limit = 56 # int | The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. (optional)
offset = 56 # int | Since the maximum limit is 200 records, to get more than that you'll have to make multiple API calls and page through the results. To retrieve all the data, you can iterate through data by using the `limit` and `offset` query parameters.  For example, if you want to retrieve data from 61-80 then you can use a query with the following parameters, `imit=20&offset=60`. (optional)

try: 
    # Get variables by search query
    api_response = api_instance.v1_variables_search_search_get(search, access_token=access_token, user_id=user_id, variable_category_name=variable_category_name, include_public=include_public, manual_tracking=manual_tracking, source=source, effect_or_cause=effect_or_cause, public_effect_or_cause=public_effect_or_cause, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->v1_variables_search_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search query which may be an entire variable name or a fragment of one. | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **user_id** | **int**| User&#39;s id | [optional] 
 **variable_category_name** | **str**| Filter variables by category name. The variable categories include Activity, Causes of Illness, Cognitive Performance, Conditions, Environment, Foods, Location, Miscellaneous, Mood, Nutrition, Physical Activity, Physique, Sleep, Social Interactions, Symptoms, Treatments, Vital Signs, and Work. | [optional] 
 **include_public** | **bool**| Set to true if you would like to include public variables when no user variables are found. | [optional] 
 **manual_tracking** | **bool**| Set to true if you would like to exlude variables like apps and website names. | [optional] 
 **source** | **str**| Specify a data source name to only return variables from a specific data source. | [optional] 
 **effect_or_cause** | **str**| Indicate if you only want variables that have user correlations. Possible values are effect and cause. | [optional] 
 **public_effect_or_cause** | **str**| Indicate if you only want variables that have aggregated correlations.  Possible values are effect and cause. | [optional] 
 **limit** | **int**| The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. | [optional] 
 **offset** | **int**| Since the maximum limit is 200 records, to get more than that you&#39;ll have to make multiple API calls and page through the results. To retrieve all the data, you can iterate through data by using the &#x60;limit&#x60; and &#x60;offset&#x60; query parameters.  For example, if you want to retrieve data from 61-80 then you can use a query with the following parameters, &#x60;imit&#x3D;20&amp;offset&#x3D;60&#x60;. | [optional] 

### Return type

[**list[Variable]**](Variable.md)

### Authorization

[access_token](../README.md#access_token), [quantimodo_oauth2](../README.md#quantimodo_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_variables_variable_name_get**
> Variable v1_variables_variable_name_get(variable_name, access_token=access_token, user_id=user_id)

Get info about a variable

Get all of the settings and information about a variable by its name. If the logged in user has modified the settings for the variable, these will be provided instead of the default settings for that variable.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
swagger_client.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure OAuth2 access token for authorization: quantimodo_oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.VariablesApi()
variable_name = 'variable_name_example' # str | Variable name
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
user_id = 56 # int | User's id (optional)

try: 
    # Get info about a variable
    api_response = api_instance.v1_variables_variable_name_get(variable_name, access_token=access_token, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->v1_variables_variable_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_name** | **str**| Variable name | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **user_id** | **int**| User&#39;s id | [optional] 

### Return type

[**Variable**](Variable.md)

### Authorization

[access_token](../README.md#access_token), [quantimodo_oauth2](../README.md#quantimodo_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

