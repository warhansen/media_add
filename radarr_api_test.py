import requests

movie = '1917'
api_key = '10fc753d66e048009a1d7fbc3a8f8053'
radarr_url = 'http://media:7878'
api_url = radarr_url + "/api/v3/movie/?apiKey=" + api_key
quality_profile_id = 'English-Movies-1080p'

getting = requests.get(api_url)
full_list = str(getting.json())
params = {'title': movie, 'QualityProfileId': quality_profile_id}


def add_movie(movie_name):
    if "\'title\': \'" + movie_name + "\'" in full_list:
        print("Found the movie the", movie_name, ",please go to look in Emby as it has already been added.")
    else:
        print("Did not find the movie", movie_name, ", it will now be added.")

    requests.post(api_url, params)


add_movie(movie)




