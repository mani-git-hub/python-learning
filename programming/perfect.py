"""checking whether given number is perfect number or not"""

n = int(input("Enter any number: "))#taking input from the user
sum1 = 0#initializing the variable
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")           