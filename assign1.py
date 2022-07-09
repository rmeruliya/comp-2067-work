x = 12.56 #value of x is defined as 12.56
y = 7 #value of y is defined as 7
z = 14.3015 #value of defined as 14.3015

result = ((3**y)-(x+y))/((x-y)*z) #here is the result where the whole equation is solved

print("result is ",result) #value of result is printed

mon = 500 #value of monday is assigned 500
tue = 750.25  #value of tuesday is assigned 750.25
wed = 625 #value of wednesday is assigned as 625
thur = 580.64 #value of thursday is assigned 580.64
fri = 700.8 #value of friday is assigned 700.8
sat = 415.48 #value of saturday is assigned 415.48
sun = 320 #value of sunday is assigned 320

total = mon + tue + wed + thur + fri + sat + sun #here the total of whole week is done for distance travelling
print("Total distance travelled is",round(total),"Km") #value of total distance is printed

avgend = (sat + sun)/2 #average of weekend is calculated
print("Average of staurday and sunday driving is",round(avgend,2),"Km") #avgend is printed to value of 2 decimal

avgday = (mon + tue + wed + thur + fri)/5 #average of weekday is calculated as avgday
print("Avg of weekday is",avgday,"Km") #value of avgday is printed


time = 40 #value of time is assigned to time as 40
speed = total/time #total speed of vehicle is calculated and assigned to speed
print("Average speed was",round(speed,1),"Km/hr") #value of speed is printed


amt = 129.95 #value of amount is assigned as 129.95
rem = ((amt)*(13/100)) #13% value of amount is calculated
hst = round(rem,2) #value to be added is rounded upto 2 decimal and assigned to rem
print("The hst that will cut is",hst) #value of hst is printed

total = amt + hst #value of hst is added to the amount
print("total with hst is ",round(total,2)) #value of amount is printed and rounded to 2 decimaml points
