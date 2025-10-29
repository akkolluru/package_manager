import requests
response = requests.get("www.google.com")
print(response.get_status())
