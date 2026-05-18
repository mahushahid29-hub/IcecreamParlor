import requests

url = "http://20.17.145.40"

response = requests.get(url)

print("Status Code:", response.status_code)

assert response.status_code == 200

print("API Base Test Passed")