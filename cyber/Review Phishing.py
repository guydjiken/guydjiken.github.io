# Step 1: Review the Playbook based on alert type and severity
def review_playbook(alert_type, alert_severity):
    # If the alert is of type 'phishing' and has medium or high severity, follow the phishing playbook
    if alert_type == "phishing" and alert_severity in ["Medium", "High"]:
        return "Follow phishing playbook: Investigate sender details, analyze message body, check attachments."
    else:
        # For low severity, no immediate action is required
        return "Low severity: Monitor alert. No immediate action required."

# Example input
alert_type = "phishing"
alert_severity = "High"

# Run the function to simulate reviewing the playbook
playbook_instructions = review_playbook(alert_type, alert_severity)
print(playbook_instructions)
