def isWordGuessed(secretWord, lettersGuessed):
    for elements in secretWord:
        if elements in lettersGuessed:
            return True
        else:
            return False