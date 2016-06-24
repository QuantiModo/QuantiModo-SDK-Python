# Connection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | id | [optional] 
**user_id** | **int** | ID of user that owns this correlation | [optional] 
**connector_id** | **int** | The id for the connector data source for which the connection is connected | 
**connect_status** | **str** | Indicates whether a connector is currently connected to a service for a user. | [optional] 
**connect_error** | **str** | Error message if there is a problem with authorizing this connection. | [optional] 
**update_requested_at** | **datetime** | Time at which an update was requested by a user. | [optional] 
**update_status** | **str** | Indicates whether a connector is currently updated. | [optional] 
**update_error** | **str** | Indicates if there was an error during the update. | [optional] 
**last_successful_updated_at** | **datetime** | The time at which the connector was last successfully updated. | [optional] 
**created_at** | **datetime** | When the record was first created. Use ISO 8601 datetime format | [optional] 
**updated_at** | **datetime** | When the record in the database was last updated. Use ISO 8601 datetime format | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


