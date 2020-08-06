"""checking whether given number is prime or not"""

num = int(input("Enter a number: "))#input taking from the user
if num > 1:# if input number is less than or equal to 1, it is not prime
   for i in range(2,num):
       if (num % i) == 0:#dividing the given num with 2
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")
       
else:
   print(num,"is not a prime number")