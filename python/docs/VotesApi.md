# swagger_client.VotesApi

All URIs are relative to *https://app.quantimo.do/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_votes_delete_post**](VotesApi.md#v1_votes_delete_post) | **POST** /v1/votes/delete | Delete vote
[**v1_votes_post**](VotesApi.md#v1_votes_post) | **POST** /v1/votes | Post or update vote


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
api_instance = swagger_client.VotesApi()
body = swagger_client.VoteDelete() # VoteDelete | The cause and effect variable names for the predictor vote to be deleted.
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
user_id = 56 # int | User's id (optional)

try: 
    # Delete vote
    api_response = api_instance.v1_votes_delete_post(body, access_token=access_token, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VotesApi->v1_votes_delete_post: %s\n" % e)
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
api_instance = swagger_client.VotesApi()
body = swagger_client.PostVote() # PostVote | Contains the cause variable, effect variable, and vote value.
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
user_id = 56 # int | User's id (optional)

try: 
    # Post or update vote
    api_response = api_instance.v1_votes_post(body, access_token=access_token, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VotesApi->v1_votes_post: %s\n" % e)
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

