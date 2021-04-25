import requests
import json

movie = '1917'
api_key = '10fc753d66e048009a1d7fbc3a8f8053'
radarr_url = 'http://media:7878'
api_url = radarr_url + "/api/v3/movie/?apiKey=" + api_key

response = requests.get(api_url)
full_list = str(response.json())


if "\'title\': \'" + movie + "\'" in full_list:
    print("found the movie the", movie, ",please go to look in Emby as it has already been added")
else:
    print("did not find the movie", movie,)






