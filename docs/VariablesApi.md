# swagger_client.VariablesApi

All URIs are relative to *https://app.quantimo.do/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_public_variables_get**](VariablesApi.md#v1_public_variables_get) | **GET** /v1/public/variables | Get public variables
[**v1_public_variables_search_search_get**](VariablesApi.md#v1_public_variables_search_search_get) | **GET** /v1/public/variables/search/{search} | Get top 5 PUBLIC variables with the most correlations
[**v1_user_variables_post**](VariablesApi.md#v1_user_variables_post) | **POST** /v1/userVariables | Update User Settings for a Variable
[**v1_variable_categories_get**](VariablesApi.md#v1_variable_categories_get) | **GET** /v1/variableCategories | Variable categories
[**v1_variables_get**](VariablesApi.md#v1_variables_get) | **GET** /v1/variables | Get variables by the category name
[**v1_variables_post**](VariablesApi.md#v1_variables_post) | **POST** /v1/variables | Create Variables
[**v1_variables_search_search_get**](VariablesApi.md#v1_variables_search_search_get) | **GET** /v1/variables/search/{search} | Get variables by search query
[**v1_variables_variable_name_get**](VariablesApi.md#v1_variables_variable_name_get) | **GET** /v1/variables/{variableName} | Get info about a variable


# **v1_public_variables_get**
> Variable v1_public_variables_get()

Get public variables

This endpoint retrieves an array of all public variables. Public variables are things like foods, medications, symptoms, conditions, and anything not unique to a particular user. For instance, a telephone number or name would not be a public variable.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.VariablesApi()

try: 
    # Get public variables
    api_response = api_instance.v1_public_variables_get()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VariablesApi->v1_public_variables_get: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Variable**](Variable.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_public_variables_search_search_get**
> Variable v1_public_variables_search_search_get(search, access_token=access_token, category_name=category_name, source=source, effect_or_cause=effect_or_cause, public_effect_or_cause=public_effect_or_cause, limit=limit, offset=offset, sort=sort)

Get top 5 PUBLIC variables with the most correlations

Get top 5 PUBLIC variables with the most correlations containing the entered search characters. For example, search for 'mood' as an effect. Since 'Overall Mood' has a lot of correlations with other variables, it should be in the autocomplete list.<br>Supported filter parameters:<br><ul><li><b>category</b> - Category of Variable</li></ul><br>

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.VariablesApi()
search = 'search_example' # str | Search query can be some fraction of a variable name.
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
category_name = 'category_name_example' # str | Filter variables by category name. The variable categories include Activity, Causes of Illness, Cognitive Performance, Conditions, Environment, Foods, Location, Miscellaneous, Mood, Nutrition, Physical Activity, Physique, Sleep, Social Interactions, Symptoms, Treatments, Vital Signs, and Work. (optional)
source = 'source_example' # str | Specify a data source name to only return variables from a specific data source. (optional)
effect_or_cause = 'effect_or_cause_example' # str | Indicate if you only want variables that have user correlations.  Possible values are effect and cause. (optional)
public_effect_or_cause = 'public_effect_or_cause_example' # str | Indicate if you only want variables that have aggregated correlations.  Possible values are effect and cause. (optional)
limit = 56 # int | The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. (optional)
offset = 56 # int | Now suppose you wanted to show results 11-20. You'd set the offset to 10 and the limit to 10. (optional)
sort = 56 # int | Sort by given field. If the field is prefixed with `-, it will sort in descending order. (optional)

try: 
    # Get top 5 PUBLIC variables with the most correlations
    api_response = api_instance.v1_public_variables_search_search_get(search, access_token=access_token, category_name=category_name, source=source, effect_or_cause=effect_or_cause, public_effect_or_cause=public_effect_or_cause, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VariablesApi->v1_public_variables_search_search_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search query can be some fraction of a variable name. | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **category_name** | **str**| Filter variables by category name. The variable categories include Activity, Causes of Illness, Cognitive Performance, Conditions, Environment, Foods, Location, Miscellaneous, Mood, Nutrition, Physical Activity, Physique, Sleep, Social Interactions, Symptoms, Treatments, Vital Signs, and Work. | [optional] 
 **source** | **str**| Specify a data source name to only return variables from a specific data source. | [optional] 
 **effect_or_cause** | **str**| Indicate if you only want variables that have user correlations.  Possible values are effect and cause. | [optional] 
 **public_effect_or_cause** | **str**| Indicate if you only want variables that have aggregated correlations.  Possible values are effect and cause. | [optional] 
 **limit** | **int**| The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. | [optional] 
 **offset** | **int**| Now suppose you wanted to show results 11-20. You&#39;d set the offset to 10 and the limit to 10. | [optional] 
 **sort** | **int**| Sort by given field. If the field is prefixed with &#x60;-, it will sort in descending order. | [optional] 

### Return type

[**Variable**](Variable.md)

### Authorization

[oauth2](../README.md#oauth2)

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
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.VariablesApi()
user_variables = swagger_client.UserVariables() # UserVariables | Variable user settings data

try: 
    # Update User Settings for a Variable
    api_instance.v1_user_variables_post(user_variables)
except ApiException as e:
    print "Exception when calling VariablesApi->v1_user_variables_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_variables** | [**UserVariables**](UserVariables.md)| Variable user settings data | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

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
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.VariablesApi()

try: 
    # Variable categories
    api_response = api_instance.v1_variable_categories_get()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VariablesApi->v1_variable_categories_get: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[VariableCategory]**](VariableCategory.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_variables_get**
> Variable v1_variables_get(access_token=access_token, id=id, user_id=user_id, category=category, name=name, last_updated=last_updated, source=source, latest_measurement_time=latest_measurement_time, number_of_measurements=number_of_measurements, last_source=last_source, limit=limit, offset=offset, sort=sort)

Get variables by the category name

Get variables by the category name. <br>Supported filter parameters:<br><ul><li><b>name</b> - Original name of the variable (supports exact name match only)</li><li><b>lastUpdated</b> - Filter by the last time any of the properties of the variable were changed. Uses UTC format \"YYYY-MM-DDThh:mm:ss\"</li><li><b>source</b> - The name of the data source that created the variable (supports exact name match only). So if you have a client application and you only want variables that were last updated by your app, you can include the name of your app here</li><li><b>latestMeasurementTime</b> - Filter variables based on the last time a measurement for them was created or updated in the UTC format \"YYYY-MM-DDThh:mm:ss\"</li><li><b>numberOfMeasurements</b> - Filter variables by the total number of measurements that they have. This could be used of you want to filter or sort by popularity.</li><li><b>lastSource</b> - Limit variables to those which measurements were last submitted by a specific source. So if you have a client application and you only want variables that were last updated by your app, you can include the name of your app here. (supports exact name match only)</li></ul><br>

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure HTTP basic authorization: basicAuth
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.VariablesApi()
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
id = 56 # int | Common variable id (optional)
user_id = 56 # int | User id (optional)
category = 'category_example' # str | Filter data by category (optional)
name = 'name_example' # str | Original name of the variable (supports exact name match only) (optional)
last_updated = 'last_updated_example' # str | Filter by the last time any of the properties of the variable were changed. Uses UTC format \"YYYY-MM-DDThh:mm:ss\" (optional)
source = 'source_example' # str | The name of the data source that created the variable (supports exact name match only). So if you have a client application and you only want variables that were last updated by your app, you can include the name of your app here (optional)
latest_measurement_time = 'latest_measurement_time_example' # str | Filter variables based on the last time a measurement for them was created or updated in the UTC format \"YYYY-MM-DDThh:mm:ss\" (optional)
number_of_measurements = 'number_of_measurements_example' # str | Filter variables by the total number of measurements that they have. This could be used of you want to filter or sort by popularity. (optional)
last_source = 'last_source_example' # str | Limit variables to those which measurements were last submitted by a specific source. So if you have a client application and you only want variables that were last updated by your app, you can include the name of your app here. (supports exact name match only) (optional)
limit = 56 # int | The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. (optional)
offset = 56 # int | Now suppose you wanted to show results 11-20. You'd set the offset to 10 and the limit to 10. (optional)
sort = 56 # int | Sort by given field. If the field is prefixed with `-, it will sort in descending order. (optional)

try: 
    # Get variables by the category name
    api_response = api_instance.v1_variables_get(access_token=access_token, id=id, user_id=user_id, category=category, name=name, last_updated=last_updated, source=source, latest_measurement_time=latest_measurement_time, number_of_measurements=number_of_measurements, last_source=last_source, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VariablesApi->v1_variables_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **id** | **int**| Common variable id | [optional] 
 **user_id** | **int**| User id | [optional] 
 **category** | **str**| Filter data by category | [optional] 
 **name** | **str**| Original name of the variable (supports exact name match only) | [optional] 
 **last_updated** | **str**| Filter by the last time any of the properties of the variable were changed. Uses UTC format \&quot;YYYY-MM-DDThh:mm:ss\&quot; | [optional] 
 **source** | **str**| The name of the data source that created the variable (supports exact name match only). So if you have a client application and you only want variables that were last updated by your app, you can include the name of your app here | [optional] 
 **latest_measurement_time** | **str**| Filter variables based on the last time a measurement for them was created or updated in the UTC format \&quot;YYYY-MM-DDThh:mm:ss\&quot; | [optional] 
 **number_of_measurements** | **str**| Filter variables by the total number of measurements that they have. This could be used of you want to filter or sort by popularity. | [optional] 
 **last_source** | **str**| Limit variables to those which measurements were last submitted by a specific source. So if you have a client application and you only want variables that were last updated by your app, you can include the name of your app here. (supports exact name match only) | [optional] 
 **limit** | **int**| The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. | [optional] 
 **offset** | **int**| Now suppose you wanted to show results 11-20. You&#39;d set the offset to 10 and the limit to 10. | [optional] 
 **sort** | **int**| Sort by given field. If the field is prefixed with &#x60;-, it will sort in descending order. | [optional] 

### Return type

[**Variable**](Variable.md)

### Authorization

[oauth2](../README.md#oauth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_variables_post**
> v1_variables_post(body, access_token=access_token)

Create Variables

Allows the client to create a new variable in the `variables` table.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.VariablesApi()
body = swagger_client.VariablesNew() # VariablesNew | Original name for the variable.
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)

try: 
    # Create Variables
    api_instance.v1_variables_post(body, access_token=access_token)
except ApiException as e:
    print "Exception when calling VariablesApi->v1_variables_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VariablesNew**](VariablesNew.md)| Original name for the variable. | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_variables_search_search_get**
> list[Variable] v1_variables_search_search_get(search, access_token=access_token, category_name=category_name, include_public=include_public, manual_tracking=manual_tracking, source=source, effect_or_cause=effect_or_cause, public_effect_or_cause=public_effect_or_cause, limit=limit, offset=offset)

Get variables by search query

Get variables containing the search characters for which the currently logged in user has measurements. Used to provide auto-complete function in variable search boxes.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.VariablesApi()
search = 'search_example' # str | Search query which may be an entire variable name or a fragment of one.
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
category_name = 'category_name_example' # str | Filter variables by category name. The variable categories include Activity, Causes of Illness, Cognitive Performance, Conditions, Environment, Foods, Location, Miscellaneous, Mood, Nutrition, Physical Activity, Physique, Sleep, Social Interactions, Symptoms, Treatments, Vital Signs, and Work. (optional)
include_public = true # bool | Set to true if you would like to include public variables when no user variables are found. (optional)
manual_tracking = true # bool | Set to true if you would like to exlude variables like apps and website names. (optional)
source = 'source_example' # str | Specify a data source name to only return variables from a specific data source. (optional)
effect_or_cause = 'effect_or_cause_example' # str | Indicate if you only want variables that have user correlations.  Possible values are effect and cause. (optional)
public_effect_or_cause = 'public_effect_or_cause_example' # str | Indicate if you only want variables that have aggregated correlations.  Possible values are effect and cause. (optional)
limit = 56 # int | The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. (optional)
offset = 56 # int | Now suppose you wanted to show results 11-20. You'd set the offset to 10 and the limit to 10. (optional)

try: 
    # Get variables by search query
    api_response = api_instance.v1_variables_search_search_get(search, access_token=access_token, category_name=category_name, include_public=include_public, manual_tracking=manual_tracking, source=source, effect_or_cause=effect_or_cause, public_effect_or_cause=public_effect_or_cause, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VariablesApi->v1_variables_search_search_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search query which may be an entire variable name or a fragment of one. | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **category_name** | **str**| Filter variables by category name. The variable categories include Activity, Causes of Illness, Cognitive Performance, Conditions, Environment, Foods, Location, Miscellaneous, Mood, Nutrition, Physical Activity, Physique, Sleep, Social Interactions, Symptoms, Treatments, Vital Signs, and Work. | [optional] 
 **include_public** | **bool**| Set to true if you would like to include public variables when no user variables are found. | [optional] 
 **manual_tracking** | **bool**| Set to true if you would like to exlude variables like apps and website names. | [optional] 
 **source** | **str**| Specify a data source name to only return variables from a specific data source. | [optional] 
 **effect_or_cause** | **str**| Indicate if you only want variables that have user correlations.  Possible values are effect and cause. | [optional] 
 **public_effect_or_cause** | **str**| Indicate if you only want variables that have aggregated correlations.  Possible values are effect and cause. | [optional] 
 **limit** | **int**| The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. | [optional] 
 **offset** | **int**| Now suppose you wanted to show results 11-20. You&#39;d set the offset to 10 and the limit to 10. | [optional] 

### Return type

[**list[Variable]**](Variable.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_variables_variable_name_get**
> Variable v1_variables_variable_name_get(variable_name, access_token=access_token)

Get info about a variable

Get all of the settings and information about a variable by its name. If the logged in user has modified the settings for the variable, these will be provided instead of the default settings for that variable.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.VariablesApi()
variable_name = 'variable_name_example' # str | Variable name
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)

try: 
    # Get info about a variable
    api_response = api_instance.v1_variables_variable_name_get(variable_name, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VariablesApi->v1_variables_variable_name_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_name** | **str**| Variable name | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 

### Return type

[**Variable**](Variable.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

