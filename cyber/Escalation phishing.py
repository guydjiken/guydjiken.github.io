# Simulated investigation findings based on the previous steps
investigation_findings = {
    "suspicious_sender": True,        # Flagged suspicious sender
    "phishing_language": True,        # Flagged phishing language in message body
    "malicious_attachment": True      # Malicious file detected based on the hash
}

# Function to decide whether to escalate or close the alert based on findings
def escalate_or_close(findings):
    # If any major indicators (suspicious sender, malicious attachment) are found, escalate the alert
    if findings["suspicious_sender"] or findings["malicious_attachment"]:
        return "Escalate the alert to Tier 2."  # Decision to escalate
    else:
        # If no major threats detected, close the alert as a false positive
        return "Close the alert as non-malicious."

# Run the function to decide whether to escalate or close the alert
decision = escalate_or_close(investigation_findings)
print(f"Decision: {decision}")
