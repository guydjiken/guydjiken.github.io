def generate_report(incident_list):
    report = []
    for incident in incident_list:
        report.append({
            'incident_id': incident['id'],
            'actions_taken': incident['actions'],
            'summary': incident['summary'],
        })
    print("Incident Report Generated:")
    for entry in report:
        print(f"Incident {entry['incident_id']}: {entry['summary']}")
        print(f"Actions Taken: {entry['actions_taken']}")
        print("----")

# Example: Incident details
incident_list = [
    {
        'id': 1,
        'actions': ['Blocked IP', 'Isolated Host', 'Terminated Process'],
        'summary': 'Detected malicious activity on Host-123 and responded.',
    },
    {
        'id': 2,
        'actions': ['Monitored traffic', 'No further action needed'],
        'summary': 'Low-priority alert, no action required.',
    }
]

generate_report(incident_list)
