#list of words 
words = ['yellow', 'world', 'Joy', 'banana', 'apple', 'green', 'graduation', 'strawberry']

#list comprehension to find words with the odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]
print('words with odd number of characters:', odd_length_words)
