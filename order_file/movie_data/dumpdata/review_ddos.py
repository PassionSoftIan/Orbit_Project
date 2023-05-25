import requests, json, time, random

with open("movie_title.json", "r") as save:
    target_movie_list = json.load(save)

with open("token.json", "r") as save:
    create_user = json.load(save)

review_content = {
    "good":["재밌어요", "다시 보고 싶어요", "띵작이에요", "이동진이 좋아할거 같아요", "친구랑 다시 볼래요", ""],
    "bad":["별로에요", "아쉬워요", "그저 그래요", "재미없어요", "시간 낭비에요", "안경 안가져 갈걸 그랬어요", ""]
}

review_vote = {
    "good": [5, 4.5, 4.0],
    "bad": [0.5, 1, 1.5, 2]
}


def create_review():
    time.sleep(0.1)
    movie = random.choice(target_movie_list)
    movie = movie.get('id')
    user = random.choice(create_user)
    bad_or_good = random.choice(["good", "bad"])

    url = f"http://127.0.0.1:8000/api/v1/review/{movie}/"
    header = {
        "Authorization": f"Token {user}"
    }
    body = {
        "vote": random.choice(review_vote[bad_or_good]),
        "content": random.choice(review_content[bad_or_good])
    }

    response = requests.post(url=url, headers=header, json=body)
    response = response.json

    print(response)

start = time.time()
for i in range(100000):
    print(f"{i}번째 리뷰 작성중")
    print(time.time() - start, "초 경과")
    create_review()

print("최종적으로", time.time() - start, "초 경과 했습니다.")




