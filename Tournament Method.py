print("Enter size of an array: ")
s = int(input())
i = 0
b = []
print("Enter array element: ")

def bubbleSort(b):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

while i<s:
    c = int(input("Enter the elements: "))
    b.append(c)
    i = i+1

print("The given elements are: ",b)
def getSecondHighest(b):
    hi = mid = lo = 0
    for i in range(0,len(b)):
        x = b[i]
        if(x>hi):
            lo = mid
            mid = hi
            hi = x
        elif(x<hi and x>mid):
            lo = mid
            mid = x
        elif(x<lo):
            lo = x
    return mid
print("The sorted array using bubble sort is = ",b)
print("Second highest Element is given array = ", getSecondHighest(b))

