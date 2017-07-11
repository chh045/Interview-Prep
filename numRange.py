def printArray(A, B, C):
    print "[",
    for i in range(B, C+1):
        print A[i], " ",
    print "]"
def numRange(A, B, C):
        if B > C:
            return -1
        if not A:
            return -1
        lo = 0
        hi = 0
        res = A[0]
        count = 0
        while 1:
            if lo > hi:
                hi += 1
                res += A[hi]
                continue
            if hi == len(A)-1:
                if res in range(B, C+1):
                    printArray(A, lo, hi)
                    count += 1
                res -= A[lo]
                if lo == len(A)-1:
                    break
                lo += 1
                continue
            if res > C:
                res -= A[lo]
                lo += 1
            elif res < B: 
                hi += 1
                res += A[hi]
            else:
                count += 1
                printArray(A, lo, hi)
                if res + A[hi+1] > C:
                    res -= A[lo]
                    lo += 1
                else:
                    hi += 1
                    res += A[hi]
        return count
print 5/2
arr = [ 80, 97, 78, 45, 23, 38, 38, 93, 83, 16, 91, 69, 18, 82, 60, 50, 61, 70, 15, 6, 52, 90 ]
#print numRange(arr, 99, 269)