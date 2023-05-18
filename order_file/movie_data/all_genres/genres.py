import requests, json

def get_genre():
    URL = 'https://api.themoviedb.org/3/genre/movie/list'

    params = {
        'language':'ko-KR',
        'api_key':'9784d9d6e5d8a8e331ba3979590355d0',
    }

    response = requests.get(URL, params=params)
    response = response.json()

    # print(len(response["results"]))

    for genre in response["genres"]:
        data = {
            "model": "movies.Genre",
            "pk": genre["id"],
            "fields":{
                "name": genre["name"]
                }
            }
        
        save_data.append(data)
        


save_data = []
get_genre()
with open(f'movies.json', 'w') as save:
    json.dump(save_data, save)

