"""checking whether given number is palindrome or not"""

num = int(input("Enter a number: "))#input taking from the user
rev = 0  # initialize rev
temp = num
while num > 0:#reversing the num to check it is palindrome or not
   digit = num % 10
   rev = rev * 10 + digit
   num //= 10
if temp == rev:
   print(temp,"is an palindrome number")
else:
   print(temp,"is not an palindrome number")