from yelp import get_restaurants
from speech_listener import get_audio_snippet
from speech_parser import parse_text

def main(): 
    # get user audio
    user_audio = get_audio_snippet()

    # parsed user text
    parsed_text = parse_text(user_audio)
    formatted_input = " ".join(parsed_text)

    restaurant_data = get_restaurants(formatted_input)

    for restaurant in restaurant_data['businesses']:
        print(restaurant['name'])

if __name__ == "__main__":
    main()
