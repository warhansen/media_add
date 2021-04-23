import requests
import json

url = "http://media:7878/api/v3/movie/?apiKey=10fc753d66e048009a1d7fbc3a8f8053"
response = requests.get(url)
full_list = (response.json())

details = json.dumps(full_list)



