def run_quiz():
    questions = [
        {
            "question": "What does the 'print' function do in Python?",
            "options": ["A. Takes input", "B. Prints output to the screen", "C. Stops the program", "D. Creates a loop"],
            "answer": "B"
        },
        {
            "question": "Which movie features a character named 'Forrest Gump'?",
            "options": ["A. Titanic", "B. The Matrix", "C. Forrest Gump", "D. Inception"],
            "answer": "C"
        },
        {
            "question": "What symbol is used to start a comment in Python?",
            "options": ["A. //", "B. <!-- -->", "C. #", "D. /* */"],
            "answer": "C"
        },
        {
            "question": "Which of these animals cannot jump?",
            "options": ["A. Dog", "B. Kangaroo", "C. Elephant", "D. Rabbit"],
            "answer": "C"
        },
        {
            "question": "What does CPU stand for?",
            "options": ["A. Central Processing Unit", "B. Computer Power Unit", "C. Control Panel Unit", "D. Central Program Unit"],
            "answer": "A"
        }
    ]

    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect! The correct answer was {q['answer']}.")

    print(f"\n🏁 Quiz complete! You got {score} out of {len(questions)} correct.")

def main():
    while True:
        run_quiz()
        again = input("\nWould you like to play again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing! 👋")
            break
        # Run the quiz game
        main()