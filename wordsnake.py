def main():
    alphabet = []
    alphabet = buildAlphabet(alphabet)
    vowels = ['a','e','i','o','u']
    vowelCount = 0

    print "Does this word have a vowel?"
    thisWord = raw_input("enter a word: ")
    
    if thisWordHasVowel(thisWord,vowels):
        vowelCount = countVowels(thisWord,vowels,vowelCount)
        print thisWord, 'has', vowelCount, 'vowel(s)'
    elif thisWordContainsY(thisWord):
        vowelCount - countVowels(thisWord,'y',vowelCount)
        print thisWord, "has", vowelCount, ", but they are all 'y'"
    else:
        print thisWord, 'does not have any vowels.'

def buildAlphabet(alphabet):
    for letter in range(97,122):
        alphabet.append(chr(letter))

def thisWordHasVowel(thisWord,vowels):
    for vowel in vowels: 
        if vowel in thisWord:
            return True

def countVowels(thisWord,vowels,vowelCount):
    for vowel in vowels:
        if vowel in thisWord:
            vowelCount += 1
    return vowelCount

def thisWordContainsY(thisWord):
    if 'y' in thisWord:
            return True

main()