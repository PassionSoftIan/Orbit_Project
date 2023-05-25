import requests, json, time

def signup(i):
    username = f"user{i}"
    password = "useruser"

    url = "http://127.0.0.1:8000/accounts/signup/"
    data = {
        "username": username,
        "password1": password,
        "password2": password,
        "nick_name": username
    }

    response = requests.post(url=url, data=data)
    response = response.json()

    key.append(response['key'])



key = []

for i in range(1, 11):
    signup(i)



with open("token.json", "w") as save:
    json.dump(key, save)