import requests


INPUT_URL = input("URL: ")

while INPUT_URL != "":

    url = 'http://127.0.0.1:5000/summarize'

    data = {
        "url": INPUT_URL
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:

        print("Summary:", response.json()['summary'])

    else:

        print("Error:", response.json()['error'])

    print()
    INPUT_URL = input("URL: ")

print("Finish")
