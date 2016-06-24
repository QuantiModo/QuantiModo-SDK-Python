# swagger_client.MeasurementsApi

All URIs are relative to *https://app.quantimo.do/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_measurement_sources_get**](MeasurementsApi.md#v1_measurement_sources_get) | **GET** /v1/measurementSources | Get measurement sources
[**v1_measurement_sources_post**](MeasurementsApi.md#v1_measurement_sources_post) | **POST** /v1/measurementSources | Add a data source
[**v1_measurements_daily_get**](MeasurementsApi.md#v1_measurements_daily_get) | **GET** /v1/measurements/daily | Get daily measurements for this user
[**v1_measurements_delete_post**](MeasurementsApi.md#v1_measurements_delete_post) | **POST** /v1/measurements/delete | Delete a measurement
[**v1_measurements_get**](MeasurementsApi.md#v1_measurements_get) | **GET** /v1/measurements | Get measurements for this user
[**v1_measurements_post**](MeasurementsApi.md#v1_measurements_post) | **POST** /v1/measurements | Post a new set or update existing measurements to the database
[**v1_measurements_range_get**](MeasurementsApi.md#v1_measurements_range_get) | **GET** /v1/measurementsRange | Get measurements range for this user
[**v2_measurements_csv_get**](MeasurementsApi.md#v2_measurements_csv_get) | **GET** /v2/measurements/csv | Get Measurements CSV
[**v2_measurements_id_delete**](MeasurementsApi.md#v2_measurements_id_delete) | **DELETE** /v2/measurements/{id} | Delete Measurement
[**v2_measurements_id_get**](MeasurementsApi.md#v2_measurements_id_get) | **GET** /v2/measurements/{id} | Get Measurement
[**v2_measurements_id_put**](MeasurementsApi.md#v2_measurements_id_put) | **PUT** /v2/measurements/{id} | Update Measurement
[**v2_measurements_request_csv_post**](MeasurementsApi.md#v2_measurements_request_csv_post) | **POST** /v2/measurements/request_csv | Post Request for Measurements CSV
[**v2_measurements_request_pdf_post**](MeasurementsApi.md#v2_measurements_request_pdf_post) | **POST** /v2/measurements/request_pdf | Post Request for Measurements PDF
[**v2_measurements_request_xls_post**](MeasurementsApi.md#v2_measurements_request_xls_post) | **POST** /v2/measurements/request_xls | Post Request for Measurements XLS


# **v1_measurement_sources_get**
> MeasurementSource v1_measurement_sources_get()

Get measurement sources

Returns a list of all the apps from which measurement data is obtained.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.MeasurementsApi()

try: 
    # Get measurement sources
    api_response = api_instance.v1_measurement_sources_get()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MeasurementsApi->v1_measurement_sources_get: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MeasurementSource**](MeasurementSource.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_measurement_sources_post**
> v1_measurement_sources_post(body, access_token=access_token)

Add a data source

Add a life-tracking app or device to the QuantiModo list of data sources.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.MeasurementsApi()
body = swagger_client.MeasurementSource() # MeasurementSource | An array of names of data sources you want to add.
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)

try: 
    # Add a data source
    api_instance.v1_measurement_sources_post(body, access_token=access_token)
except ApiException as e:
    print "Exception when calling MeasurementsApi->v1_measurement_sources_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MeasurementSource**](MeasurementSource.md)| An array of names of data sources you want to add. | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_measurements_daily_get**
> Measurement v1_measurements_daily_get(variable_name, access_token=access_token, abbreviated_unit_name=abbreviated_unit_name, start_time=start_time, end_time=end_time, grouping_width=grouping_width, grouping_timezone=grouping_timezone, limit=limit, offset=offset, sort=sort)

Get daily measurements for this user

Measurements are any value that can be recorded like daily steps, a mood rating, or apples eaten. <br>Supported filter parameters:<br><ul><li><b>value</b> - Value of measurement</li><li><b>lastUpdated</b> - The time that this measurement was created or last updated in the UTC format \"YYYY-MM-DDThh:mm:ss\"</li></ul><br>

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.MeasurementsApi()
variable_name = 'variable_name_example' # str | Name of the variable you want measurements for
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
abbreviated_unit_name = 'abbreviated_unit_name_example' # str | The unit your want the measurements in (optional)
start_time = 'start_time_example' # str | The lower limit of measurements returned (Iso8601) (optional)
end_time = 'end_time_example' # str | The upper limit of measurements returned (Iso8601) (optional)
grouping_width = 56 # int | The time (in seconds) over which measurements are grouped together (optional)
grouping_timezone = 'grouping_timezone_example' # str | The time (in seconds) over which measurements are grouped together (optional)
limit = 56 # int | The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. (optional)
offset = 56 # int | Now suppose you wanted to show results 11-20. You'd set the offset to 10 and the limit to 10. (optional)
sort = 56 # int | Sort by given field. If the field is prefixed with `-, it will sort in descending order. (optional)

try: 
    # Get daily measurements for this user
    api_response = api_instance.v1_measurements_daily_get(variable_name, access_token=access_token, abbreviated_unit_name=abbreviated_unit_name, start_time=start_time, end_time=end_time, grouping_width=grouping_width, grouping_timezone=grouping_timezone, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MeasurementsApi->v1_measurements_daily_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_name** | **str**| Name of the variable you want measurements for | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **abbreviated_unit_name** | **str**| The unit your want the measurements in | [optional] 
 **start_time** | **str**| The lower limit of measurements returned (Iso8601) | [optional] 
 **end_time** | **str**| The upper limit of measurements returned (Iso8601) | [optional] 
 **grouping_width** | **int**| The time (in seconds) over which measurements are grouped together | [optional] 
 **grouping_timezone** | **str**| The time (in seconds) over which measurements are grouped together | [optional] 
 **limit** | **int**| The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. | [optional] 
 **offset** | **int**| Now suppose you wanted to show results 11-20. You&#39;d set the offset to 10 and the limit to 10. | [optional] 
 **sort** | **int**| Sort by given field. If the field is prefixed with &#x60;-, it will sort in descending order. | [optional] 

### Return type

[**Measurement**](Measurement.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_measurements_delete_post**
> CommonResponse v1_measurements_delete_post(body)

Delete a measurement

Delete a previously submitted measurement

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.MeasurementsApi()
body = swagger_client.MeasurementDelete() # MeasurementDelete | The startTime and variableId of the measurement to be deleted.

try: 
    # Delete a measurement
    api_response = api_instance.v1_measurements_delete_post(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MeasurementsApi->v1_measurements_delete_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MeasurementDelete**](MeasurementDelete.md)| The startTime and variableId of the measurement to be deleted. | 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_measurements_get**
> Measurement v1_measurements_get(access_token=access_token, variable_name=variable_name, variable_category_name=variable_category_name, source=source, value=value, last_updated=last_updated, unit=unit, start_time=start_time, created_at=created_at, updated_at=updated_at, end_time=end_time, grouping_width=grouping_width, grouping_timezone=grouping_timezone, limit=limit, offset=offset, sort=sort)

Get measurements for this user

Measurements are any value that can be recorded like daily steps, a mood rating, or apples eaten. <br>Supported filter parameters:<br><ul><li><b>value</b> - Value of measurement</li><li><b>lastUpdated</b> - The time that this measurement was created or last updated in the UTC format \"YYYY-MM-DDThh:mm:ss\"</li></ul><br>

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.MeasurementsApi()
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
variable_name = 'variable_name_example' # str | Name of the variable you want measurements for (optional)
variable_category_name = 'variable_category_name_example' # str | Name of the variable category you want measurements for (optional)
source = 'source_example' # str | Name of the source you want measurements for (supports exact name match only) (optional)
value = 'value_example' # str | Value of measurement (optional)
last_updated = 'last_updated_example' # str | The time that this measurement was created or last updated in the format \"YYYY-MM-DDThh:mm:ss\" (optional)
unit = 'unit_example' # str | The unit you want the measurements returned in (optional)
start_time = 'start_time_example' # str | The lower limit of measurements returned (Epoch) (optional)
created_at = 'created_at_example' # str | The time the measurement record was first created in the format YYYY-MM-DDThh:mm:ss. Time zone should be UTC and not local. (optional)
updated_at = 'updated_at_example' # str | The time the measurement record was last changed in the format YYYY-MM-DDThh:mm:ss. Time zone should be UTC and not local. (optional)
end_time = 'end_time_example' # str | The upper limit of measurements returned (Epoch) (optional)
grouping_width = 56 # int | The time (in seconds) over which measurements are grouped together (optional)
grouping_timezone = 'grouping_timezone_example' # str | The time (in seconds) over which measurements are grouped together (optional)
limit = 56 # int | The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. (optional)
offset = 56 # int | Now suppose you wanted to show results 11-20. You'd set the offset to 10 and the limit to 10. (optional)
sort = 56 # int | Sort by given field. If the field is prefixed with `-, it will sort in descending order. (optional)

try: 
    # Get measurements for this user
    api_response = api_instance.v1_measurements_get(access_token=access_token, variable_name=variable_name, variable_category_name=variable_category_name, source=source, value=value, last_updated=last_updated, unit=unit, start_time=start_time, created_at=created_at, updated_at=updated_at, end_time=end_time, grouping_width=grouping_width, grouping_timezone=grouping_timezone, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MeasurementsApi->v1_measurements_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **variable_name** | **str**| Name of the variable you want measurements for | [optional] 
 **variable_category_name** | **str**| Name of the variable category you want measurements for | [optional] 
 **source** | **str**| Name of the source you want measurements for (supports exact name match only) | [optional] 
 **value** | **str**| Value of measurement | [optional] 
 **last_updated** | **str**| The time that this measurement was created or last updated in the format \&quot;YYYY-MM-DDThh:mm:ss\&quot; | [optional] 
 **unit** | **str**| The unit you want the measurements returned in | [optional] 
 **start_time** | **str**| The lower limit of measurements returned (Epoch) | [optional] 
 **created_at** | **str**| The time the measurement record was first created in the format YYYY-MM-DDThh:mm:ss. Time zone should be UTC and not local. | [optional] 
 **updated_at** | **str**| The time the measurement record was last changed in the format YYYY-MM-DDThh:mm:ss. Time zone should be UTC and not local. | [optional] 
 **end_time** | **str**| The upper limit of measurements returned (Epoch) | [optional] 
 **grouping_width** | **int**| The time (in seconds) over which measurements are grouped together | [optional] 
 **grouping_timezone** | **str**| The time (in seconds) over which measurements are grouped together | [optional] 
 **limit** | **int**| The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. | [optional] 
 **offset** | **int**| Now suppose you wanted to show results 11-20. You&#39;d set the offset to 10 and the limit to 10. | [optional] 
 **sort** | **int**| Sort by given field. If the field is prefixed with &#x60;-, it will sort in descending order. | [optional] 

### Return type

[**Measurement**](Measurement.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_measurements_post**
> v1_measurements_post(body, access_token=access_token)

Post a new set or update existing measurements to the database

You can submit or update multiple measurements in a \"measurements\" sub-array.  If the variable these measurements correspond to does not already exist in the database, it will be automatically added.  The request body should look something like [{\"measurements\":[{\"startTime\":1439389320,\"value\":\"3\"}, {\"startTime\":1439389319,\"value\":\"2\"}],\"name\":\"Acne (out of 5)\",\"source\":\"QuantiModo\",\"category\":\"Symptoms\",\"combinationOperation\":\"MEAN\",\"unit\":\"/5\"}]

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.MeasurementsApi()
body = swagger_client.MeasurementSet() # MeasurementSet | An array of measurements you want to insert.
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)

try: 
    # Post a new set or update existing measurements to the database
    api_instance.v1_measurements_post(body, access_token=access_token)
except ApiException as e:
    print "Exception when calling MeasurementsApi->v1_measurements_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MeasurementSet**](MeasurementSet.md)| An array of measurements you want to insert. | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_measurements_range_get**
> MeasurementRange v1_measurements_range_get(sources=sources, user=user)

Get measurements range for this user

Get Unix time-stamp (epoch time) of the user's first and last measurements taken.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.MeasurementsApi()
sources = 'sources_example' # str | Enter source name to limit to specific source (varchar) (optional)
user = 56 # int | If not specified, uses currently logged in user (bigint) (optional)

try: 
    # Get measurements range for this user
    api_response = api_instance.v1_measurements_range_get(sources=sources, user=user)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MeasurementsApi->v1_measurements_range_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sources** | **str**| Enter source name to limit to specific source (varchar) | [optional] 
 **user** | **int**| If not specified, uses currently logged in user (bigint) | [optional] 

### Return type

[**MeasurementRange**](MeasurementRange.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_measurements_csv_get**
> file v2_measurements_csv_get(access_token=access_token)

Get Measurements CSV

Download a CSV containing all user measurements

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: quantimodo_oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.MeasurementsApi()
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)

try: 
    # Get Measurements CSV
    api_response = api_instance.v2_measurements_csv_get(access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MeasurementsApi->v2_measurements_csv_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 

### Return type

[**file**](file.md)

### Authorization

[quantimodo_oauth2](../README.md#quantimodo_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_measurements_id_delete**
> InlineResponse20012 v2_measurements_id_delete(id, access_token=access_token)

Delete Measurement

Delete Measurement

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: quantimodo_oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.MeasurementsApi()
id = 56 # int | id of Measurement
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)

try: 
    # Delete Measurement
    api_response = api_instance.v2_measurements_id_delete(id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MeasurementsApi->v2_measurements_id_delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of Measurement | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[quantimodo_oauth2](../README.md#quantimodo_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_measurements_id_get**
> InlineResponse20011 v2_measurements_id_get(id, access_token=access_token)

Get Measurement

Get Measurement

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: quantimodo_oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.MeasurementsApi()
id = 56 # int | id of Measurement
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)

try: 
    # Get Measurement
    api_response = api_instance.v2_measurements_id_get(id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MeasurementsApi->v2_measurements_id_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of Measurement | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[quantimodo_oauth2](../README.md#quantimodo_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_measurements_id_put**
> InlineResponse20012 v2_measurements_id_put(id, access_token=access_token, body=body)

Update Measurement

Update Measurement

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: quantimodo_oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.MeasurementsApi()
id = 56 # int | id of Measurement
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
body = swagger_client.Measurement() # Measurement | Measurement that should be updated (optional)

try: 
    # Update Measurement
    api_response = api_instance.v2_measurements_id_put(id, access_token=access_token, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MeasurementsApi->v2_measurements_id_put: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of Measurement | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **body** | [**Measurement**](Measurement.md)| Measurement that should be updated | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[quantimodo_oauth2](../README.md#quantimodo_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_measurements_request_csv_post**
> int v2_measurements_request_csv_post(access_token=access_token)

Post Request for Measurements CSV

Use this endpoint to schedule a CSV export containing all user measurements to be emailed to the user within 24 hours.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: quantimodo_oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.MeasurementsApi()
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)

try: 
    # Post Request for Measurements CSV
    api_response = api_instance.v2_measurements_request_csv_post(access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MeasurementsApi->v2_measurements_request_csv_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 

### Return type

**int**

### Authorization

[quantimodo_oauth2](../README.md#quantimodo_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_measurements_request_pdf_post**
> int v2_measurements_request_pdf_post(access_token=access_token)

Post Request for Measurements PDF

Use this endpoint to schedule a PDF export containing all user measurements to be emailed to the user within 24 hours.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: quantimodo_oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.MeasurementsApi()
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)

try: 
    # Post Request for Measurements PDF
    api_response = api_instance.v2_measurements_request_pdf_post(access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MeasurementsApi->v2_measurements_request_pdf_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 

### Return type

**int**

### Authorization

[quantimodo_oauth2](../README.md#quantimodo_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_measurements_request_xls_post**
> int v2_measurements_request_xls_post(access_token=access_token)

Post Request for Measurements XLS

Use this endpoint to schedule a XLS export containing all user measurements to be emailed to the user within 24 hours.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: quantimodo_oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.MeasurementsApi()
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)

try: 
    # Post Request for Measurements XLS
    api_response = api_instance.v2_measurements_request_xls_post(access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MeasurementsApi->v2_measurements_request_xls_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 

### Return type

**int**

### Authorization

[quantimodo_oauth2](../README.md#quantimodo_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

