# Measurement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variable** | **str** | ORIGINAL Name of the variable for which we are creating the measurement records | 
**source** | **str** | Application or device used to record the measurement values | 
**start_time** | **str** | Start Time for the measurement event in ISO 8601 | 
**human_time** | [**HumanTime**](HumanTime.md) | Start Time for the measurement event in ISO 8601 | [optional] 
**value** | **float** | Converted measurement value in requested unit | 
**unit** | **str** | Unit of measurement as requested in GET request | 
**original_value** | **int** | Original value | [optional] 
**stored_value** | **float** | Measurement value in the unit as orignally submitted | [optional] 
**stored_abbreviated_unit_name** | **str** | Unit of measurement as originally submitted | [optional] 
**original_abbreviated_unit_name** | **str** | Original Unit of measurement as originally submitted | [optional] 
**abbreviated_unit_name** | **str** | Unit of measurement as originally submitted | [optional] 
**note** | **str** | Note of measurement | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


