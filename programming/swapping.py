"""swapping the array of elements at the given postions"""

def swap(list, pos1, pos2):# Swap function defition  
      
    list[pos1], list[pos2] = list[pos2], list[pos1]#swapping of two elements 
    return list
  

#initializing the ele from the user
lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n): 
    ele = int(input()) 
    lst.append(ele)
#initializing the positions from the user   
pos1 = int(input("enter the pos 1 :")) 
pos2 = int(input("enter the pos 2 :"))

k = swap(lst, pos1-1, pos2-1)#calling function  
print(k)#printing after swapping