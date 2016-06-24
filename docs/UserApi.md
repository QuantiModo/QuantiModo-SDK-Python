# swagger_client.UserApi

All URIs are relative to *https://app.quantimo.do/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_organizations_organization_id_users_post**](UserApi.md#v1_organizations_organization_id_users_post) | **POST** /v1/organizations/{organizationId}/users | Get user tokens for existing users, create new users
[**v1_user_me_get**](UserApi.md#v1_user_me_get) | **GET** /v1/user/me | Get all available units for variableGet authenticated user


# **v1_organizations_organization_id_users_post**
> UserTokenSuccessfulResponse v1_organizations_organization_id_users_post(organization_id, body, access_token=access_token)

Get user tokens for existing users, create new users

Get user tokens for existing users, create new users

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: internalApiKey
swagger_client.configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi()
organization_id = 56 # int | Organization ID
body = swagger_client.UserTokenRequest() # UserTokenRequest | Provides organization token and user ID
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)

try: 
    # Get user tokens for existing users, create new users
    api_response = api_instance.v1_organizations_organization_id_users_post(organization_id, body, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->v1_organizations_organization_id_users_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Organization ID | 
 **body** | [**UserTokenRequest**](UserTokenRequest.md)| Provides organization token and user ID | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 

### Return type

[**UserTokenSuccessfulResponse**](UserTokenSuccessfulResponse.md)

### Authorization

[oauth2](../README.md#oauth2), [internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_user_me_get**
> User v1_user_me_get()

Get all available units for variableGet authenticated user

Returns user info for the currently authenticated user.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UserApi()

try: 
    # Get all available units for variableGet authenticated user
    api_response = api_instance.v1_user_me_get()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->v1_user_me_get: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

