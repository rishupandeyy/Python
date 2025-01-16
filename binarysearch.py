from array import *

arr = array('i', [])

n= int(input("enter length of array you want \t"))

for i in range(n) :
    x = int(input("Enter the  value \t"))
    arr.append(x)


print(arr)
val= int(input("enter element you wanna search \t"))

def search( low ,high ):
    if high>=low:
        mid = (low + high)//2
       

        if arr[mid] ==val:
           return mid
        elif arr[mid] > val:
             return search( low , mid-1)
        else:
            return search(mid+1 , high )
    else:
        return-1
    


result = search( 0,len(arr)-1)

if result != -1:
    print("Element found at index : ", result)
else:
    print("Element not found in the array")