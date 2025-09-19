# quiz_game.py
# Simple Command-Line Quiz Game

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Paris", "B) London", "C) Rome", "D) Madrid"],
        "answer": "A"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["A) 10", "B) 11", "C) 12", "D) 13"],
        "answer": "C"
    },
    {
        "question": "Which language is this program written in?",
        "options": ["A) Java", "B) Python", "C) C++", "D) JavaScript"],
        "answer": "B"
    }
]

def play_quiz():
    print("Welcome to the Quiz Game!\n")
    score = 0
    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer (A/B/C/D): ").upper()
        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}\n")
    print(f"Quiz finished! Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    play_quiz()
