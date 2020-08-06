"""finding the factorial of a given number"""

num = int(input("Enter a number: "))#input taking from the user
factorial = 1
if num < 0:# check if the number is negative or positive
   print("factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)