# Pseudo Python code for phishing email investigation task
#
#The review_alert() function parses the phishing alert to extract email body and sender information and checks if the suspicious domain is present.
#The verify_domain() function queries a threat intelligence service to check the reputation of the suspicious domain.
#document_findings() function logs the email details, sender info, domain verification, and any Indicators of Compromise (IOCs) to an incident handler's journal.

def review_alert(alert):
    """
    Function to review the alert and extract relevant information.
    """
    # Parse the alert to understand the nature of the phishing email
    email_content = alert.get("email_body")
    sender_info = alert.get("sender_info")
    domain_found = False
    
    print("Reviewing phishing alert...")

    # Check if the alert contains the suspicious domain
    if "signin.office365x24.com" in email_content:
        domain_found = True
    
    return email_content, sender_info, domain_found

def verify_domain(domain):
    """
    Function to verify the suspicious domain using a threat intelligence service.
    """
    # Use a threat intelligence API (e.g., VirusTotal) to verify domain
    threat_intel_response = query_threat_intel_service(domain)
    
    # Check if domain is flagged as malicious
    if threat_intel_response.get("reputation") == "malicious":
        return True
    return False

def document_findings(email_content, sender_info, domain_verification, IOCs):
    """
    Function to document the initial findings, including email details, sender, and IOCs.
    """
    findings = {
        "email_content": email_content,
        "sender": sender_info,
        "domain_verification": domain_verification,
        "indicators_of_compromise": IOCs
    }
    
    # Log or save findings to incident handler's journal
    save_to_incident_journal(findings)

def main():
    # Sample alert with phishing email details
    alert = {
        "email_body": "Click here to access your Office365 account: signin.office365x24.com",
        "sender_info": "phisher@example.com"
    }
    
    # Step 1: Review the phishing alert
    email_content, sender_info, domain_found = review_alert(alert)
    
    # Step 2: Identify and verify the suspicious domain
    if domain_found:
        domain_verification = verify_domain("signin.office365x24.com")
    else:
        domain_verification = False

    # Step 3: Document findings including Indicators of Compromise (IOCs)
    IOCs = ["malicious_domain: signin.office365x24.com", "phishing_email_from: phisher@example.com"]
    document_findings(email_content, sender_info, domain_verification, IOCs)

if __name__ == "__main__":
    main()


