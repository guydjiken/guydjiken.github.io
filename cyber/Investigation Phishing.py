import hashlib

# Simulated email data for investigation
email_data = {
    "sender": "noreply@fakebank.com",  # Simulated suspicious sender
    "sender_name": "Fake Bank",        # Sender name mismatch
    "message_body": "Urgent! Please download the attached file.",  # Message body contains phishing indicators
    "attachment_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"  # Simulated file hash
}

# Malicious file hash from threat intelligence (known malicious hash)
malicious_hash = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"

# Function to investigate phishing email
def investigate_email(email_data):
    # Step 1: Check for mismatched sender details (e.g., "fake" in the domain or name)
    if "fake" in email_data["sender"] or "fake" in email_data["sender_name"].lower():
        print("Suspicious sender detected.")  # Log suspicious sender

    # Step 2: Analyze message body for common phishing indicators (like "urgent" or "important")
    if "urgent" in email_data["message_body"].lower():
        print("Phishing language detected in message body.")  # Log phishing language

    # Step 3: Check if the attachment's hash matches known malicious hash
    if email_data["attachment_hash"] == malicious_hash:
        print("Malicious file hash detected.")  # Log malicious file detection
    
    # Return a conclusion of the investigation
    return "Investigation complete."

# Perform the investigation and print the results
result = investigate_email(email_data)
print(result)
