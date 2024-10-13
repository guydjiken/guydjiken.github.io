# First, install the requests library if you don't have it already. It will help in making API calls.

# pip install requests

import requests

def query_chronicle_or_threat_service(domain):
    """
    Function to query VirusTotal for the given domain's reputation and associated threat intelligence data.
    """
    # Replace with your VirusTotal API key
    api_key = 'YOUR_VIRUSTOTAL_API_KEY'
    
    # VirusTotal API endpoint for domain report
    url = f"https://www.virustotal.com/vtapi/v2/domain/report"

    # Parameters to be sent to the API
    params = {
        'apikey': api_key,
        'domain': domain
    }

    # Perform the request
    response = requests.get(url, params=params)

    if response.status_code == 200:
        # Parse the response JSON
        threat_data = response.json()
        
        # Extract useful information from the response
        reputation = "malicious" if threat_data.get("positives", 0) > 0 else "clean"
        associated_ips = threat_data.get("resolutions", [])
        
        return {
            "domain": domain,
            "reputation": reputation,
            "associated_ips": associated_ips,
            "phishing_campaign": threat_data.get("categories", {}).get("phishing"),
            "malware": threat_data.get("detected_urls", [])
        }
    else:
        print(f"Error querying threat service: {response.status_code}")
        return None

# Example Usage
if __name__ == "__main__":
    domain = "signin.office365x24.com"
    threat_data = query_chronicle_or_threat_service(domain)
    
    if threat_data:
        print("Threat Intelligence Data:")
        print(threat_data)
