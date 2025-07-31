def greet_user():
  """Asks the user for their name and favorite color, then prints a personalized greeting."""

  # Get the user's name
  name = input("What is your name? ")

  # Get the user's favorite color
  color = input("What is your favorite color? ")

  # Print the personalized greeting
  print(f"Hello, {name}! Your favorite color, {color}, is awesome!")

# Call the function to execute the program
greet_user()