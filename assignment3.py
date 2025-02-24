import json
import csv


def load_questions(filename="C:/Users/Admin/OneDrive/Рабочий стол/Assignment 3/A3/quiz.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data.get("quiz", {})
    except FileNotFoundError:
        print(f"Error: File {filename} was not found.")
        return {}

    
def ask_questions(questions):
    while True:
        name = input("Enter your name: ").strip().replace(" ", "_")
        if name:
            break
        print("Invalid name. Please try again.")
    results = []
    score = 0
    total_questions = len(questions)
    
    for i, (key, value) in enumerate(questions.items(), start=1):
        print(f"\n Question {i}: {value['question']}")
        for option, answer in value["options"].items():
            print(f" {option}) {answer}")    
    
    
        while True:
            user_answer = input("Enter your answer(or 'quit' for exit): ").strip().lower()
            if user_answer in value["options"].keys() or user_answer == "quit":
                break
            print("Invalid answer. Please try again.")
        
        if user_answer == "quit":
            break
    
        is_correct = user_answer == value["correct_answer"].lower()    
        if is_correct:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {value['correct_answer']}) {value['options'][value['correct_answer']]}\n")
            
        results.append([i, value["question"], user_answer, value["correct_answer"], "Correct" if is_correct else "Incorrect"])
        
    save_results(name, results)
    show_summary(score, total_questions)
    
    
def save_results(username,results):
    
    if not results:
        print("No results to save.")
        return     
    
    filename = f"{username}_quiz_results.csv"
    try:
        with open(filename, mode="w", newline="",encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Question Number.", "Question Text", "Your Answer", "Correct Answer", "Result"])
            writer.writerows(results)
        print(f"Results saved to {filename}.")
    except IOError as e:
        print(f"File Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
def show_summary(score, total_questions):
    
    if total_questions == 0:
        print("The quiz was not taken.")
        return
    
    score_percent = (score / total_questions) * 100
    print(f"\nYou got {score} out of {total_questions} questions correct. Total score: {score:.2f}%")
    
    if score_percent >= 90:
        print("excellent!")
    elif score_percent >= 70:
        print("Good job!")
    elif score_percent >= 50:
        print("You passed!")
    else:
        print("Better luck next time!")
        
if __name__ == "__main__":
    questions = load_questions()
    ask_questions(questions)
