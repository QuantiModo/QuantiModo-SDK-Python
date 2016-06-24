# Connector

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Connector ID number | 
**name** | **str** | Connector lowercase system name | 
**display_name** | **str** | Connector pretty display name | 
**image** | **str** | URL to the image of the connector logo | 
**get_it_url** | **str** | URL to a site where one can get this device or application | 
**connected** | **str** | True if the authenticated user has this connector enabled | 
**connect_instructions** | **str** | URL and parameters used when connecting to a service | 
**last_update** | **int** | Epoch timestamp of last sync | 
**total_measurements_in_last_update** | **int** | Number of measurements obtained during latest update | 
**no_data_yet** | **bool** | True if user has no measurements for this connector | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


