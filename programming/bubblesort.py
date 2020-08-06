"""implementation of Bubble Sort """
  
def bubbleSort(arr):# bubble sorting function definition 
    n = len(arr)  
    for i in range(n-1): # Traverse through all array elements 
        for j in range(0, n-i-1):# traverse the array from 0 to n-i-1    
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] # Swap if the element found is greater
  
lst = []# creating an empty list 
n = int(input("Enter number of elements : "))# number of elemetns as input 
for i in range(0, n): # iterating till the range
    ele = int(input()) 
    lst.append(ele)  # adding the element  
    
bubbleSort(lst)#calling function 
  
print ("Sorted array is:") 
for i in range(len(lst)): 
    print ("%d" %lst[i]),  