alphabet = []
for letter in range(97,122):
    alphabet.append(chr(letter))

vowels = ['a','e','i','o','u']
words  = ['apple','banana','when','fgds']

thisWord = words[1] # "banana"

def containsVowel(thisWord,vowels):
    for vowel in vowels: 
        if vowel in thisWord:
            return True

if containsVowel(thisWord,vowels):
    print thisWord, 'has a vowel.'
else:
    print thisWord, 'does not have a vowel.'