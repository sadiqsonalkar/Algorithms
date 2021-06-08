def selectionsort(A):
    N = len(A)
    for i in range(0, N):
        small = A[i]
        pos = i
        for j in range(i + 1, N):
            if A[j] < small:
                small = A[j]
                pos = j
        temp = A[pos]
        A[pos] = A[i]
        A[i] = temp
        print ("After pass :")
        print (A)
        
A = [10, 7, 3, 1, 9, 7, 4, 3]
print ("Initial Array :")
print (A)
selectionsort(A)
print("\nMinimum element is ", A[0])
print("Maximum element is ", A[len(A)-1])
