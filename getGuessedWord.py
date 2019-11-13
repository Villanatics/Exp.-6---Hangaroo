def getGuessedWord(secretWord, lettersGuessed):
    string = ""
    for elements in secretWord:
        if elements in lettersGuessed:
            string += elements
        elif elements not in lettersGuessed:
            string += '_'
    return string
