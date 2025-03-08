'''string  = "The quick brown fox jumps over the lazy dog"
default_dict = {}
for i in string:
    if i.isalpha():
        lower_case = i.lower()
        default_dict[lower_case] = 0
if len(default_dict) == 26:
    print("Pangram")
else:
    print("Not Pangram")

'''
import string
 
def is_pangram(s):
    # Convert to lowercase and remove spaces
    s = s.lower()
    # Get all letters of the alphabet
    alphabet = set(string.ascii_lowercase)
    print(alphabet)
    # Check if all letters are present in the given string
    return alphabet.issubset(set(s))
 
# Example Usage
sentence1 = "The quick brown fox jumps over the lazy dog"
sentence2 = "Hello World"
 
print(is_pangram(sentence1))  # Output: True
print(is_pangram(sentence2))  # Output: False'''