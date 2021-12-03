print("Please go through to the password checker.")
thePassword = input("Input your password here please: ")
Valid = False
#The Valid boolean data will determine which my errors are in my inputted password.
#What I basically did in my coding is in each category(symbols, numbers, capitals, and len), I started counting them from 0 and if the value was 1 or greater, the condition was met.
#len was greater than 15 though and special characters were evaluated by the any() function.
def passwordChecker(yourPassword):
   
    if len(yourPassword)> 15:
        Valid = True
    else:
        print("Password too short.")
        Valid = False

    capitals = 0

    if Valid:
        for i in yourPassword: 
             if i.isupper():
                 capitals = capitals + 1

    if capitals >= 1:
        Valid = True
    else: 
        print("Password needs to have at least one capital letter.")
        Valid = False

    number = 0
    numberList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    if Valid:
        for i in yourPassword:
            for numbers in numberList:
                if i == numbers:
                    number = number + 1

    if number >= 1:
        Valid = True
    else:
        print("Password needs at least one number.")
        Valid = False


    SpecialChars = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "|", "\\", "/", ":", ";", "\"", "'", ">", "<", ",", ".", "?"]

    if Valid:
        #If any() function was used to determine if the string contained any mentioned special chars.
        if any(char in SpecialChars for char in yourPassword):
            print("Valid Password!")
        else:
            print("Password needs at least one special character from the keyboard.")
    else:
        print("Password needs at least one special character from the keyboard.")
    
        
passwordChecker(thePassword)
