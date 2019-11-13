def getAvailableLetters (lettersGuessed):
    Alphabet = "abcdefghijklmnopqrstuvwxyz"
    a = ""
    for elements in Alphabet:
        if elements not in lettersGuessed:
            a += elements
    return a
    
def getGuessedWord(secretWord, lettersGuessed):
    string = ""
    for elements in secretWord:
        if elements in lettersGuessed:
            string += elements
        elif elements not in lettersGuessed:
            string += '_'
    return string

def isWordGuessed(secretWord, lettersGuessed):
    for elements in secretWord:
        if elements in lettersGuessed:
            return True
        else:
            return False

def Hangaroo(secretWord):
   print ('Welcome to Hangaroo!!')
   print ('The word you need to guess is ' + str(len(secretWord)) + ' letters long.')
    
   guesses = ''
   guessesremaining = 10
   
   print ('------------')
  
   while True:
        print ('The guesses you have left are: ' + str(guessesremaining))
        print ('The available letters are: ' + getAvailableLetters(guesses))
        guess = input('Guess a letter: ')
        
        if guess in secretWord and guess not in guesses:
            guesses += guess
            print ('NICE!: ' + getGuessedWord(secretWord, guesses))
        elif guess in guesses:
            print ('Sorry, but you have already guessed that: ' + getGuessedWord(secretWord, guesses))
        else:
            guesses += guess
            print ('Sorry, but that letter is not here: ' + getGuessedWord(secretWord, guesses))
            guessesremaining -= 1
        
        print ('------------')
        
        if guessesremaining <= 0:
            print ('Sorry, but you lost the GAME, loser >:D ')
            break
        if isWordGuessed(secretWord, guesses):
            print ('CONGRAJALASHUNS YOU HAVE GUESSED THE WORD CORRECTLY :D')
            break