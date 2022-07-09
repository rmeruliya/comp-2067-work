n = input('Enter a positive integer:')#taking an an integer from the user
if n.isdigit():#checking if the integer is valid
    n = int(n)
    if 0 <= n and n < 30:#checking if the user in put is between 0 an 30
        n = 2 ** n #calculating 2^n if between 0 and 30
        print('value of 2^n is', n)#printing the value of n
    elif 30 <= n and n < 50:#checking if the user in put is between 0 an 30
        n = 2 ** (0.3 * n)# calculating 2^0.3*n if between 30 and 50
        print('value of 2^(0.3*n)) is ', n)#printing the value of n
    elif 50 <= n and n < 80:#checking if the user in put is between 0 an 30
        n = 1.5 ** (0.3 * n)#calculating 1.5^0.3*n if between 50 and 80
        print('value of 1.5^(0.3*n)) is ', n)#printing the value of n
    elif n >= 80:#checking if user input is greater than 80
        n = 1.2 ** (0.2 * n)# calculating 1.2^0.2*n
        print('value of 1.2 ^(0.2 * n)) is ', n)#printing the value of n
else:
    print('You did not enter valid input')#printing not valid statement
