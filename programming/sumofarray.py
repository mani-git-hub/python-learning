"""finding the sum of the given array"""

def _sum(arr): 
    return(sum(arr))## return sum using inbuilt sum() function
    
    
lst = []# creating an empty list 
n = int(input("Enter number of elements : "))# number of elemetns as input 
for i in range(0, n): # iterating till the range
    ele = int(input()) 
    lst.append(ele)  # adding the element      

 
ans = _sum(lst)
 
print ('Sum of the array is ', ans)