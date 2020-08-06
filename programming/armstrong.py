"""checking whether given number is armstrong or not"""

num = int(input("Enter a number: ")) #input taking from the user
sum = 0  # initialize sum
temp = num
while temp > 0:# find the sum of the cube of each digit
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")