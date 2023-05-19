import json

with open("movies.json", "r") as save:
    movie_data = json.load(save)


for i in range(len(movie_data)):
    movie = movie_data[i]

    # if movie["pk"] == 144069:
    #     print(movie)
    for fields_key in movie["fields"]:
        if not movie["fields"][fields_key]:
            if fields_key == "poster_path":
                print(i)

movie_data.pop(3546)

for i in range(len(movie_data)):
    movie = movie_data[i]

    # if movie["pk"] == 144069:
    #     print(movie)
    for fields_key in movie["fields"]:
        if not movie["fields"][fields_key]:
            if fields_key == "poster_path":
                print(i)

with open(f'movies.json', 'w') as save:
    json.dump(movie_data, save)