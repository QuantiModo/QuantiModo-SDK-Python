# swagger_client.PairsApi

All URIs are relative to *https://app.quantimo.do/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_pairs_csv_get**](PairsApi.md#v1_pairs_csv_get) | **GET** /v1/pairsCsv | Get pairs
[**v1_pairs_get**](PairsApi.md#v1_pairs_get) | **GET** /v1/pairs | Get pairs


# **v1_pairs_csv_get**
> list[Pairs] v1_pairs_csv_get(cause, effect, access_token=access_token, user_id=user_id, cause_source=cause_source, cause_unit=cause_unit, delay=delay, duration=duration, effect_source=effect_source, effect_unit=effect_unit, end_time=end_time, start_time=start_time, limit=limit, offset=offset, sort=sort)

Get pairs

Pairs cause measurements with effect measurements grouped over the duration of action after the onset delay.

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
api_instance = swagger_client.PairsApi()
cause = 'cause_example' # str | Original variable name for the explanatory or independent variable
effect = 'effect_example' # str | Original variable name for the outcome or dependent variable
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
user_id = 56 # int | User's id (optional)
cause_source = 'cause_source_example' # str | Name of data source that the cause measurements should come from (optional)
cause_unit = 'cause_unit_example' # str | Abbreviated name for the unit cause measurements to be returned in (optional)
delay = 'delay_example' # str | The amount of time in seconds that elapses after the predictor/stimulus event before the outcome as perceived by a self-tracker is known as the “onset delay”. For example, the “onset delay” between the time a person takes an aspirin (predictor/stimulus event) and the time a person perceives a change in their headache severity (outcome) is approximately 30 minutes. (optional)
duration = 'duration_example' # str | The amount of time over which a predictor/stimulus event can exert an observable influence on an outcome variable’s value. For instance, aspirin (stimulus/predictor) typically decreases headache severity for approximately four hours (duration of action) following the onset delay. (optional)
effect_source = 'effect_source_example' # str | Name of data source that the effectmeasurements should come from (optional)
effect_unit = 'effect_unit_example' # str | Abbreviated name for the unit effect measurements to be returned in (optional)
end_time = 'end_time_example' # str | The most recent date (in epoch time) for which we should return measurements (optional)
start_time = 'start_time_example' # str | The earliest date (in epoch time) for which we should return measurements (optional)
limit = 56 # int | The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. (optional)
offset = 56 # int | Since the maximum limit is 200 records, to get more than that you'll have to make multiple API calls and page through the results. To retrieve all the data, you can iterate through data by using the `limit` and `offset` query parameters.  For example, if you want to retrieve data from 61-80 then you can use a query with the following parameters, `imit=20&offset=60`. (optional)
sort = 56 # int | Sort by given field. If the field is prefixed with `-, it will sort in descending order. (optional)

try: 
    # Get pairs
    api_response = api_instance.v1_pairs_csv_get(cause, effect, access_token=access_token, user_id=user_id, cause_source=cause_source, cause_unit=cause_unit, delay=delay, duration=duration, effect_source=effect_source, effect_unit=effect_unit, end_time=end_time, start_time=start_time, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PairsApi->v1_pairs_csv_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cause** | **str**| Original variable name for the explanatory or independent variable | 
 **effect** | **str**| Original variable name for the outcome or dependent variable | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **user_id** | **int**| User&#39;s id | [optional] 
 **cause_source** | **str**| Name of data source that the cause measurements should come from | [optional] 
 **cause_unit** | **str**| Abbreviated name for the unit cause measurements to be returned in | [optional] 
 **delay** | **str**| The amount of time in seconds that elapses after the predictor/stimulus event before the outcome as perceived by a self-tracker is known as the “onset delay”. For example, the “onset delay” between the time a person takes an aspirin (predictor/stimulus event) and the time a person perceives a change in their headache severity (outcome) is approximately 30 minutes. | [optional] 
 **duration** | **str**| The amount of time over which a predictor/stimulus event can exert an observable influence on an outcome variable’s value. For instance, aspirin (stimulus/predictor) typically decreases headache severity for approximately four hours (duration of action) following the onset delay. | [optional] 
 **effect_source** | **str**| Name of data source that the effectmeasurements should come from | [optional] 
 **effect_unit** | **str**| Abbreviated name for the unit effect measurements to be returned in | [optional] 
 **end_time** | **str**| The most recent date (in epoch time) for which we should return measurements | [optional] 
 **start_time** | **str**| The earliest date (in epoch time) for which we should return measurements | [optional] 
 **limit** | **int**| The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. | [optional] 
 **offset** | **int**| Since the maximum limit is 200 records, to get more than that you&#39;ll have to make multiple API calls and page through the results. To retrieve all the data, you can iterate through data by using the &#x60;limit&#x60; and &#x60;offset&#x60; query parameters.  For example, if you want to retrieve data from 61-80 then you can use a query with the following parameters, &#x60;imit&#x3D;20&amp;offset&#x3D;60&#x60;. | [optional] 
 **sort** | **int**| Sort by given field. If the field is prefixed with &#x60;-, it will sort in descending order. | [optional] 

### Return type

[**list[Pairs]**](Pairs.md)

### Authorization

[access_token](../README.md#access_token), [quantimodo_oauth2](../README.md#quantimodo_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pairs_get**
> list[Pairs] v1_pairs_get(cause, effect, access_token=access_token, user_id=user_id, cause_source=cause_source, cause_unit=cause_unit, delay=delay, duration=duration, effect_source=effect_source, effect_unit=effect_unit, end_time=end_time, start_time=start_time, limit=limit, offset=offset, sort=sort)

Get pairs

Pairs cause measurements with effect measurements grouped over the duration of action after the onset delay.

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
api_instance = swagger_client.PairsApi()
cause = 'cause_example' # str | Original variable name for the explanatory or independent variable
effect = 'effect_example' # str | Original variable name for the outcome or dependent variable
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
user_id = 56 # int | User's id (optional)
cause_source = 'cause_source_example' # str | Name of data source that the cause measurements should come from (optional)
cause_unit = 'cause_unit_example' # str | Abbreviated name for the unit cause measurements to be returned in (optional)
delay = 'delay_example' # str | The amount of time in seconds that elapses after the predictor/stimulus event before the outcome as perceived by a self-tracker is known as the “onset delay”. For example, the “onset delay” between the time a person takes an aspirin (predictor/stimulus event) and the time a person perceives a change in their headache severity (outcome) is approximately 30 minutes. (optional)
duration = 'duration_example' # str | The amount of time over which a predictor/stimulus event can exert an observable influence on an outcome variable’s value. For instance, aspirin (stimulus/predictor) typically decreases headache severity for approximately four hours (duration of action) following the onset delay. (optional)
effect_source = 'effect_source_example' # str | Name of data source that the effectmeasurements should come from (optional)
effect_unit = 'effect_unit_example' # str | Abbreviated name for the unit effect measurements to be returned in (optional)
end_time = 'end_time_example' # str | The most recent date (in epoch time) for which we should return measurements (optional)
start_time = 'start_time_example' # str | The earliest date (in epoch time) for which we should return measurements (optional)
limit = 56 # int | The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. (optional)
offset = 56 # int | Since the maximum limit is 200 records, to get more than that you'll have to make multiple API calls and page through the results. To retrieve all the data, you can iterate through data by using the `limit` and `offset` query parameters.  For example, if you want to retrieve data from 61-80 then you can use a query with the following parameters, `imit=20&offset=60`. (optional)
sort = 56 # int | Sort by given field. If the field is prefixed with `-, it will sort in descending order. (optional)

try: 
    # Get pairs
    api_response = api_instance.v1_pairs_get(cause, effect, access_token=access_token, user_id=user_id, cause_source=cause_source, cause_unit=cause_unit, delay=delay, duration=duration, effect_source=effect_source, effect_unit=effect_unit, end_time=end_time, start_time=start_time, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PairsApi->v1_pairs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cause** | **str**| Original variable name for the explanatory or independent variable | 
 **effect** | **str**| Original variable name for the outcome or dependent variable | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **user_id** | **int**| User&#39;s id | [optional] 
 **cause_source** | **str**| Name of data source that the cause measurements should come from | [optional] 
 **cause_unit** | **str**| Abbreviated name for the unit cause measurements to be returned in | [optional] 
 **delay** | **str**| The amount of time in seconds that elapses after the predictor/stimulus event before the outcome as perceived by a self-tracker is known as the “onset delay”. For example, the “onset delay” between the time a person takes an aspirin (predictor/stimulus event) and the time a person perceives a change in their headache severity (outcome) is approximately 30 minutes. | [optional] 
 **duration** | **str**| The amount of time over which a predictor/stimulus event can exert an observable influence on an outcome variable’s value. For instance, aspirin (stimulus/predictor) typically decreases headache severity for approximately four hours (duration of action) following the onset delay. | [optional] 
 **effect_source** | **str**| Name of data source that the effectmeasurements should come from | [optional] 
 **effect_unit** | **str**| Abbreviated name for the unit effect measurements to be returned in | [optional] 
 **end_time** | **str**| The most recent date (in epoch time) for which we should return measurements | [optional] 
 **start_time** | **str**| The earliest date (in epoch time) for which we should return measurements | [optional] 
 **limit** | **int**| The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. | [optional] 
 **offset** | **int**| Since the maximum limit is 200 records, to get more than that you&#39;ll have to make multiple API calls and page through the results. To retrieve all the data, you can iterate through data by using the &#x60;limit&#x60; and &#x60;offset&#x60; query parameters.  For example, if you want to retrieve data from 61-80 then you can use a query with the following parameters, &#x60;imit&#x3D;20&amp;offset&#x3D;60&#x60;. | [optional] 
 **sort** | **int**| Sort by given field. If the field is prefixed with &#x60;-, it will sort in descending order. | [optional] 

### Return type

[**list[Pairs]**](Pairs.md)

### Authorization

[access_token](../README.md#access_token), [quantimodo_oauth2](../README.md#quantimodo_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

