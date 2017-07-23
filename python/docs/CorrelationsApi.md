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
> list[Correlation] v1_aggregated_correlations_get(access_token=access_token, user_id=user_id, effect=effect, cause=cause, correlation_coefficient=correlation_coefficient, onset_delay=onset_delay, duration_of_action=duration_of_action, updated_at=updated_at, limit=limit, offset=offset, sort=sort, outcomes_of_interest=outcomes_of_interest)

Get aggregated correlations

Get correlations based on the anonymized aggregate data from all QuantiModo users.

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
api_instance = swagger_client.CorrelationsApi()
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
user_id = 56 # int | User's id (optional)
effect = 'effect_example' # str | Variable name of the effect variable for which the user desires correlations (optional)
cause = 'cause_example' # str | Variable name of the cause variable for which the user desires correlations (optional)
correlation_coefficient = 'correlation_coefficient_example' # str | Pearson correlation coefficient between cause and effect after lagging by onset delay and grouping by duration of action (optional)
onset_delay = 'onset_delay_example' # str | The amount of time in seconds that elapses after the predictor/stimulus event before the outcome as perceived by a self-tracker is known as the “onset delay”. For example, the “onset delay” between the time a person takes an aspirin (predictor/stimulus event) and the time a person perceives a change in their headache severity (outcome) is approximately 30 minutes. (optional)
duration_of_action = 'duration_of_action_example' # str | The amount of time over which a predictor/stimulus event can exert an observable influence on an outcome variable’s value. For instance, aspirin (stimulus/predictor) typically decreases headache severity for approximately four hours (duration of action) following the onset delay. (optional)
updated_at = 'updated_at_example' # str | The time that this measurement was last updated in the UTC format \"YYYY-MM-DDThh:mm:ss\".  Generally, you'll be retrieving new or updated user data. To avoid unnecessary API calls, you'll want to store your last refresh time locally. Then whenever you make a request to get new data, you should limit the returned results to those updated since your last refresh by appending append `?updatedAt=(ge)2013-01-D01T01:01:01 to your request. (optional)
limit = 56 # int | The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. (optional)
offset = 56 # int | Since the maximum limit is 200 records, to get more than that you'll have to make multiple API calls and page through the results. To retrieve all the data, you can iterate through data by using the `limit` and `offset` query parameters.  For example, if you want to retrieve data from 61-80 then you can use a query with the following parameters, `imit=20&offset=60`. (optional)
sort = 56 # int | Sort by given field. If the field is prefixed with `-, it will sort in descending order. (optional)
outcomes_of_interest = true # bool | Only include correlations for which the effect is an outcome of interest for the user (optional)

