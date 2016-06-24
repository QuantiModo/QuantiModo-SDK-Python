# swagger_client.PairsApi

All URIs are relative to *https://app.quantimo.do/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_pairs_csv_get**](PairsApi.md#v1_pairs_csv_get) | **GET** /v1/pairsCsv | Get pairs
[**v1_pairs_get**](PairsApi.md#v1_pairs_get) | **GET** /v1/pairs | Get pairs


# **v1_pairs_csv_get**
> list[Pairs] v1_pairs_csv_get(cause, effect, access_token=access_token, cause_source=cause_source, cause_unit=cause_unit, delay=delay, duration=duration, effect_source=effect_source, effect_unit=effect_unit, end_time=end_time, start_time=start_time, limit=limit, offset=offset, sort=sort)

Get pairs

Pairs cause measurements with effect measurements grouped over the duration of action after the onset delay.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PairsApi()
cause = 'cause_example' # str | Original variable name for the explanatory or independent variable
effect = 'effect_example' # str | Original variable name for the outcome or dependent variable
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
cause_source = 'cause_source_example' # str | Name of data source that the cause measurements should come from (optional)
cause_unit = 'cause_unit_example' # str | Abbreviated name for the unit cause measurements to be returned in (optional)
delay = 'delay_example' # str | Delay before onset of action (in seconds) from the cause variable settings. (optional)
duration = 'duration_example' # str | Duration of action (in seconds) from the cause variable settings. (optional)
effect_source = 'effect_source_example' # str | Name of data source that the effectmeasurements should come from (optional)
effect_unit = 'effect_unit_example' # str | Abbreviated name for the unit effect measurements to be returned in (optional)
end_time = 'end_time_example' # str | The most recent date (in epoch time) for which we should return measurements (optional)
start_time = 'start_time_example' # str | The earliest date (in epoch time) for which we should return measurements (optional)
limit = 56 # int | The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. (optional)
offset = 56 # int | Now suppose you wanted to show results 11-20. You'd set the offset to 10 and the limit to 10. (optional)
sort = 56 # int | Sort by given field. If the field is prefixed with `-, it will sort in descending order. (optional)

try: 
    # Get pairs
    api_response = api_instance.v1_pairs_csv_get(cause, effect, access_token=access_token, cause_source=cause_source, cause_unit=cause_unit, delay=delay, duration=duration, effect_source=effect_source, effect_unit=effect_unit, end_time=end_time, start_time=start_time, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PairsApi->v1_pairs_csv_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cause** | **str**| Original variable name for the explanatory or independent variable | 
 **effect** | **str**| Original variable name for the outcome or dependent variable | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **cause_source** | **str**| Name of data source that the cause measurements should come from | [optional] 
 **cause_unit** | **str**| Abbreviated name for the unit cause measurements to be returned in | [optional] 
 **delay** | **str**| Delay before onset of action (in seconds) from the cause variable settings. | [optional] 
 **duration** | **str**| Duration of action (in seconds) from the cause variable settings. | [optional] 
 **effect_source** | **str**| Name of data source that the effectmeasurements should come from | [optional] 
 **effect_unit** | **str**| Abbreviated name for the unit effect measurements to be returned in | [optional] 
 **end_time** | **str**| The most recent date (in epoch time) for which we should return measurements | [optional] 
 **start_time** | **str**| The earliest date (in epoch time) for which we should return measurements | [optional] 
 **limit** | **int**| The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. | [optional] 
 **offset** | **int**| Now suppose you wanted to show results 11-20. You&#39;d set the offset to 10 and the limit to 10. | [optional] 
 **sort** | **int**| Sort by given field. If the field is prefixed with &#x60;-, it will sort in descending order. | [optional] 

### Return type

[**list[Pairs]**](Pairs.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pairs_get**
> list[Pairs] v1_pairs_get(cause, effect, access_token=access_token, cause_source=cause_source, cause_unit=cause_unit, delay=delay, duration=duration, effect_source=effect_source, effect_unit=effect_unit, end_time=end_time, start_time=start_time, limit=limit, offset=offset, sort=sort)

Get pairs

Pairs cause measurements with effect measurements grouped over the duration of action after the onset delay.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PairsApi()
cause = 'cause_example' # str | Original variable name for the explanatory or independent variable
effect = 'effect_example' # str | Original variable name for the outcome or dependent variable
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
cause_source = 'cause_source_example' # str | Name of data source that the cause measurements should come from (optional)
cause_unit = 'cause_unit_example' # str | Abbreviated name for the unit cause measurements to be returned in (optional)
delay = 'delay_example' # str | Delay before onset of action (in seconds) from the cause variable settings. (optional)
duration = 'duration_example' # str | Duration of action (in seconds) from the cause variable settings. (optional)
effect_source = 'effect_source_example' # str | Name of data source that the effectmeasurements should come from (optional)
effect_unit = 'effect_unit_example' # str | Abbreviated name for the unit effect measurements to be returned in (optional)
end_time = 'end_time_example' # str | The most recent date (in epoch time) for which we should return measurements (optional)
start_time = 'start_time_example' # str | The earliest date (in epoch time) for which we should return measurements (optional)
limit = 56 # int | The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. (optional)
offset = 56 # int | Now suppose you wanted to show results 11-20. You'd set the offset to 10 and the limit to 10. (optional)
sort = 56 # int | Sort by given field. If the field is prefixed with `-, it will sort in descending order. (optional)

try: 
    # Get pairs
    api_response = api_instance.v1_pairs_get(cause, effect, access_token=access_token, cause_source=cause_source, cause_unit=cause_unit, delay=delay, duration=duration, effect_source=effect_source, effect_unit=effect_unit, end_time=end_time, start_time=start_time, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PairsApi->v1_pairs_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cause** | **str**| Original variable name for the explanatory or independent variable | 
 **effect** | **str**| Original variable name for the outcome or dependent variable | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **cause_source** | **str**| Name of data source that the cause measurements should come from | [optional] 
 **cause_unit** | **str**| Abbreviated name for the unit cause measurements to be returned in | [optional] 
 **delay** | **str**| Delay before onset of action (in seconds) from the cause variable settings. | [optional] 
 **duration** | **str**| Duration of action (in seconds) from the cause variable settings. | [optional] 
 **effect_source** | **str**| Name of data source that the effectmeasurements should come from | [optional] 
 **effect_unit** | **str**| Abbreviated name for the unit effect measurements to be returned in | [optional] 
 **end_time** | **str**| The most recent date (in epoch time) for which we should return measurements | [optional] 
 **start_time** | **str**| The earliest date (in epoch time) for which we should return measurements | [optional] 
 **limit** | **int**| The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. | [optional] 
 **offset** | **int**| Now suppose you wanted to show results 11-20. You&#39;d set the offset to 10 and the limit to 10. | [optional] 
 **sort** | **int**| Sort by given field. If the field is prefixed with &#x60;-, it will sort in descending order. | [optional] 

### Return type

[**list[Pairs]**](Pairs.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

