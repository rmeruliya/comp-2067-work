str1 = input("Enter a string with only alphanumeric characters:")# taking input from the user
if str1.isalnum():#validating if the input is alphabetic
    print(str1,'a valid alphabetic string')#printing the statement of valid alphabetic string
    print("number of characters in input are",len(str1))#printing the number of characters in input str
    index = str1.find('e')#finding the character e using find
    if index == -1:
        print(str1,'does not contain letter "e"')
    else:
        rep = str1.replace('e','*')
        print('replaced "e" with "*" is ',rep)
        
else:
    print(str1,"is not a valid string")#printing not valid statement
    
