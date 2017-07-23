# TrackingReminder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | id | [optional] 
**client_id** | **str** | clientId | [optional] 
**user_id** | **int** | ID of User | [optional] 
**variable_id** | **int** | Id for the variable to be tracked | 
**default_value** | **float** | Default value to use for the measurement when tracking | 
**reminder_start_time** | **str** | Earliest time of day at which reminders should appear in UTC HH:MM:SS format | [optional] 
**reminder_end_time** | **str** | Latest time of day at which reminders should appear in UTC HH:MM:SS format | [optional] 
**reminder_sound** | **str** | String identifier for the sound to accompany the reminder | [optional] 
**reminder_frequency** | **int** | Number of seconds between one reminder and the next | 
**pop_up** | **bool** | True if the reminders should appear as a popup notification | [optional] 
**sms** | **bool** | True if the reminders should be delivered via SMS | [optional] 
**email** | **bool** | True if the reminders should be delivered via email | [optional] 
**notification_bar** | **bool** | True if the reminders should appear in the notification bar | [optional] 
**latest_tracking_reminder_notification_reminder_time** | **datetime** | UTC ISO 8601 \&quot;YYYY-MM-DDThh:mm:ss\&quot;  timestamp for the reminder time of the latest tracking reminder notification that has been pre-emptively generated in the database | [optional] 
**last_tracked** | **datetime** | UTC ISO 8601 \&quot;YYYY-MM-DDThh:mm:ss\&quot;  timestamp for the last time a measurement was received for this user and variable | [optional] 
**start_tracking_date** | **str** | Earliest date on which the user should be reminded to track in YYYY-MM-DD format | [optional] 
**stop_tracking_date** | **str** | Latest date on which the user should be reminded to track in YYYY-MM-DD format | [optional] 
**updated_at** | **datetime** | When the record in the database was last updated. Use UTC ISO 8601 \&quot;YYYY-MM-DDThh:mm:ss\&quot;  datetime format. Time zone should be UTC and not local. | [optional] 
**variable_name** | **str** | Name of the variable to be used when sending measurements | [optional] 
**variable_category_name** | **str** | Name of the variable category to be used when sending measurements | [optional] 
**unit_abbreviated_name** | **str** | Abbreviated name of the unit to be used when sending measurements | [optional] 
**combination_operation** | **str** | The way multiple measurements are aggregated over time | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

