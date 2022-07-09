L1 = [5, -34, 0, 98,-11, 244, 193, 98, -10, -20, 45, 67]#the list l1 is initiated
print(L1)#list l1 is printed
n = int(input('Enter an integer:'))#an integer input is taken from the user
count = 0# count is initiated to 0 for counting number of occurance
for i in range(len(L1)):
    if L1[i] == n:#checking if list element is equal to user input
        count = count + 1#increasing the cound
        
if count >= 1:#checking the element has occured at least once
    x = L1.index(n)# assigning the first index of input to x
    print('the first occurance of',n,'is at index',x)#printing the index
    print('all elements after first occurance are:',L1[x+1:])#printing all the elemnts after the occurance
    L1.remove(n)#removing the element of first occurance from list
    print(L1)#printing the updated list l1
    
else:
    print(n,'does not occur in list L1')#printing the number which is not in the list

            
