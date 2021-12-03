print("This program will analyze your sentence to show the number of words, vowels, and consonants.")
theInput = input("Please input your sentence here: ")
#Putting the program inside the function to train myself not to get confused with parameters and arguments.
#It was supposed to be only words, vowels, and consonants but the program is going to be incomplete if symbols and numbers were inputted so I added them.
def sentenceAnalyzer(yourSentence):
    vowels = 0
    words = 0
    consonants = 0
    numbers = 0
    symbols = 0
    for i in yourSentence:
        if ( (i >= "a" and i <= "z") or (i >= "A" and i <= "Z") ):
            #Lowering each letter in the string so the letters can become neutral in counting
            i = i.lower()
            if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
                vowels = vowels + 1
            else:
                consonants = consonants + 1
        elif i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9":
            numbers = numbers + 1
        #Putting this elif statement so spaces cannot be counted as symbols.
        elif i == " ":
            pass
        else:
            symbols = symbols + 1
        #Splitting the string with space separator as a default so the words can be counted.
        words = str(len(yourSentence.split()))

    print(f"Vowels: {vowels}\nConsonants: {consonants}\nNumbers = {numbers}\nSymbols = {symbols}\nWords: {words}")

sentenceAnalyzer(theInput)