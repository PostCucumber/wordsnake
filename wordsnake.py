def main():
    alphabet = []
    alphabet = buildAlphabet(alphabet)
    characterCount = 0
    vowels = ['a','e','i','o','u']
    vowelCount = 0
    consonantCount = 0

    print "Does this word have a vowel?"
    thisWord = raw_input("enter a word: ")
    thisWord = makeCharArray(thisWord)
    print(thisWord)
    characterCount = len(thisWord)
    print "Amount of characters: ",characterCount
    vowelCount = countVowels(thisWord,characterCount,vowels,vowelCount)
    print "Amount of vowels: ",vowelCount

def buildAlphabet(alphabet):
    for letter in range(97,122):
        alphabet.append (chr(letter))

def countVowels(thisWord,characterCount,vowels,vowelCount):
    for character in thisWord:
        for i in range(0,4):
            if character == vowels[i]:
                ++vowelCount
    return vowelCount
    
    '''
    for i in range(0,characterCount):
        if thisWord[i] == vowels[i]:
            ++vowelCount
        elif thisWord[1] == 'y':
            ++vowelCount
        else:
            ++consonantCount
    return vowelCount
    '''

def makeCharArray(thisWord):
    return [char for char in thisWord]

main()