# Alex Chen
# ET 574, Functions
# Hw #1
# Prof. Sun

def isVowelWord(word):
    if 'a' and 'e' and 'i' and 'o' and 'u' in word.lower():
        print(f"{word} contains every vowel")
    else:
        print(f"{word} does not contain every vowel")


word = input("Enter a word: ")
isVowelWord(word)
