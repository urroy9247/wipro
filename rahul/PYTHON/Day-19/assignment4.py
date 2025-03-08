from collections import defaultdict
 
def group_anagrams(words):
    anagrams = defaultdict(list)
 
    for word in words:
        # Sort the word and use it as a key
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
 
    # Convert the dictionary values to a list
    return list(anagrams.values())
 
# Example usage:
words_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words_list))