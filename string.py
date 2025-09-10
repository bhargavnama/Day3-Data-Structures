# Finds the length of the string
def length(string: str):
    len = 0
    for _ in string:
        len += 1
    return len

# string = input("Enter a string: ")

# print(f"Length of entered string is {length(string)}")



# Compare two strings
def compare_strings(str1: str, str2: str) -> True:
    if len(str1) != len(str2): 
        return False
    else:
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                return False
        return True

# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")
# if compare_strings(str1, str2):
#     print(f"Both the string are same")
# else:
#     print("Both the strings are not same")


# Concatenate two strings
def concatenate_strings(str1, str2):
    return str1 + str2

# str1 = input("Enter the first string: ")
# str2 = input("Enter the second string: ")
# print(f"Concatenated string is: {concatenate_strings(str1, str2)}")


# count alphabets, digits and special chars in a string
def count_types(string: str):
    alphabets = 0
    digits = 0
    special_chars = 0
    
    for ch in string:
        if ch.isalpha():
            alphabets += 1
        elif ch.isdigit():
            digits += 1
        else:
            special_chars += 1
    
    print(f"There are {alphabets} alphabets, {digits} digits and {special_chars} special" 
          "characters in the string")
    
# string = input("Enter a string: ")
# count_types(string)


# count vowels and consonants in the string
def count_vowels_consonants(string: str):
    vowels_count = 0
    consonants_count = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
    for char in string:
        if char in vowels:
            vowels_count += 1
        else:
            consonants_count += 1
            
    print(f"There are {vowels_count} vowels and {consonants_count} consonants in the string")
    
# string = input("Enter a string: ")
# count_vowels_consonants(string)


# Count number of words in the string
def count_words(string: str):
    words = string.split()
    print(f"There are {len(words)} wors in the given string")
    
# string = input("Enter a string: ")
# count_words(string)

# Count occurances of a character
def count_occurances(string: str) -> int:
    freq = {}
    for ch in string:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    
    res = ""    
    for key, val in freq.items():
        res += f"{key}{val}"
        
    return res

# string = input("Enter a string: ")
# print(count_occurances(string))


# Highest frequency character
def highest_freq_char(string: str) -> str:
    freq = {}
    max_freq_char = string[0]
    
    for char in string:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
        max_freq_char = max_freq_char if freq[char] < freq[max_freq_char] else char
    
    return max_freq_char

# string = input("Enter a string: ")
# print(f"{highest_freq_char(string)} has the highest frequency")
    

# Lowest frequency character
def highest_freq_char(string: str) -> str:
    freq = {}
    max_freq_char = string[0]
    
    for char in string:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
        max_freq_char = max_freq_char if freq[char] > freq[max_freq_char] else char
    
    return max_freq_char

# string = input("Enter a string: ")    
# print(f"{highest_freq_char(string)} has the least frequency")
    