def monitor_alerts(alert_queue):
    for alert in alert_queue:
        severity = alert['severity']
        # Prioritize alerts based on severity
        if severity in ['Critical', 'High']:
            investigate_alert(alert)
        else:
            # Log low or medium severity alerts
            log_alert(alert)

def investigate_alert(alert):
    log_data = alert['log_data']
    # Analyze logs, check firewall and endpoint data
    if suspicious_activity(log_data):
        escalate_alert(alert)
    else:
        resolve_alert(alert)

def suspicious_activity(log_data):
    # Placeholder logic for detecting suspicious activity
    if 'malicious_pattern' in log_data:
        return True
    return False

def escalate_alert(alert):
    print(f"Escalating alert {alert['id']} to Tier 2...")
    # Create incident ticket and escalate the alert
    create_ticket(alert)

def resolve_alert(alert):
    print(f"Resolving alert {alert['id']} as a false positive.")

def log_alert(alert):
    print(f"Logging low priority alert {alert['id']}...")

def create_ticket(alert):
    # Generate a ticket for the escalated alert
    print(f"Creating ticket for alert {alert['id']}...")

# Simulated alert queue
alert_queue = [
    {'id': 1, 'severity': 'Critical', 'log_data': 'malicious_pattern'},
    {'id': 2, 'severity': 'Low', 'log_data': 'normal_pattern'},
    {'id': 3, 'severity': 'High', 'log_data': 'malicious_pattern'},
]

monitor_alerts(alert_queue)
