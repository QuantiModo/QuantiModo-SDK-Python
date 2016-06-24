# swagger_client.VotesApi

All URIs are relative to *https://app.quantimo.do/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_votes_delete_post**](VotesApi.md#v1_votes_delete_post) | **POST** /v1/votes/delete | Delete vote
[**v1_votes_post**](VotesApi.md#v1_votes_post) | **POST** /v1/votes | Post or update vote


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
api_instance = swagger_client.VotesApi()
body = swagger_client.VoteDelete() # VoteDelete | The cause and effect variable names for the predictor vote to be deleted.
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)

try: 
    # Delete vote
    api_response = api_instance.v1_votes_delete_post(body, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VotesApi->v1_votes_delete_post: %s\n" % e
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
api_instance = swagger_client.VotesApi()
body = swagger_client.PostVote() # PostVote | Contains the cause variable, effect variable, and vote value.
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)

try: 
    # Post or update vote
    api_response = api_instance.v1_votes_post(body, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VotesApi->v1_votes_post: %s\n" % e
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

