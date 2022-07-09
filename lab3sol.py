fav_animal = input("Enter you favorite animal name in lowercase:") #user enters the animal name input
print("Your fav animal name in upper case is:",fav_animal.upper())#this statement prints out upper case of the uper input using upper

new_str = fav_animal.replace('o','*')#here o is replaced with * using .replace and assigned to new_Str
print("the leftmost occurance of o that is changed is:",new_str)#leftmost occurance of o is replaced with * and printed

fav_num=int(input("Enter your favorite 2 digit number betwee 10 and 99:")) #getting two digit int input from the user
print("Your 2 digit favorite number is",fav_num)#fav number of user is printed

list1 = ['red', 'blue', 'yellow', 'green', 'red', 'pink',1, [2,3] ]#here list1 is assigned with a list of string and int
print(list1)#value of list1 is pritned


print("the last 3 characters of list with index 2 are:",list1[2][3:])#last 3 character of index 2 are printed

print("elements of list1 starting with the element with index 3 until the end of the list are:",list1[3:])#elements of list1 from index 3 unitl end are printed

color = input("Enter your favorite color:")#input of his fav color is taken and assigned to color
list1.insert(0,color)#value of color is inserted at first index in list using insert
print(list1)#updated list is printed


print("number of element is list1 is:",len(list1))#number of element in list 1 is printed by len
res = fav_num - len(list1)#favnum-len of list1 is done and assigned to red
print(res)#value of res is printed
