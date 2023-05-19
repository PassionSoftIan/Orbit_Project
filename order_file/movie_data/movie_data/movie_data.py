import requests, json, time

start = time.time()

def get_movie(page:int):
    global pk, genre_pk

    print(f"{page}번째 페이지 요청합니다.")

    URL = 'https://api.themoviedb.org/3/movie/popular'

    params = {
        'language': 'ko-KR',
        'page': str(page),
        'api_key': '9784d9d6e5d8a8e331ba3979590355d0',
    }

    response = requests.get(URL, params=params)
    response = response.json()

    for i in range(20):
        time.sleep(0.1)
        print(f"{page}번째 페이지 {i}번째 영화 요청합니다.")
        detail_URL = f'https://api.themoviedb.org/3/movie/{response["results"][i]["id"]}'
        detail_params = {
          'language': 'ko-KR',
          'api_key': '9784d9d6e5d8a8e331ba3979590355d0',
        }

        detail_response = requests.get(detail_URL, params=detail_params)
        detail_response = detail_response.json()


        data = {
            "model": "movies.Movie",
            "pk": response["results"][i]["id"],
            "fields": {
                "title": response['results'][i]['title'],
                "overview": response['results'][i]['overview'],
                "poster_path": response['results'][i]['poster_path'],
                "release_date": response['results'][i].get('release_date', ""),
                "vote_average": response['results'][i]['vote_average'],
                "genre": response['results'][i]['genre_ids'],
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


with open("movies.json", "r") as save:
    movie_data = json.load(save)

pk = 1
for i in range(263, 501):
    get_movie(i)

youtube_key = []
youtube_pk = 1

for movie in movie_data:
    id = movie['pk']

    video_URL = f'https://api.themoviedb.org/3/movie/{id}/videos'
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
                "movie": id,
                "key": video_info["key"]
            }
        }
        print(f"{youtube_pk}번째 영상 youtube 작업중")
        youtube_key.append(data)
        youtube_pk += 1
        with open(f'youtube.json', 'w') as save:
            json.dump(youtube_key, save)


still_cut = []
still_pk = 1

for movie in movie_data:
    id = movie['pk']

    img_URL = f'https://api.themoviedb.org/3/movie/{id}/images'
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
                "movie": id,
                "img_url": img_info['file_path']
            }
        }

        print(f"{still_pk}번째 still_cut 작업중")

        still_cut.append(data)
        still_pk += 1
        with open(f'still.json', 'w') as save:
            json.dump(still_cut, save)

print(time.time() - start)


