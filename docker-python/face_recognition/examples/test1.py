import requests

url="http://10.0.2.15"

for i in range(10):
	response = requests.get(url)
	print(response.text)