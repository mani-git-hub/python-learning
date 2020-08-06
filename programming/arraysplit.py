"""splitting of array at the given postion and adding at the end of teh array"""

def splitArr(arr, m, k): ##function definition 
    for i in range(0, k):  
        x = arr[0] 
        for j in range(0, m-1): 
            arr[j] = arr[j + 1]  
        arr[m-1] = x 


#initializing the ele from the user
lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n): 
    ele = int(input()) 
    lst.append(ele) 
    
l = len(lst)#finding the length of the array 
position = int(input("enter the postion : "))# setting the postion in array for splitting
  
splitArr(lst, l, position)#function calling 
  
for i in range(0, n):  
    print(lst[i], end = ' ')