mystr = input("Enter an str containing at least 6 charachters:")# taking input from the user
if len(mystr) < 6:#validating the input of user
    print(mystr,"is not a valid str")
#printing not valid statement
    print("number of characters in input are",len(mystr))#printing the number of characters in input str
elif mystr.isalpha():
#validating if the input is alphabetic
    print('You have entered a valid alphabetic string')
#printing the statement of valid alphabetic string
    print("number of characters in input are",len(mystr))#printing the number of characters in input str

else:
    print(mystr," is not a valid str")
#printing not valid statement
    index = mystr.find('e')#finding the character e using find
    print("your input contains e at",index, "index position")#printing the index position of e 
    print("number of characters in input are",len(mystr))#printing the number of characters in input str
    
