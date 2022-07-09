str1 = input("Enter a string with only alphanumeric characters:")# taking input from the user
if str1.isalnum():#validating if the input is alphnumric
    print(str1,'a valid alphabetic string')#printing the statement of valid alphnumeric string
    print("number of characters in input are",len(str1))#printing the number of characters in input 
    index = str1.find('e')#finding the character e using find
    if index == -1:#validating if e is present in str1
        print(str1,'does not contain letter "e"')#printing the statement of not present
    else:
        rep = str1.replace('e','*')#replacing the value where * occured in character
        print('replaced "e" with "*" is ',rep)#printing the replaced rep
        
else:
    print(str1,"is not a valid input")#printing not valid statement
    
