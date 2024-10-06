import requests

def investigate_ip(ip_address):
    # Use an API or open-source tool to check the IP address
    response = requests.get(f"https://api.ipscanner.com/check/{ip_address}")
    ip_data = response.json()
    
    if ip_data['status'] == 'malicious':
        block_ip(ip_address)
        escalate_ip(ip_address)
    else:
        print(f"IP {ip_address} is safe.")
        
def block_ip(ip_address):
    # Simulate firewall IP block
    print(f"Blocking IP {ip_address} on the firewall...")

def escalate_ip(ip_address):
    # Simulate escalation to a higher-tier analyst
    print(f"Escalating IP {ip_address} to Tier 2 for further investigation...")

# Example: Investigate a malicious IP
investigate_ip('221.181.185.159')
