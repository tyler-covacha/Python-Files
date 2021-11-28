def vowel(string):
    vowel1 = "aeiou"
    vowelCounter = 0
    for i in string:
        for x in vowel1:
            if x == i:
                vowelCounter += 1
    print("The string you entered includes",vowelCounter,"vowels and", end=" ")
    return vowelCounter

def consonant(string):
    vowel1 = "aeiou"
    consonantCounter = 0
    counter = 0
    for i in string:
        for x in vowel1:
            if x == i:
                consonantCounter += 1
    consonantCounter = len(string) - consonantCounter
    print(consonantCounter,"consonants")
    return consonantCounter

x = input("Enter a string: ")
vowel(x)
consonant(x)

