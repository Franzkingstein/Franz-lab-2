from collections import Counter

def second(s):
    words = s.split()  # Fix the variable name here
    count = Counter(words)  # Use the correct function name
    return count

s = input("Enter a String: ")
print(second(s))
