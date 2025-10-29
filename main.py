import requests
response = requests.get("www.example.com")
print(response.get_status())
