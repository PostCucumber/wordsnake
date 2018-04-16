def main():
    alphabet = []
    alphabet = buildAlphabet(alphabet)
    vowels = ['a','e','i','o','u']

    print "Does this word have a vowel?"
    thisWord = raw_input("enter a word: ")
    
    if containsVowel(thisWord,vowels):
        print thisWord, 'has a vowel.'
    elif containsY(thisWord):
        print thisWord, "has a vowel, but it's a 'y'"
    else: 
        print thisWord, 'does not have a vowel.'

def buildAlphabet(alphabet):
    for letter in range(97,122):
        alphabet.append(chr(letter))

def containsVowel(thisWord,vowels):
    for vowel in vowels: 
        if vowel in thisWord:
            return True

def containsY(thisWord):
    if 'y' in thisWord:
            return True

main()