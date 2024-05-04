def number_of_unique_characters(s):
    unique_chars = set(s)
    return {char: s.count(char) for char in unique_chars}

print(number_of_unique_characters('aaabbcda')) 