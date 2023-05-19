import requests

YOUR_YELP_API_KEY_HERE = "----"

def get_restaurants(keywords):
    querystring = {
        "location": "irvine",
        "term": keywords
    }

    url = "https://api.yelp.com/v3/businesses/search"
    headers = {"Authorization": "Bearer " + YOUR_YELP_API_KEY_HERE}
    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    return response.json()
