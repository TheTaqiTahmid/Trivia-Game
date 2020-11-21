import requests
import json
import random
import html
import pprint

url = 'https://opentdb.com/api.php?amount=1&category=19&difficulty=easy&type=multiple'
# print(r.status_code)
# question = json.loads(r.text)
# print(question)
# pprint.pprint(question)
# category = {'General Knowledge': 9, 'Science: Mathematics': 19, 'Science: Computer': 18}
category = {1: ('General Knowledge', 9), 2: ('Science: Mathematics', 19), 3: ('Science: Computer', 18), 4: ('Entertainment: Film', 11)}
j = 1
for i in category:
    print(str(j) + '. ' + category[i][0])
    j += 1
category_response = False
while category_response is False:
    category_chosen = input('\nPlease select your category: ')
    try:
        category_chosen = int(category_chosen)
        if category_chosen > 4 or category_chosen <= 0:
            print('Please enter a valid integer')
        else:
            category_response = True
    except:
        print('Please enter an integer value')

new_url = 'https://opentdb.com/api.php?amount=1&category='+str(category[category_chosen][1])+'&difficulty=easy&type=multiple'

result = {'correct': 0, 'incorrect': 0, 'total': 0}
endgame = ''
while endgame.lower() != 'quit':
    r = requests.get(new_url)
    n = 1
    if r.status_code != 200:
        endgame = input("There was a problem at the server. Press any keys to try again or write quit to exit: ")
    else:
        data = json.loads(r.text)
        quiz_question = html.unescape(data['results'][0]['question'])
        quiz_answer = html.unescape(data['results'][0]['incorrect_answers'])
        corr_ans = html.unescape(data['results'][0]['correct_answer'])
        quiz_answer.append(corr_ans)
        random.shuffle(quiz_answer)
        print(quiz_question + '\n')
        for answer in quiz_answer:
            print(str(n) + '. ' + answer)
            n += 1
        valid_ans = False
        while not valid_ans:
            response = input("Please insert your response: ")
            try:
                response = int(response)
                if response >= 5 or response <= 0:
                    print("Please enter a valid integer")
                else:
                    valid_ans = True
            except:
                print("Please insert an integer value: ")

        if quiz_answer[int(response) - 1] == corr_ans:
            print("You have answered correctly!")
            result['correct'] += 1
            result['total'] += 1
        else:
            print("Sorry! your answer is wrong")
            result['incorrect'] += 1
            result['total'] += 1
    endgame = input("Press any keys to continue or if you want to exit write 'quit': ")

print("Thanks for playing \n" + "Here is you result, total quiz: {}, correct answer: {}, incorrect answer: {}".format(
    result['total'], result['correct'], result['incorrect']))
print("You have answered {:.2f}% of the questions correctly!".format(result['correct'] / result['total'] * 100))
