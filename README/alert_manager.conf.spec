[settings]
	* If you do not specify an entry for each attribute, the event manager will use the default value.

index	= <index_name>
	* Name of the index where the alert meta events will be written to
	* Defaults to "alerts"

incident_list_length = <integer>
	* Number of events shown in list in the incident posture dashboard
	* Defaults to 10
	
default_owner = <owner_name>
	* Default owner for new alerts
	* Defaults to "unassigned"

default_impact = <impact_name>
        * Fallback impact for new incidents if the alert handler is unable to parse it
        * Defaults to "low"

default_urgency = <urgency_name>
        * Fallback urgency for new incidents if the alert handler is unable to parse it from results
        * Defaults to "low"

default_priority = <priority_name>
        * Fallback priority for new incidents if the alert handler is unable to parse it
        * Defaults to "low"

user_directories = [both | builtin | alert_manager]
	* Configure which user directories are enabled
	* Defaults to both
