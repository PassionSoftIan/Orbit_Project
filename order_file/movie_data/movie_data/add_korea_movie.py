import requests, json, time

with open("movies.json", "r") as save:
    movie_data = json.load(save)

with open("still.json", "r") as save:
    still_cut = json.load(save)

with open("youtube.json", "r") as save:
    youtube_key = json.load(save)


movie_id_list = [242452,
                313108,
                346646,
                45035,
                10355,
                26955,
                124157,
                381375,
                37870,
                165213,
                89623,
                38015,
                574302,
                281780,
                ]

def movie_detail(movie_id):
    global youtube_pk, still_pk

    time.sleep(0.1)
    print(f"{movie_id}영화를 저장합니다.")
    detail_URL = f'https://api.themoviedb.org/3/movie/{movie_id}'
    detail_params = {
        'language': 'ko-KR',
        'api_key': '9784d9d6e5d8a8e331ba3979590355d0',
    }

    detail_response = requests.get(detail_URL, params=detail_params)
    detail_response = detail_response.json()


    data = {
        "model": "movies.Movie",
        "pk": movie_id,
        "fields": {
            "title": detail_response['title'],
            "overview": detail_response['overview'],
            "poster_path": detail_response['poster_path'],
            "release_date": detail_response.get('release_date', ""),
            "vote_average": detail_response['vote_average'],
            "genre": list(map(lambda x: x["id"], detail_response['genres'])),
            "tagline": detail_response['tagline'],
            "revenue": detail_response['revenue'],
        }
    }

    for key in data["fields"]:
        if key == "tagline":
            continue

        if data['fields'][key] == "":
            print(page, i)
            break
    else:
        movie_data.append(data)
        with open(f'movies.json', 'w') as save:
            json.dump(movie_data, save)

    video_URL = f'https://api.themoviedb.org/3/movie/{movie_id}/videos'
    video_params = {
        'language': 'ko-KR',
        'api_key': '9784d9d6e5d8a8e331ba3979590355d0',
    }

    video_response = requests.get(video_URL, params=video_params)
    video_response = video_response.json()

    for video_info in video_response['results']:
        if video_info['site'] != "YouTube":
            continue
        data = {
            "model": "movies.youtube_key",
            "pk": youtube_pk,
            "fields": {
                "movie": movie_id,
                "key": video_info["key"]
            }
        }
        print(f"{youtube_pk}번째 영상 youtube 작업중")
        youtube_key.append(data)
        youtube_pk += 1
        print(youtube_key)
        with open(f'youtube.json', 'w') as save:
            json.dump(youtube_key, save)

    img_URL = f'https://api.themoviedb.org/3/movie/{movie_id}/images'
    img_params = {
        'api_key': '9784d9d6e5d8a8e331ba3979590355d0',
    }

    img_response = requests.get(img_URL, params=img_params)
    img_response = img_response.json()

    for i in range(min(3, len(img_response["backdrops"]))):
        img_info = img_response["backdrops"][i]
        data = {
            "model": "movies.stillcut",
            "pk": still_pk,
            "fields": {
                "movie": movie_id,
                "img_url": img_info['file_path']
            }
        }

        print(f"{still_pk}번째 still_cut 작업중")

        still_cut.append(data)
        still_pk += 1
        with open(f'still.json', 'w') as save:
            json.dump(still_cut, save)



still_pk = len(still_cut) + 1
youtube_pk = len(youtube_key) + 1

for movie_id in movie_id_list:
    movie_detail(movie_id)
