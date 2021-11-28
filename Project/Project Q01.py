def menu():
    '''prints menu'''
    
    print("Hello, this program allows you to translate text to morse code or translate morse code to text.")
    print()
    print("Please, select one of the below options:")
    print()
    print("*** Enter 't' for encoding text")
    print("*** Enter 'm' for decoding morse code")
    print("*** Enter 'e' to exit the program.")
    print()

def morse_code_dict():
    ''' takes morse.txt and stores them into 2 dictionaries
        one for encoding and one for decoding '''
    
    encoding = {}
    decoding = {}
    morse_file = open("morse.txt",'r')
    for line in morse_file:
        line = line.split()
        encoding[line[0]] = line[1]
        decoding[line[1]] = line[0]
    morse_file.close()
    return list([encoding, decoding])
    
        
    
def text_to_morse(text):
    ''' translates each letter into morse code and prints translated phrase '''
    morse_text = ('')
    encoding = morse_code_dict()[0]

    #for letter, checks if letter is a space or a letter
    for letter in text:

        # space translates into 3 spaces
        if letter == ' ':
            morse_text += '  '
            
        # a letter translates into morse code
        else:
            letter = letter.upper()
            
            # checks if it is a letter or number
            if letter not in encoding:
                print("***invalid character***")
                print()
                return print()
            
            morse_text = morse_text + encoding[letter] + ' '
            
    print(morse_text)
    print()
    print()

        
def morse_to_english(morse):
    ''' translates each morse code letter into an english letter and prints
        translated morse code phrase '''
    
    morse += ' '
    english_text = ('')
    decoding = morse_code_dict()[1]
    space_counter = 0
    letter = ''

    #for loop for each character in morse
    for character in morse:
            
        #check if there is a . or -
        if character == '.' or character == '-':
            
            #if so, add to a temp string
            letter = letter + character

            #resets space counter
            space_counter = 0
            
        #if there is a space
        elif character == ' ':
                
            #translate temp string and add to english_text
            if letter != '':

                # checks if it is a valid morse code
                if letter not in decoding:
                    print("***invalid morse code character***")
                    print()
                    return print()
                
                english_text = english_text + decoding[letter]
                letter = ''
            
            # add 1 to space_counter
            space_counter += 1

        # checks if it is a valid morse code
        else:
            print("***invalid morse code character***")
            print()
            return print()

            
        #if there are 3 spaces in the morse code
        while space_counter == 3:
            
            #add space to english_text
            english_text = english_text + ' '
            space_counter = 0
            
    print(english_text)
    print()
    print()

    
def main():
    '''main function'''
    
    menu()
    user_input = input("My input is: ")

    # checks if user input is a valid option
    valid_input = "tme"
    while user_input not in valid_input:
        print("***invalid option***")
        user_input = input("Please enter a valid option: ")

    # if user wants to encode or decode
    while user_input == 't' or user_input == 'm':
        print()
        if user_input == 't':
            print("Please enter text to translate:")
            text_to_translate = input()
            text_to_morse(text_to_translate)
        elif user_input == 'm':
            print("Please enter morse to translate:")
            morse_to_translate = input()
            morse_to_english(morse_to_translate)
        menu()
        user_input = input("My input is: ")
        while user_input not in valid_input:
           print("***invalid option***")
           user_input = input("Please enter a valid option: ")

    #if user wants to encode or decode
    if user_input == 'e':
        print()
        print("Thanks for using this program!")
        

main()
