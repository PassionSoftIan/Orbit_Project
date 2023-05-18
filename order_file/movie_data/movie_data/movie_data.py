import requests, json

def get_movie(page:int):
    global pk, genre_pk

    URL = 'https://api.themoviedb.org/3/discover/movie'

    params = {
        'include_video':'false',
        'language':'ko-KR',
        'page':str(page),
        'sort_by':'vote_average.desc',
        'vote_count.gte': '200',
        'api_key':'9784d9d6e5d8a8e331ba3979590355d0',
    }

    response = requests.get(URL, params=params)
    response = response.json()

    # print(len(response["results"]))

    for i in range(20):
        data = {
            "model": "movies.Movie",
            "pk": pk,
            "fields":{
                "title": response['results'][i]['title'],
                "overview":response['results'][i]['overview'],
                "poster_path":response['results'][i]['poster_path'],
                "release_date":response['results'][i]['release_date'],
                "vote_average":response['results'][i]['vote_average'],
                "popularity":response['results'][i]['popularity'],
                "genre":response['results'][i]['genre_ids']
                }
            }


        for key in data["fields"]:
            if data['fields'][key] == "":
                print(page, i)
                break
        else:
            save_data.append(data)
            pk += 1



save_data = []

pk = 1
for i in range(1, 501):
    get_movie(i)

with open(f'movies.json', 'w') as save:
    json.dump(save_data, save)

