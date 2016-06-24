# swagger_client.CorrelationsApi

All URIs are relative to *https://app.quantimo.do/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_aggregated_correlations_get**](CorrelationsApi.md#v1_aggregated_correlations_get) | **GET** /v1/aggregatedCorrelations | Get aggregated correlations
[**v1_aggregated_correlations_post**](CorrelationsApi.md#v1_aggregated_correlations_post) | **POST** /v1/aggregatedCorrelations | Store or Update a Correlation
[**v1_correlations_get**](CorrelationsApi.md#v1_correlations_get) | **GET** /v1/correlations | Get correlations
[**v1_organizations_organization_id_users_user_id_variables_variable_name_causes_get**](CorrelationsApi.md#v1_organizations_organization_id_users_user_id_variables_variable_name_causes_get) | **GET** /v1/organizations/{organizationId}/users/{userId}/variables/{variableName}/causes | Search user correlations for a given cause
[**v1_organizations_organization_id_users_user_id_variables_variable_name_effects_get**](CorrelationsApi.md#v1_organizations_organization_id_users_user_id_variables_variable_name_effects_get) | **GET** /v1/organizations/{organizationId}/users/{userId}/variables/{variableName}/effects | Search user correlations for a given cause
[**v1_public_correlations_search_search_get**](CorrelationsApi.md#v1_public_correlations_search_search_get) | **GET** /v1/public/correlations/search/{search} | Get average correlations for variables containing search term
[**v1_variables_variable_name_causes_get**](CorrelationsApi.md#v1_variables_variable_name_causes_get) | **GET** /v1/variables/{variableName}/causes | Search user correlations for a given effect
[**v1_variables_variable_name_effects_get**](CorrelationsApi.md#v1_variables_variable_name_effects_get) | **GET** /v1/variables/{variableName}/effects | Search user correlations for a given cause
[**v1_variables_variable_name_public_causes_get**](CorrelationsApi.md#v1_variables_variable_name_public_causes_get) | **GET** /v1/variables/{variableName}/public/causes | Search public correlations for a given effect
[**v1_variables_variable_name_public_effects_get**](CorrelationsApi.md#v1_variables_variable_name_public_effects_get) | **GET** /v1/variables/{variableName}/public/effects | Search public correlations for a given cause
[**v1_votes_delete_post**](CorrelationsApi.md#v1_votes_delete_post) | **POST** /v1/votes/delete | Delete vote
[**v1_votes_post**](CorrelationsApi.md#v1_votes_post) | **POST** /v1/votes | Post or update vote


# **v1_aggregated_correlations_get**
> list[Correlation] v1_aggregated_correlations_get(access_token=access_token, effect=effect, cause=cause, correlation_coefficient=correlation_coefficient, onset_delay=onset_delay, duration_of_action=duration_of_action, last_updated=last_updated, limit=limit, offset=offset, sort=sort)

Get aggregated correlations

Get correlations based on the anonymized aggregate data from all QuantiModo users.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CorrelationsApi()
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
effect = 'effect_example' # str | ORIGINAL variable name of the effect variable for which the user desires correlations (optional)
cause = 'cause_example' # str | ORIGINAL variable name of the cause variable for which the user desires correlations (optional)
correlation_coefficient = 'correlation_coefficient_example' # str | Pearson correlation coefficient between cause and effect after lagging by onset delay and grouping by duration of action (optional)
onset_delay = 'onset_delay_example' # str | The number of seconds which pass following a cause measurement before an effect would likely be observed. (optional)
duration_of_action = 'duration_of_action_example' # str | The time in seconds over which the cause would be expected to exert a measurable effect. We have selected a default value for each variable. This default value may be replaced by a user specified by adjusting their variable user settings. (optional)
last_updated = 'last_updated_example' # str | The time that this measurement was last updated in the UTC format \"YYYY-MM-DDThh:mm:ss\" (optional)
limit = 56 # int | The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. (optional)
offset = 56 # int | Now suppose you wanted to show results 11-20. You'd set the offset to 10 and the limit to 10. (optional)
sort = 56 # int | Sort by given field. If the field is prefixed with `-, it will sort in descending order. (optional)

try: 
    # Get aggregated correlations
    api_response = api_instance.v1_aggregated_correlations_get(access_token=access_token, effect=effect, cause=cause, correlation_coefficient=correlation_coefficient, onset_delay=onset_delay, duration_of_action=duration_of_action, last_updated=last_updated, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CorrelationsApi->v1_aggregated_correlations_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **effect** | **str**| ORIGINAL variable name of the effect variable for which the user desires correlations | [optional] 
 **cause** | **str**| ORIGINAL variable name of the cause variable for which the user desires correlations | [optional] 
 **correlation_coefficient** | **str**| Pearson correlation coefficient between cause and effect after lagging by onset delay and grouping by duration of action | [optional] 
 **onset_delay** | **str**| The number of seconds which pass following a cause measurement before an effect would likely be observed. | [optional] 
 **duration_of_action** | **str**| The time in seconds over which the cause would be expected to exert a measurable effect. We have selected a default value for each variable. This default value may be replaced by a user specified by adjusting their variable user settings. | [optional] 
 **last_updated** | **str**| The time that this measurement was last updated in the UTC format \&quot;YYYY-MM-DDThh:mm:ss\&quot; | [optional] 
 **limit** | **int**| The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. | [optional] 
 **offset** | **int**| Now suppose you wanted to show results 11-20. You&#39;d set the offset to 10 and the limit to 10. | [optional] 
 **sort** | **int**| Sort by given field. If the field is prefixed with &#x60;-, it will sort in descending order. | [optional] 

### Return type

[**list[Correlation]**](Correlation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_aggregated_correlations_post**
> v1_aggregated_correlations_post(body, access_token=access_token)

Store or Update a Correlation

Add correlation

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CorrelationsApi()
body = swagger_client.PostCorrelation() # PostCorrelation | Provides correlation data
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)

try: 
    # Store or Update a Correlation
    api_instance.v1_aggregated_correlations_post(body, access_token=access_token)
except ApiException as e:
    print "Exception when calling CorrelationsApi->v1_aggregated_correlations_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostCorrelation**](PostCorrelation.md)| Provides correlation data | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_correlations_get**
> list[Correlation] v1_correlations_get(access_token=access_token, effect=effect, cause=cause, correlation_coefficient=correlation_coefficient, onset_delay=onset_delay, duration_of_action=duration_of_action, last_updated=last_updated, limit=limit, offset=offset, sort=sort)

Get correlations

Get correlations.<br>Supported filter parameters:<br><ul><li><b>correlationCoefficient</b> - Pearson correlation coefficient between cause and effect after lagging by onset delay and grouping by duration of action</li><li><b>onsetDelay</b> - The number of seconds which pass following a cause measurement before an effect would likely be observed.</li><li><b>durationOfAction</b> - The time in seconds over which the cause would be expected to exert a measurable effect. We have selected a default value for each variable. This default value may be replaced by a user specified by adjusting their variable user settings.</li><li><b>lastUpdated</b> - The time that this measurement was last updated in the UTC format \"YYYY-MM-DDThh:mm:ss\"</li></ul><br>

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CorrelationsApi()
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
effect = 'effect_example' # str | ORIGINAL variable name of the effect variable for which the user desires correlations (optional)
cause = 'cause_example' # str | ORIGINAL variable name of the cause variable for which the user desires correlations (optional)
correlation_coefficient = 'correlation_coefficient_example' # str | Pearson correlation coefficient between cause and effect after lagging by onset delay and grouping by duration of action (optional)
onset_delay = 'onset_delay_example' # str | The number of seconds which pass following a cause measurement before an effect would likely be observed. (optional)
duration_of_action = 'duration_of_action_example' # str | The time in seconds over which the cause would be expected to exert a measurable effect. We have selected a default value for each variable. This default value may be replaced by a user specified by adjusting their variable user settings. (optional)
last_updated = 'last_updated_example' # str | The time that this measurement was last updated in the UTC format \"YYYY-MM-DDThh:mm:ss\" (optional)
limit = 56 # int | The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. (optional)
offset = 56 # int | Now suppose you wanted to show results 11-20. You'd set the offset to 10 and the limit to 10. (optional)
sort = 56 # int | Sort by given field. If the field is prefixed with `-, it will sort in descending order. (optional)

try: 
    # Get correlations
    api_response = api_instance.v1_correlations_get(access_token=access_token, effect=effect, cause=cause, correlation_coefficient=correlation_coefficient, onset_delay=onset_delay, duration_of_action=duration_of_action, last_updated=last_updated, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CorrelationsApi->v1_correlations_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **effect** | **str**| ORIGINAL variable name of the effect variable for which the user desires correlations | [optional] 
 **cause** | **str**| ORIGINAL variable name of the cause variable for which the user desires correlations | [optional] 
 **correlation_coefficient** | **str**| Pearson correlation coefficient between cause and effect after lagging by onset delay and grouping by duration of action | [optional] 
 **onset_delay** | **str**| The number of seconds which pass following a cause measurement before an effect would likely be observed. | [optional] 
 **duration_of_action** | **str**| The time in seconds over which the cause would be expected to exert a measurable effect. We have selected a default value for each variable. This default value may be replaced by a user specified by adjusting their variable user settings. | [optional] 
 **last_updated** | **str**| The time that this measurement was last updated in the UTC format \&quot;YYYY-MM-DDThh:mm:ss\&quot; | [optional] 
 **limit** | **int**| The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. | [optional] 
 **offset** | **int**| Now suppose you wanted to show results 11-20. You&#39;d set the offset to 10 and the limit to 10. | [optional] 
 **sort** | **int**| Sort by given field. If the field is prefixed with &#x60;-, it will sort in descending order. | [optional] 

### Return type

[**list[Correlation]**](Correlation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_organizations_organization_id_users_user_id_variables_variable_name_causes_get**
> list[Correlation] v1_organizations_organization_id_users_user_id_variables_variable_name_causes_get(organization_id, user_id, variable_name, organization_token, access_token=access_token, include_public=include_public)

Search user correlations for a given cause

Returns average of all correlations and votes for all user cause variables for a given cause. If parameter \"include_public\" is used, it also returns public correlations. User correlation overwrites or supersedes public correlation.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CorrelationsApi()
organization_id = 56 # int | Organization ID
user_id = 56 # int | User id
variable_name = 'variable_name_example' # str | Effect variable name
organization_token = 'organization_token_example' # str | Organization access token
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
include_public = 'include_public_example' # str | Include public correlations, Can be \"1\" or empty. (optional)

try: 
    # Search user correlations for a given cause
    api_response = api_instance.v1_organizations_organization_id_users_user_id_variables_variable_name_causes_get(organization_id, user_id, variable_name, organization_token, access_token=access_token, include_public=include_public)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CorrelationsApi->v1_organizations_organization_id_users_user_id_variables_variable_name_causes_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Organization ID | 
 **user_id** | **int**| User id | 
 **variable_name** | **str**| Effect variable name | 
 **organization_token** | **str**| Organization access token | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **include_public** | **str**| Include public correlations, Can be \&quot;1\&quot; or empty. | [optional] 

### Return type

[**list[Correlation]**](Correlation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_organizations_organization_id_users_user_id_variables_variable_name_effects_get**
> list[CommonResponse] v1_organizations_organization_id_users_user_id_variables_variable_name_effects_get(organization_id, user_id, variable_name, organization_token, access_token=access_token, include_public=include_public)

Search user correlations for a given cause

Returns average of all correlations and votes for all user cause variables for a given effect. If parameter \"include_public\" is used, it also returns public correlations. User correlation overwrites or supersedes public correlation.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CorrelationsApi()
organization_id = 56 # int | Organization ID
user_id = 56 # int | User id
variable_name = 'variable_name_example' # str | Cause variable name
organization_token = 'organization_token_example' # str | Organization access token
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
include_public = 'include_public_example' # str | Include public correlations, Can be \"1\" or empty. (optional)

try: 
    # Search user correlations for a given cause
    api_response = api_instance.v1_organizations_organization_id_users_user_id_variables_variable_name_effects_get(organization_id, user_id, variable_name, organization_token, access_token=access_token, include_public=include_public)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CorrelationsApi->v1_organizations_organization_id_users_user_id_variables_variable_name_effects_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Organization ID | 
 **user_id** | **int**| User id | 
 **variable_name** | **str**| Cause variable name | 
 **organization_token** | **str**| Organization access token | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **include_public** | **str**| Include public correlations, Can be \&quot;1\&quot; or empty. | [optional] 

### Return type

[**list[CommonResponse]**](CommonResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_public_correlations_search_search_get**
> list[Correlation] v1_public_correlations_search_search_get(search, effect_or_cause, access_token=access_token)

Get average correlations for variables containing search term

Returns the average correlations from all users for all public variables that contain the characters in the search query. Returns average of all users public variable correlations with a specified cause or effect.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CorrelationsApi()
search = 'search_example' # str | Name of the variable that you want to know the causes or effects of.
effect_or_cause = 'effect_or_cause_example' # str | Setting this to effect indicates that the searched variable is the effect and that the causes of this variable should be returned.  cause indicates that the searched variable is the cause and the effects should be returned.
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)

try: 
    # Get average correlations for variables containing search term
    api_response = api_instance.v1_public_correlations_search_search_get(search, effect_or_cause, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CorrelationsApi->v1_public_correlations_search_search_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Name of the variable that you want to know the causes or effects of. | 
 **effect_or_cause** | **str**| Setting this to effect indicates that the searched variable is the effect and that the causes of this variable should be returned.  cause indicates that the searched variable is the cause and the effects should be returned. | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 

### Return type

[**list[Correlation]**](Correlation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_variables_variable_name_causes_get**
> list[Correlation] v1_variables_variable_name_causes_get(variable_name)

Search user correlations for a given effect

Returns average of all correlations and votes for all user cause variables for a given effect

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CorrelationsApi()
variable_name = 'variable_name_example' # str | Effect variable name

try: 
    # Search user correlations for a given effect
    api_response = api_instance.v1_variables_variable_name_causes_get(variable_name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CorrelationsApi->v1_variables_variable_name_causes_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_name** | **str**| Effect variable name | 

### Return type

[**list[Correlation]**](Correlation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_variables_variable_name_effects_get**
> list[Correlation] v1_variables_variable_name_effects_get(variable_name, access_token=access_token)

Search user correlations for a given cause

Returns average of all correlations and votes for all user effect variables for a given cause

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CorrelationsApi()
variable_name = 'variable_name_example' # str | Cause variable name
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)

try: 
    # Search user correlations for a given cause
    api_response = api_instance.v1_variables_variable_name_effects_get(variable_name, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CorrelationsApi->v1_variables_variable_name_effects_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_name** | **str**| Cause variable name | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 

### Return type

[**list[Correlation]**](Correlation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_variables_variable_name_public_causes_get**
> list[Correlation] v1_variables_variable_name_public_causes_get(variable_name, access_token=access_token)

Search public correlations for a given effect

Returns average of all correlations and votes for all public cause variables for a given effect

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CorrelationsApi()
variable_name = 'variable_name_example' # str | Effect variable name
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)

try: 
    # Search public correlations for a given effect
    api_response = api_instance.v1_variables_variable_name_public_causes_get(variable_name, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CorrelationsApi->v1_variables_variable_name_public_causes_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_name** | **str**| Effect variable name | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 

### Return type

[**list[Correlation]**](Correlation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_variables_variable_name_public_effects_get**
> list[Correlation] v1_variables_variable_name_public_effects_get(variable_name, access_token=access_token)

Search public correlations for a given cause

Returns average of all correlations and votes for all public cause variables for a given cause

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CorrelationsApi()
variable_name = 'variable_name_example' # str | Cause variable name
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)

try: 
    # Search public correlations for a given cause
    api_response = api_instance.v1_variables_variable_name_public_effects_get(variable_name, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CorrelationsApi->v1_variables_variable_name_public_effects_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_name** | **str**| Cause variable name | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 

### Return type

[**list[Correlation]**](Correlation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_votes_delete_post**
> CommonResponse v1_votes_delete_post(body, access_token=access_token)

Delete vote

Delete previously posted vote

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CorrelationsApi()
body = swagger_client.VoteDelete() # VoteDelete | The cause and effect variable names for the predictor vote to be deleted.
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)

try: 
    # Delete vote
    api_response = api_instance.v1_votes_delete_post(body, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CorrelationsApi->v1_votes_delete_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VoteDelete**](VoteDelete.md)| The cause and effect variable names for the predictor vote to be deleted. | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_votes_post**
> CommonResponse v1_votes_post(body, access_token=access_token)

Post or update vote

This is to enable users to indicate their opinion on the plausibility of a causal relationship between a treatment and outcome. QuantiModo incorporates crowd-sourced plausibility estimations into their algorithm. This is done allowing user to indicate their view of the plausibility of each relationship with thumbs up/down buttons placed next to each prediction.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CorrelationsApi()
body = swagger_client.PostVote() # PostVote | Contains the cause variable, effect variable, and vote value.
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)

try: 
    # Post or update vote
    api_response = api_instance.v1_votes_post(body, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CorrelationsApi->v1_votes_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostVote**](PostVote.md)| Contains the cause variable, effect variable, and vote value. | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

