def main():
    alphabet = []
    alphabet = buildAlphabet(alphabet)
    characterCount = 0
    vowels = ['a','e','i','o','u']
    vowelCount = 0
    consonantCount = 0

    print "Does this word have a vowel?"
    thisWord = raw_input("enter a word: ")
    
    characterCount = len(thisWord)
    print(characterCount)
    vowelCount,consonantCount = countVowels(thisWord,characterCount,vowels,vowelCount,consonantCount)

def buildAlphabet(alphabet):
    for letter in range(97,122):
        alphabet.append (chr(letter))

def countVowels(thisWord,characterCount,vowels,vowelCount,consonantCount):
    for i in range(0,characterCount):
        if thisWord[i] == vowels[i]:
            ++vowelCount
        elif thisWord[1] == 'y':
            ++vowelCount
        else:
            ++consonantCount
    return vowelCount,consonantCount          

def makeCharArray(thisWord):
    return [char for char in thisWord]

main()