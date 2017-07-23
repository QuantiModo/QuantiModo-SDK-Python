# swagger_client.RemindersApi

All URIs are relative to *https://app.quantimo.do/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_tracking_reminder_notifications_get**](RemindersApi.md#v1_tracking_reminder_notifications_get) | **GET** /v1/trackingReminderNotifications | Get specific pending tracking reminders
[**v1_tracking_reminder_notifications_skip_post**](RemindersApi.md#v1_tracking_reminder_notifications_skip_post) | **POST** /v1/trackingReminderNotifications/skip | Skip a pending tracking reminder
[**v1_tracking_reminder_notifications_snooze_post**](RemindersApi.md#v1_tracking_reminder_notifications_snooze_post) | **POST** /v1/trackingReminderNotifications/snooze | Snooze a pending tracking reminder
[**v1_tracking_reminder_notifications_track_post**](RemindersApi.md#v1_tracking_reminder_notifications_track_post) | **POST** /v1/trackingReminderNotifications/track | Track a pending tracking reminder
[**v1_tracking_reminders_delete_post**](RemindersApi.md#v1_tracking_reminders_delete_post) | **POST** /v1/trackingReminders/delete | Delete tracking reminder
[**v1_tracking_reminders_get**](RemindersApi.md#v1_tracking_reminders_get) | **GET** /v1/trackingReminders | Get repeating tracking reminder settings
[**v1_tracking_reminders_post**](RemindersApi.md#v1_tracking_reminders_post) | **POST** /v1/trackingReminders | Store a Tracking Reminder


# **v1_tracking_reminder_notifications_get**
> InlineResponse2002 v1_tracking_reminder_notifications_get(access_token=access_token, user_id=user_id, variable_category_name=variable_category_name, created_at=created_at, updated_at=updated_at, limit=limit, offset=offset, sort=sort)

Get specific pending tracking reminders

Specfic pending reminder instances that still need to be tracked.  

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
api_instance = swagger_client.RemindersApi()
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
user_id = 56 # int | User's id (optional)
variable_category_name = 'variable_category_name_example' # str | Limit tracking reminder notifications to a specific variable category (optional)
created_at = 'created_at_example' # str | When the record was first created. Use UTC ISO 8601 \"YYYY-MM-DDThh:mm:ss\"  datetime format. Time zone should be UTC and not local. (optional)
updated_at = 'updated_at_example' # str | When the record was last updated. Use UTC ISO 8601 \"YYYY-MM-DDThh:mm:ss\"  datetime format. Time zone should be UTC and not local. (optional)
limit = 56 # int | The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records. (optional)
offset = 56 # int | OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned. (optional)
sort = 'sort_example' # str | Sort by given field. If the field is prefixed with '-', it will sort in descending order. (optional)

try: 
    # Get specific pending tracking reminders
    api_response = api_instance.v1_tracking_reminder_notifications_get(access_token=access_token, user_id=user_id, variable_category_name=variable_category_name, created_at=created_at, updated_at=updated_at, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemindersApi->v1_tracking_reminder_notifications_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **user_id** | **int**| User&#39;s id | [optional] 
 **variable_category_name** | **str**| Limit tracking reminder notifications to a specific variable category | [optional] 
 **created_at** | **str**| When the record was first created. Use UTC ISO 8601 \&quot;YYYY-MM-DDThh:mm:ss\&quot;  datetime format. Time zone should be UTC and not local. | [optional] 
 **updated_at** | **str**| When the record was last updated. Use UTC ISO 8601 \&quot;YYYY-MM-DDThh:mm:ss\&quot;  datetime format. Time zone should be UTC and not local. | [optional] 
 **limit** | **int**| The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records. | [optional] 
 **offset** | **int**| OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned. | [optional] 
 **sort** | **str**| Sort by given field. If the field is prefixed with &#39;-&#39;, it will sort in descending order. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[access_token](../README.md#access_token), [quantimodo_oauth2](../README.md#quantimodo_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_tracking_reminder_notifications_skip_post**
> CommonResponse v1_tracking_reminder_notifications_skip_post(body, access_token=access_token, user_id=user_id)

Skip a pending tracking reminder

Deletes the pending tracking reminder

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
api_instance = swagger_client.RemindersApi()
body = swagger_client.TrackingReminderNotificationSkip() # TrackingReminderNotificationSkip | Id of the pending reminder to be skipped or deleted
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
user_id = 56 # int | User's id (optional)

try: 
    # Skip a pending tracking reminder
    api_response = api_instance.v1_tracking_reminder_notifications_skip_post(body, access_token=access_token, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemindersApi->v1_tracking_reminder_notifications_skip_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrackingReminderNotificationSkip**](TrackingReminderNotificationSkip.md)| Id of the pending reminder to be skipped or deleted | 
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

# **v1_tracking_reminder_notifications_snooze_post**
> CommonResponse v1_tracking_reminder_notifications_snooze_post(body, access_token=access_token, user_id=user_id)

Snooze a pending tracking reminder

Changes the reminder time to now plus one hour

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
api_instance = swagger_client.RemindersApi()
body = swagger_client.TrackingReminderNotificationSnooze() # TrackingReminderNotificationSnooze | Id of the pending reminder to be snoozed
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
user_id = 56 # int | User's id (optional)

try: 
    # Snooze a pending tracking reminder
    api_response = api_instance.v1_tracking_reminder_notifications_snooze_post(body, access_token=access_token, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemindersApi->v1_tracking_reminder_notifications_snooze_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrackingReminderNotificationSnooze**](TrackingReminderNotificationSnooze.md)| Id of the pending reminder to be snoozed | 
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

# **v1_tracking_reminder_notifications_track_post**
> CommonResponse v1_tracking_reminder_notifications_track_post(body, access_token=access_token, user_id=user_id)

Track a pending tracking reminder

Adds the default measurement for the pending tracking reminder with the reminder time as the measurment start time

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
api_instance = swagger_client.RemindersApi()
body = swagger_client.TrackingReminderNotificationTrack() # TrackingReminderNotificationTrack | Id of the pending reminder to be tracked
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
user_id = 56 # int | User's id (optional)

try: 
    # Track a pending tracking reminder
    api_response = api_instance.v1_tracking_reminder_notifications_track_post(body, access_token=access_token, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemindersApi->v1_tracking_reminder_notifications_track_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrackingReminderNotificationTrack**](TrackingReminderNotificationTrack.md)| Id of the pending reminder to be tracked | 
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

# **v1_tracking_reminders_delete_post**
> CommonResponse v1_tracking_reminders_delete_post(body, access_token=access_token, user_id=user_id)

Delete tracking reminder

Delete previously created tracking reminder

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
api_instance = swagger_client.RemindersApi()
body = swagger_client.TrackingReminderDelete() # TrackingReminderDelete | Id of reminder to be deleted
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
user_id = 56 # int | User's id (optional)

try: 
    # Delete tracking reminder
    api_response = api_instance.v1_tracking_reminders_delete_post(body, access_token=access_token, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemindersApi->v1_tracking_reminders_delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrackingReminderDelete**](TrackingReminderDelete.md)| Id of reminder to be deleted | 
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

# **v1_tracking_reminders_get**
> InlineResponse200 v1_tracking_reminders_get(access_token=access_token, user_id=user_id, variable_category_name=variable_category_name, created_at=created_at, updated_at=updated_at, limit=limit, offset=offset, sort=sort)

Get repeating tracking reminder settings

Users can be reminded to track certain variables at a specified frequency with a default value.

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
api_instance = swagger_client.RemindersApi()
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
user_id = 56 # int | User's id (optional)
variable_category_name = 'variable_category_name_example' # str | Limit tracking reminders to a specific variable category (optional)
created_at = 'created_at_example' # str | When the record was first created. Use UTC ISO 8601 \"YYYY-MM-DDThh:mm:ss\"  datetime format. Time zone should be UTC and not local. (optional)
updated_at = 'updated_at_example' # str | When the record was last updated. Use UTC ISO 8601 \"YYYY-MM-DDThh:mm:ss\"  datetime format. Time zone should be UTC and not local. (optional)
limit = 56 # int | The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records. (optional)
offset = 56 # int | OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned. (optional)
sort = 'sort_example' # str | Sort by given field. If the field is prefixed with '-', it will sort in descending order. (optional)

try: 
    # Get repeating tracking reminder settings
    api_response = api_instance.v1_tracking_reminders_get(access_token=access_token, user_id=user_id, variable_category_name=variable_category_name, created_at=created_at, updated_at=updated_at, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemindersApi->v1_tracking_reminders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **user_id** | **int**| User&#39;s id | [optional] 
 **variable_category_name** | **str**| Limit tracking reminders to a specific variable category | [optional] 
 **created_at** | **str**| When the record was first created. Use UTC ISO 8601 \&quot;YYYY-MM-DDThh:mm:ss\&quot;  datetime format. Time zone should be UTC and not local. | [optional] 
 **updated_at** | **str**| When the record was last updated. Use UTC ISO 8601 \&quot;YYYY-MM-DDThh:mm:ss\&quot;  datetime format. Time zone should be UTC and not local. | [optional] 
 **limit** | **int**| The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records. | [optional] 
 **offset** | **int**| OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned. | [optional] 
 **sort** | **str**| Sort by given field. If the field is prefixed with &#39;-&#39;, it will sort in descending order. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token), [quantimodo_oauth2](../README.md#quantimodo_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_tracking_reminders_post**
> InlineResponse2001 v1_tracking_reminders_post(access_token=access_token, user_id=user_id, body=body)

Store a Tracking Reminder

This is to enable users to create reminders to track a variable with a default value at a specified frequency

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
api_instance = swagger_client.RemindersApi()
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
user_id = 56 # int | User's id (optional)
body = swagger_client.TrackingReminder() # TrackingReminder | TrackingReminder that should be stored (optional)

try: 
    # Store a Tracking Reminder
    api_response = api_instance.v1_tracking_reminders_post(access_token=access_token, user_id=user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemindersApi->v1_tracking_reminders_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **user_id** | **int**| User&#39;s id | [optional] 
 **body** | [**TrackingReminder**](TrackingReminder.md)| TrackingReminder that should be stored | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token), [quantimodo_oauth2](../README.md#quantimodo_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

