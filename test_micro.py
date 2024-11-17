import requests


def test_microservice():
    # Make a request to the microservice
    response = requests.get("http://localhost:5000/api/quote", params={"user_id": 123, "progress_level": "50%"})
    if response.status_code == 200:
        data = response.json()
        print(f"Quote for user {data['user_id']}: {data['quote']}")
    else:
        print(f"Error: {response.status_code}, {response.text}")


if __name__ == '__main__':
    test_microservice()
