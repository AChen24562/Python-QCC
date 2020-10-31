# Alex Chen
# ET 574, Functions
# Extra Credit
# Prof. Sun

def isVowelWord(word):
    isVowelWord = True
    if 'a' and 'e' and 'i' and 'o' and 'u' in word.lower():
        return isVowelWord
    else:
        isVowelWord = False
        return isVowelWord


word = input("Enter a word: ")
if isVowelWord(word):
    print(f"{word} is a vowel word")
else:
    print(f"{word} is NOT a vowel word")