try: 
    # Get aggregated correlations
    api_response = api_instance.v1_aggregated_correlations_get(access_token=access_token, user_id=user_id, effect=effect, cause=cause, correlation_coefficient=correlation_coefficient, onset_delay=onset_delay, duration_of_action=duration_of_action, updated_at=updated_at, limit=limit, offset=offset, sort=sort, outcomes_of_interest=outcomes_of_interest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorrelationsApi->v1_aggregated_correlations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **user_id** | **int**| User&#39;s id | [optional] 
 **effect** | **str**| Variable name of the effect variable for which the user desires correlations | [optional] 
 **cause** | **str**| Variable name of the cause variable for which the user desires correlations | [optional] 
 **correlation_coefficient** | **str**| Pearson correlation coefficient between cause and effect after lagging by onset delay and grouping by duration of action | [optional] 
 **onset_delay** | **str**| The amount of time in seconds that elapses after the predictor/stimulus event before the outcome as perceived by a self-tracker is known as the “onset delay”. For example, the “onset delay” between the time a person takes an aspirin (predictor/stimulus event) and the time a person perceives a change in their headache severity (outcome) is approximately 30 minutes. | [optional] 
 **duration_of_action** | **str**| The amount of time over which a predictor/stimulus event can exert an observable influence on an outcome variable’s value. For instance, aspirin (stimulus/predictor) typically decreases headache severity for approximately four hours (duration of action) following the onset delay. | [optional] 
 **updated_at** | **str**| The time that this measurement was last updated in the UTC format \&quot;YYYY-MM-DDThh:mm:ss\&quot;.  Generally, you&#39;ll be retrieving new or updated user data. To avoid unnecessary API calls, you&#39;ll want to store your last refresh time locally. Then whenever you make a request to get new data, you should limit the returned results to those updated since your last refresh by appending append &#x60;?updatedAt&#x3D;(ge)2013-01-D01T01:01:01 to your request. | [optional] 
 **limit** | **int**| The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. | [optional] 
 **offset** | **int**| Since the maximum limit is 200 records, to get more than that you&#39;ll have to make multiple API calls and page through the results. To retrieve all the data, you can iterate through data by using the &#x60;limit&#x60; and &#x60;offset&#x60; query parameters.  For example, if you want to retrieve data from 61-80 then you can use a query with the following parameters, &#x60;imit&#x3D;20&amp;offset&#x3D;60&#x60;. | [optional] 
 **sort** | **int**| Sort by given field. If the field is prefixed with &#x60;-, it will sort in descending order. | [optional] 
 **outcomes_of_interest** | **bool**| Only include correlations for which the effect is an outcome of interest for the user | [optional] 

### Return type

[**list[Correlation]**](Correlation.md)

### Authorization

[access_token](../README.md#access_token), [quantimodo_oauth2](../README.md#quantimodo_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_aggregated_correlations_post**
> v1_aggregated_correlations_post(body, access_token=access_token, user_id=user_id)

Store or Update a Correlation

Add correlation

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
api_instance = swagger_client.CorrelationsApi()
body = swagger_client.PostCorrelation() # PostCorrelation | Provides correlation data
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
user_id = 56 # int | User's id (optional)

try: 
    # Store or Update a Correlation
    api_instance.v1_aggregated_correlations_post(body, access_token=access_token, user_id=user_id)
except ApiException as e:
    print("Exception when calling CorrelationsApi->v1_aggregated_correlations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostCorrelation**](PostCorrelation.md)| Provides correlation data | 
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

# **v1_correlations_get**
> list[Correlation] v1_correlations_get(access_token=access_token, user_id=user_id, effect=effect, cause=cause, correlation_coefficient=correlation_coefficient, onset_delay=onset_delay, duration_of_action=duration_of_action, updated_at=updated_at, limit=limit, offset=offset, sort=sort, outcomes_of_interest=outcomes_of_interest)

Get correlations

Get correlations based on data from a single user.

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
api_instance = swagger_client.CorrelationsApi()
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
user_id = 56 # int | User's id (optional)
effect = 'effect_example' # str | Variable name of the effect variable for which the user desires correlations (optional)
cause = 'cause_example' # str | Variable name of the cause variable for which the user desires correlations (optional)
correlation_coefficient = 'correlation_coefficient_example' # str | Pearson correlation coefficient between cause and effect after lagging by onset delay and grouping by duration of action (optional)
onset_delay = 'onset_delay_example' # str | The amount of time in seconds that elapses after the predictor/stimulus event before the outcome as perceived by a self-tracker is known as the “onset delay”. For example, the “onset delay” between the time a person takes an aspirin (predictor/stimulus event) and the time a person perceives a change in their headache severity (outcome) is approximately 30 minutes. (optional)
duration_of_action = 'duration_of_action_example' # str | The amount of time over which a predictor/stimulus event can exert an observable influence on an outcome variable’s value. For instance, aspirin (stimulus/predictor) typically decreases headache severity for approximately four hours (duration of action) following the onset delay. (optional)
updated_at = 'updated_at_example' # str | The time that this measurement was last updated in the UTC format \"YYYY-MM-DDThh:mm:ss\".  Generally, you'll be retrieving new or updated user data. To avoid unnecessary API calls, you'll want to store your last refresh time locally. Then whenever you make a request to get new data, you should limit the returned results to those updated since your last refresh by appending append `?updatedAt=(ge)2013-01-D01T01:01:01 to your request. (optional)
limit = 56 # int | The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. (optional)
offset = 56 # int | Since the maximum limit is 200 records, to get more than that you'll have to make multiple API calls and page through the results. To retrieve all the data, you can iterate through data by using the `limit` and `offset` query parameters.  For example, if you want to retrieve data from 61-80 then you can use a query with the following parameters, `imit=20&offset=60`. (optional)
sort = 56 # int | Sort by given field. If the field is prefixed with `-, it will sort in descending order. (optional)
outcomes_of_interest = true # bool | Only include correlations for which the effect is an outcome of interest for the user (optional)

try: 
    # Get correlations
    api_response = api_instance.v1_correlations_get(access_token=access_token, user_id=user_id, effect=effect, cause=cause, correlation_coefficient=correlation_coefficient, onset_delay=onset_delay, duration_of_action=duration_of_action, updated_at=updated_at, limit=limit, offset=offset, sort=sort, outcomes_of_interest=outcomes_of_interest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorrelationsApi->v1_correlations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **user_id** | **int**| User&#39;s id | [optional] 
 **effect** | **str**| Variable name of the effect variable for which the user desires correlations | [optional] 
 **cause** | **str**| Variable name of the cause variable for which the user desires correlations | [optional] 
 **correlation_coefficient** | **str**| Pearson correlation coefficient between cause and effect after lagging by onset delay and grouping by duration of action | [optional] 
 **onset_delay** | **str**| The amount of time in seconds that elapses after the predictor/stimulus event before the outcome as perceived by a self-tracker is known as the “onset delay”. For example, the “onset delay” between the time a person takes an aspirin (predictor/stimulus event) and the time a person perceives a change in their headache severity (outcome) is approximately 30 minutes. | [optional] 
 **duration_of_action** | **str**| The amount of time over which a predictor/stimulus event can exert an observable influence on an outcome variable’s value. For instance, aspirin (stimulus/predictor) typically decreases headache severity for approximately four hours (duration of action) following the onset delay. | [optional] 
 **updated_at** | **str**| The time that this measurement was last updated in the UTC format \&quot;YYYY-MM-DDThh:mm:ss\&quot;.  Generally, you&#39;ll be retrieving new or updated user data. To avoid unnecessary API calls, you&#39;ll want to store your last refresh time locally. Then whenever you make a request to get new data, you should limit the returned results to those updated since your last refresh by appending append &#x60;?updatedAt&#x3D;(ge)2013-01-D01T01:01:01 to your request. | [optional] 
 **limit** | **int**| The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. | [optional] 
 **offset** | **int**| Since the maximum limit is 200 records, to get more than that you&#39;ll have to make multiple API calls and page through the results. To retrieve all the data, you can iterate through data by using the &#x60;limit&#x60; and &#x60;offset&#x60; query parameters.  For example, if you want to retrieve data from 61-80 then you can use a query with the following parameters, &#x60;imit&#x3D;20&amp;offset&#x3D;60&#x60;. | [optional] 
 **sort** | **int**| Sort by given field. If the field is prefixed with &#x60;-, it will sort in descending order. | [optional] 
 **outcomes_of_interest** | **bool**| Only include correlations for which the effect is an outcome of interest for the user | [optional] 

### Return type

[**list[Correlation]**](Correlation.md)

### Authorization

[access_token](../README.md#access_token), [quantimodo_oauth2](../README.md#quantimodo_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_organizations_organization_id_users_user_id_variables_variable_name_causes_get**
> list[Correlation] v1_organizations_organization_id_users_user_id_variables_variable_name_causes_get(organization_id, user_id2, variable_name, organization_token, access_token=access_token, user_id=user_id, include_public=include_public)

Search user correlations for a given cause

Returns average of all correlations and votes for all user cause variables for a given cause. If parameter \"include_public\" is used, it also returns public correlations. User correlation overwrites or supersedes public correlation.

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
api_instance = swagger_client.CorrelationsApi()
organization_id = 56 # int | Organization ID
user_id2 = 56 # int | User id
variable_name = 'variable_name_example' # str | Effect variable name
organization_token = 'organization_token_example' # str | Organization access token
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
user_id = 56 # int | User's id (optional)
include_public = 'include_public_example' # str | Include public correlations, Can be \"1\" or empty. (optional)

try: 
    # Search user correlations for a given cause
    api_response = api_instance.v1_organizations_organization_id_users_user_id_variables_variable_name_causes_get(organization_id, user_id2, variable_name, organization_token, access_token=access_token, user_id=user_id, include_public=include_public)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorrelationsApi->v1_organizations_organization_id_users_user_id_variables_variable_name_causes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Organization ID | 
 **user_id2** | **int**| User id | 
 **variable_name** | **str**| Effect variable name | 
 **organization_token** | **str**| Organization access token | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **user_id** | **int**| User&#39;s id | [optional] 
 **include_public** | **str**| Include public correlations, Can be \&quot;1\&quot; or empty. | [optional] 

### Return type

[**list[Correlation]**](Correlation.md)

### Authorization

[access_token](../README.md#access_token), [quantimodo_oauth2](../README.md#quantimodo_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_organizations_organization_id_users_user_id_variables_variable_name_effects_get**
> list[CommonResponse] v1_organizations_organization_id_users_user_id_variables_variable_name_effects_get(organization_id, user_id2, variable_name, organization_token, access_token=access_token, user_id=user_id, include_public=include_public)

Search user correlations for a given cause

Returns average of all correlations and votes for all user cause variables for a given effect. If parameter \"include_public\" is used, it also returns public correlations. User correlation overwrites or supersedes public correlation.

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
api_instance = swagger_client.CorrelationsApi()
organization_id = 56 # int | Organization ID
user_id2 = 56 # int | User id
variable_name = 'variable_name_example' # str | Cause variable name
organization_token = 'organization_token_example' # str | Organization access token
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
user_id = 56 # int | User's id (optional)
include_public = 'include_public_example' # str | Include public correlations, Can be \"1\" or empty. (optional)

try: 
    # Search user correlations for a given cause
    api_response = api_instance.v1_organizations_organization_id_users_user_id_variables_variable_name_effects_get(organization_id, user_id2, variable_name, organization_token, access_token=access_token, user_id=user_id, include_public=include_public)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorrelationsApi->v1_organizations_organization_id_users_user_id_variables_variable_name_effects_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Organization ID | 
 **user_id2** | **int**| User id | 
 **variable_name** | **str**| Cause variable name | 
 **organization_token** | **str**| Organization access token | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **user_id** | **int**| User&#39;s id | [optional] 
 **include_public** | **str**| Include public correlations, Can be \&quot;1\&quot; or empty. | [optional] 

### Return type

[**list[CommonResponse]**](CommonResponse.md)

### Authorization

[access_token](../README.md#access_token), [quantimodo_oauth2](../README.md#quantimodo_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_public_correlations_search_search_get**
> list[Correlation] v1_public_correlations_search_search_get(search, effect_or_cause, access_token=access_token, user_id=user_id, outcomes_of_interest=outcomes_of_interest)

Get average correlations for variables containing search term

Returns the average correlations from all users for all public variables that contain the characters in the search query. Returns average of all users public variable correlations with a specified cause or effect.

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
api_instance = swagger_client.CorrelationsApi()
search = 'search_example' # str | Name of the variable that you want to know the causes or effects of.
effect_or_cause = 'effect_or_cause_example' # str | Setting this to effect indicates that the searched variable is the effect and that the causes of this variable should be returned. cause indicates that the searched variable is the cause and the effects should be returned.
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
user_id = 56 # int | User's id (optional)
outcomes_of_interest = true # bool | Only include correlations for which the effect is an outcome of interest for the user (optional)

try: 
    # Get average correlations for variables containing search term
    api_response = api_instance.v1_public_correlations_search_search_get(search, effect_or_cause, access_token=access_token, user_id=user_id, outcomes_of_interest=outcomes_of_interest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorrelationsApi->v1_public_correlations_search_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Name of the variable that you want to know the causes or effects of. | 
 **effect_or_cause** | **str**| Setting this to effect indicates that the searched variable is the effect and that the causes of this variable should be returned. cause indicates that the searched variable is the cause and the effects should be returned. | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **user_id** | **int**| User&#39;s id | [optional] 
 **outcomes_of_interest** | **bool**| Only include correlations for which the effect is an outcome of interest for the user | [optional] 

### Return type

[**list[Correlation]**](Correlation.md)

### Authorization

[access_token](../README.md#access_token), [quantimodo_oauth2](../README.md#quantimodo_oauth2)

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
api_instance = swagger_client.CorrelationsApi()
variable_name = 'variable_name_example' # str | Effect variable name

try: 
    # Search user correlations for a given effect
    api_response = api_instance.v1_variables_variable_name_causes_get(variable_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorrelationsApi->v1_variables_variable_name_causes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_name** | **str**| Effect variable name | 

### Return type

[**list[Correlation]**](Correlation.md)

### Authorization

[access_token](../README.md#access_token), [quantimodo_oauth2](../README.md#quantimodo_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_variables_variable_name_effects_get**
> list[Correlation] v1_variables_variable_name_effects_get(variable_name, access_token=access_token, user_id=user_id, correlation_coefficient=correlation_coefficient)

Search user correlations for a given cause

Returns average of all correlations and votes for all user effect variables for a given cause

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
api_instance = swagger_client.CorrelationsApi()
variable_name = 'variable_name_example' # str | Cause variable name
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
user_id = 56 # int | User's id (optional)
correlation_coefficient = 'correlation_coefficient_example' # str | You can use this to get effects with correlations greater than or less than 0 (optional)

try: 
    # Search user correlations for a given cause
    api_response = api_instance.v1_variables_variable_name_effects_get(variable_name, access_token=access_token, user_id=user_id, correlation_coefficient=correlation_coefficient)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorrelationsApi->v1_variables_variable_name_effects_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_name** | **str**| Cause variable name | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **user_id** | **int**| User&#39;s id | [optional] 
 **correlation_coefficient** | **str**| You can use this to get effects with correlations greater than or less than 0 | [optional] 

### Return type

[**list[Correlation]**](Correlation.md)

### Authorization

[access_token](../README.md#access_token), [quantimodo_oauth2](../README.md#quantimodo_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_variables_variable_name_public_causes_get**
> list[Correlation] v1_variables_variable_name_public_causes_get(variable_name, access_token=access_token, user_id=user_id, correlation_coefficient=correlation_coefficient)

Search public correlations for a given effect

Returns average of all correlations and votes for all public cause variables for a given effect

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
api_instance = swagger_client.CorrelationsApi()
variable_name = 'variable_name_example' # str | Effect variable name
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
user_id = 56 # int | User's id (optional)
correlation_coefficient = 'correlation_coefficient_example' # str | You can use this to get causes with correlations greater than or less than 0 (optional)

try: 
    # Search public correlations for a given effect
    api_response = api_instance.v1_variables_variable_name_public_causes_get(variable_name, access_token=access_token, user_id=user_id, correlation_coefficient=correlation_coefficient)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorrelationsApi->v1_variables_variable_name_public_causes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_name** | **str**| Effect variable name | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **user_id** | **int**| User&#39;s id | [optional] 
 **correlation_coefficient** | **str**| You can use this to get causes with correlations greater than or less than 0 | [optional] 

### Return type

[**list[Correlation]**](Correlation.md)

### Authorization

[access_token](../README.md#access_token), [quantimodo_oauth2](../README.md#quantimodo_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_variables_variable_name_public_effects_get**
> list[Correlation] v1_variables_variable_name_public_effects_get(variable_name, access_token=access_token, user_id=user_id)

Search public correlations for a given cause

Returns average of all correlations and votes for all public cause variables for a given cause

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
api_instance = swagger_client.CorrelationsApi()
variable_name = 'variable_name_example' # str | Cause variable name
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
user_id = 56 # int | User's id (optional)

try: 
    # Search public correlations for a given cause
    api_response = api_instance.v1_variables_variable_name_public_effects_get(variable_name, access_token=access_token, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorrelationsApi->v1_variables_variable_name_public_effects_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_name** | **str**| Cause variable name | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **user_id** | **int**| User&#39;s id | [optional] 

### Return type

[**list[Correlation]**](Correlation.md)

### Authorization

[access_token](../README.md#access_token), [quantimodo_oauth2](../README.md#quantimodo_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_votes_delete_post**
> CommonResponse v1_votes_delete_post(body, access_token=access_token, user_id=user_id)

Delete vote

Delete previously posted vote

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
api_instance = swagger_client.CorrelationsApi()
body = swagger_client.VoteDelete() # VoteDelete | The cause and effect variable names for the predictor vote to be deleted.
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
user_id = 56 # int | User's id (optional)

try: 
    # Delete vote
    api_response = api_instance.v1_votes_delete_post(body, access_token=access_token, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorrelationsApi->v1_votes_delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VoteDelete**](VoteDelete.md)| The cause and effect variable names for the predictor vote to be deleted. | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **user_id** | **int**| User&#39;s id | [optional] 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

[access_token](../README.md#access_token), [quantimodo_oauth2](../README.md#quantimodo_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_votes_post**
> CommonResponse v1_votes_post(body, access_token=access_token, user_id=user_id)

Post or update vote

This is to enable users to indicate their opinion on the plausibility of a causal relationship between a treatment and outcome. QuantiModo incorporates crowd-sourced plausibility estimations into their algorithm. This is done allowing user to indicate their view of the plausibility of each relationship with thumbs up/down buttons placed next to each prediction.

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
api_instance = swagger_client.CorrelationsApi()
body = swagger_client.PostVote() # PostVote | Contains the cause variable, effect variable, and vote value.
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
user_id = 56 # int | User's id (optional)

try: 
    # Post or update vote
    api_response = api_instance.v1_votes_post(body, access_token=access_token, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorrelationsApi->v1_votes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostVote**](PostVote.md)| Contains the cause variable, effect variable, and vote value. | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **user_id** | **int**| User&#39;s id | [optional] 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

[access_token](../README.md#access_token), [quantimodo_oauth2](../README.md#quantimodo_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

