import requests
import json

movie = '1918'
url = "http://media:7878/api/v3/movie/?apiKey=10fc753d66e048009a1d7fbc3a8f8053"

response = requests.get(url)
full_list = str(response.json())


if "\'title\': \'" + movie + "\'" in full_list:
    print("found the movie the", movie, ",please go to look in Emby as it has already been added")
else:
    print("did not find the movie", movie,)






