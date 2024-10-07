# Simulated alert ticket (this would typically be a system entry, here represented as a dictionary)
alert_ticket = {
    "ticket_id": 101,              # Unique ID for the ticket
    "status": "Investigating",      # Initial status of the ticket
    "comments": ""                 # Placeholder for comments
}

# Function to update the alert ticket based on the investigation results
def update_ticket(ticket, decision, comments):
    # Update the status of the ticket based on the decision to escalate or close
    ticket["status"] = "Escalated" if "Escalate" in decision else "Closed"
    # Add detailed comments to the ticket
    ticket["comments"] = comments
    return ticket

# Final comments based on the investigation findings
final_comments = """
Investigated phishing alert:
- Suspicious sender detected.
- Phishing language in message body.
- Malicious file hash verified.
"""

# Run the function to update the ticket with the final status and comments
updated_ticket = update_ticket(alert_ticket, decision, final_comments)
print(f"Updated Ticket: {updated_ticket}")
