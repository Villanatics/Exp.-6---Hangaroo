def getAvailableLetters (lettersGuessed):
    Alphabet = "abcdefghijklmnopqrstuvwxyz"
    a = ""
    for elements in Alphabet:
        if elements not in lettersGuessed:
            a += elements
    return a