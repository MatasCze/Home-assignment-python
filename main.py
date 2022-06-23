import requests



word_list = []

def randomWordGenerator(word_count):
    #get response as a json object, extract the words and place them in a list
    if (word_count < 5) or (word_count > 20):
        print("Integer out of range")
    else:
        counter = 0
        while(counter < word_count):
            response = requests.get('https://random-words-api.vercel.app/word')
            json_response = response.json()
            word_from_json_response = json_response[0].get('word')
            word_list.append(word_from_json_response)
            counter += 1
        return word_list

try:
    print(randomWordGenerator(word_list))
except TypeError as e:
    print("Type error message: {}".format(e))
