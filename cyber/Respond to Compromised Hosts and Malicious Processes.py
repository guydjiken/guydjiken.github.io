def respond_to_incident(host):
    # Investigate the compromised host for malicious activity
    if detect_malicious_process(host):
        isolate_host(host)
        terminate_process(host)
        delete_malicious_files(host)
    else:
        print(f"No malicious activity detected on {host['name']}.")

def detect_malicious_process(host):
    # Placeholder logic for detecting malicious processes
    if 'malicious_process' in host['processes']:
        return True
    return False

def isolate_host(host):
    # Simulate network isolation
    print(f"Isolating host {host['name']} from the network...")

def terminate_process(host):
    # Simulate terminating a malicious process
    print(f"Terminating malicious process on {host['name']}...")

def delete_malicious_files(host):
    # Simulate deleting malicious files from the host
    print(f"Deleting malicious files from {host['name']}...")

# Example: Respond to an incident on a compromised host
compromised_host = {
    'name': 'Host-123',
    'processes': ['malicious_process', 'normal_process']
}
respond_to_incident(compromised_host)
