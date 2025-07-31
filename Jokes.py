import random

def tell_a_joke():
    jokes = [
         "Why do Python developers wear glasses? Because they can't C!",
        "Why did the programmer quit his job? Because he didn't get arrays.",
        "How do you comfort a JavaScript bug? You console it.",
        "Why do programmers prefer dark mode? Because the light attracts bugs!",
        "I told my computer I needed a break... and it said: 'Why not try a while loop?'",
        "Why was the Python function so chill? Because it had no class!",
        "Why was the developer unhappy at their job? They wanted arrays!",
        "There are 10 kinds of people in the world: Those who understand binary and those who don't.",
        "Why did the Python file go to therapy? It had too many unresolved issues.",
        "What's a programmer's favorite hangout place? The Foo Bar."
    ]
    joke = random.choice(jokes)
    print("\n🃏 Here's your programming joke of the day:")
    print(f"\n😂 {joke}\n")

# Run the program
if __name__ == "__main__":
    tell_a_joke()
    
   