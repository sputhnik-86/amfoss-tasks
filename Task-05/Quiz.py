import requests
import time

def get_questions():
    url = "https://opentdb.com/api.php?amount=5&type=boolean"
    response = requests.get(url)
    data = response.json()
    return data["results"]

def play_quiz():
    questions = get_questions()
    score = 0
    question_number = 1

    for q in questions:
        print("Question", question_number, ":", q['question'])
        print("Type True or False:")
        start = time.time()
        answer = input("Your answer: ")
        end = time.time()
        
        if end - start > 15:
            print("Time up")
        else:
            if answer.lower() == q['correct_answer'].lower():
                print("Correct")
                score += 1
            else:
                print("Wrong , Correct answer is", q['correct_answer'])
        question_number += 1
    print("Game Over , Your score:", score, "/", len(questions))
