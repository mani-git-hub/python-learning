""" implementation of Insertion Sort """
   
def insertionSort(arr):# Function to do insertion sort  
    for i in range(1, len(arr)):# Traverse through 1 to len(arr) 
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
    
lst = []# creating an empty list 
n = int(input("Enter number of elements : "))# number of elemetns as input 
for i in range(0, n): # iterating till the range
    ele = int(input()) 
    lst.append(ele)  # adding the element  
    
insertionSort(lst) #function calling

print ("Sorted array is:") 
for i in range(len(lst)): 
    print ("%d" %lst[i])