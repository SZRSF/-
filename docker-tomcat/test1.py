import requests

url="http://localhost"

for i in range(10):
	response = requests.get(url)
	print(response.text)
