import requests, json, time

def get_movie_title():

    url = "http://127.0.0.1:8000/api/v1/movie/alltitle/"

    response = requests.get(url=url)
    response = response.json()

    with open("movie_title.json", "w") as save:
        json.dump(response, save)

get_movie_title()