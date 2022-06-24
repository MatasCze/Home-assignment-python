import requests
import musicbrainzngs

musicbrainzngs.set_useragent(
    "MusicFetcherByWord", "1.0", contact="matasczepla@gmail.com")

def random_word_generator(word_count):
    #get response as a json object, extract the words and place them in a list
    word_list = []   
    counter = 0
    while(counter < word_count):
        response = requests.get('https://random-words-api.vercel.app/word')
        json_response = response.json()
        word_from_json_response = json_response[0].get('word')
        if word_from_json_response not in word_list:
            word_list.append(word_from_json_response)
            counter += 1
    word_list.sort()
    return word_list

def fetch_and_print_recordings(word_list):
    for word in word_list:
        result = musicbrainzngs.search_recordings("'" + word + "'")
        if (len(result.get('recording-list')) != 0):
            title = result.get('recording-list')[0].get('title')
            album = result.get('recording-list')[0].get('release-list')[0].get('release-group').get('title')
            artist = result.get('recording-list')[0].get('artist-credit')[0].get('name')
            print("For keyword {} found:\nArtist: {}\n Album: {}\n Title: {}\n".format(word, artist, album, title))
        else:
            print('For keyword ' + word + ' - no recording found!' + '\n')

if __name__ == '__main__':
    import sys
    user_input = sys.argv[1]
    try:
        user_input_word_count = int(user_input)
        if (user_input_word_count < 5) or (user_input_word_count > 20):
            print("Custom error message: integer out of range, must be between 5 and 20")
        else:
            try:       
                generated_words = random_word_generator(user_input_word_count)
                print(generated_words) 
                fetch_and_print_recordings(generated_words)
            except TypeError as e:
                print("Type error message: {}".format(e))
    except ValueError as e:
        print("Value error message: {}".format(e))
    