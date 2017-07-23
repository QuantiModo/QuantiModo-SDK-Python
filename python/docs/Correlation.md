# Correlation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_daily_low_cause** | **float** |  | [optional] 
**average_daily_high_cause** | **float** |  | [optional] 
**average_effect** | **float** |  | [optional] 
**average_effect_following_high_cause** | **float** |  | [optional] 
**average_effect_following_low_cause** | **float** |  | [optional] 
**average_effect_following_high_cause_explanation** | **str** |  | [optional] 
**average_effect_following_low_cause_explanation** | **str** |  | [optional] 
**average_vote** | **float** | Average Vote | [optional] 
**causality_factor** | **float** |  | [optional] 
**cause** | **str** | Variable name of the cause variable for which the user desires correlations. | 
**cause_variable_category_name** | **str** | Variable category of the cause variable. | [optional] 
**cause_changes** | **int** | Number of changes in the predictor variable (a.k.a the number of experiments) | [optional] 
**cause_variable_combination_operation** | **str** | The way cause measurements are aggregated | [optional] 
**cause_variable_image_url** | **str** |  | [optional] 
**cause_variable_ion_icon** | **str** | For use in Ionic apps | [optional] 
**cause_unit** | **str** | Unit of the predictor variable | [optional] 
**cause_variable_default_unit_id** | **int** | Unit Id of the predictor variable | [optional] 
**cause_variable_id** | **int** |  | [optional] 
**cause_variable_name** | **str** | Variable name of the cause variable for which the user desires correlations. | [optional] 
**correlation_coefficient** | **float** | Pearson correlation coefficient between cause and effect measurements | 
**created_at** | **datetime** | When the record was first created. Use UTC ISO 8601 \&quot;YYYY-MM-DDThh:mm:ss\&quot;  datetime format | [optional] 
**data_analysis** | **str** | How the data was analyzed | [optional] 
**data_sources** | **str** | How the data was obtained | [optional] 
**duration_of_action** | **float** | The amount of time over which a predictor/stimulus event can exert an observable influence on an outcome variable’s value. For instance, aspirin (stimulus/predictor) typically decreases headache severity for approximately four hours (duration of action) following the onset delay. | 
**effect** | **str** | Variable name of the effect variable for which the user desires correlations. | 
**effect_variable_category_name** | **str** | Variable category of the effect variable. | [optional] 
**effect_variable_image_url** | **str** |  | [optional] 
**effect_variable_ion_icon** | **str** | For use in Ionic apps | [optional] 
**effect_size** | **str** | Magnitude of the effects of a cause indicating whether it&#39;s practically meaningful. | [optional] 
**effect_variable_id** | **str** | Magnitude of the effects of a cause indicating whether it&#39;s practically meaningful. | [optional] 
**effect_variable_name** | **str** | Variable name of the effect variable for which the user desires correlations. | [optional] 
**gauge_image** | **str** | Illustrates the strength of the relationship | [optional] 
**image_url** | **str** | Large image for Facebook | [optional] 
**number_of_pairs** | **float** | Number of points that went into the correlation calculation | 
**onset_delay** | **float** | The amount of time in seconds that elapses after the predictor/stimulus event before the outcome as perceived by a self-tracker is known as the “onset delay”. For example, the “onset delay” between the time a person takes an aspirin (predictor/stimulus event) and the time a person perceives a change in their headache severity (outcome) is approximately 30 minutes. | 
**optimal_pearson_product** | **float** | Optimal Pearson Product | [optional] 
**outcome_data_sources** | **str** | original name of the cause. | [optional] 
**predictor_explanation** | **str** | HIGHER Remeron predicts HIGHER Overall Mood | [optional] 
**principal_investigator** | **str** | Mike Sinn | [optional] 
**qm_score** | **float** | Value representing the significance of the relationship as a function of crowdsourced insights, predictive strength, data quantity, and data quality | [optional] 
**reverse_correlation** | **float** | Correlation when cause and effect are reversed. For any causal relationship, the forward correlation should exceed the reverse correlation. | [optional] 
**significance_explanation** | **str** | Using a two-tailed t-test with alpha &#x3D; 0.05, it was determined that the change... | [optional] 
**statistical_significance** | **str** | A function of the effect size and sample size | [optional] 
**strength_level** | **str** | weak, moderate, strong | [optional] 
**study_abstract** | **str** | These data suggest with a high degree of confidence... | [optional] 
**study_background** | **str** | In order to reduce suffering through the advancement of human knowledge... | [optional] 
**study_design** | **str** | This study is based on data donated by one QuantiModo user... | [optional] 
**study_limitations** | **str** | As with any human experiment, it was impossible to control for all potentially confounding variables... | [optional] 
**study_link_dynamic** | **str** | Url for the interactive study within the web app | [optional] 
**study_link_facebook** | **str** | Url for sharing the study on Facebook | [optional] 
**study_link_google** | **str** | Url for sharing the study on Google+ | [optional] 
**study_link_twitter** | **str** | Url for sharing the study on Twitter | [optional] 
**study_link_static** | **str** | Url for sharing the statically rendered study on social media | [optional] 
**study_objective** | **str** | The objective of this study is to determine... | [optional] 
**study_results** | **str** | This analysis suggests that... | [optional] 
**study_title** | **str** | N1 Study HIGHER Remeron predicts HIGHER Overall Mood | [optional] 
**timestamp** | **float** | Time at which correlation was calculated | 
**updated_at** | **datetime** | When the record in the database was last updated. Use UTC ISO 8601 \&quot;YYYY-MM-DDThh:mm:ss\&quot;  datetime format. Time zone should be UTC and not local. | [optional] 
**user_vote** | **float** | User Vote | [optional] 
**value_predicting_high_outcome** | **float** | cause value that predicts an above average effect value (in default unit for cause variable) | [optional] 
**value_predicting_high_outcome_explanation** | **str** | Overall Mood, on average, 34% HIGHER after around 3.98mg Remeron | [optional] 
**value_predicting_low_outcome** | **float** | cause value that predicts a below average effect value (in default unit for cause variable) | [optional] 
**value_predicting_low_outcome_explanation** | **str** | Overall Mood, on average, 4% LOWER after around 0mg Remeron | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

