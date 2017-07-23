# Measurement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variable_name** | **str** | Name of the variable for which we are creating the measurement records | 
**source_name** | **str** | Application or device used to record the measurement values | 
**start_time_string** | **str** | Start Time for the measurement event in UTC ISO 8601 \&quot;YYYY-MM-DDThh:mm:ss\&quot; | 
**start_time_epoch** | **int** | Seconds between the start of the event measured and 1970 (Unix timestamp) | [optional] 
**human_time** | [**HumanTime**](HumanTime.md) |  | [optional] 
**value** | **float** | Converted measurement value in requested unit | 
**original_value** | **int** | Original value as originally submitted | [optional] 
**originalunit_abbreviated_name** | **str** | Original Unit of measurement as originally submitted | [optional] 
**unit_abbreviated_name** | **str** | Abbreviated name for the unit of measurement | 
**note** | **str** | Note of measurement | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


