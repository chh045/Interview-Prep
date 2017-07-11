def prettyPrint(A):
        length = 2*A-1
        arr = [[A for i in range(length)] for _ in range(length)]
        start = 1
        for val in range(A-1, 0, -1):
            print "val, start, length: ", val, start, length
            for i in range(start, length-1):
                for j in range(start, length-1):
                    print i, j
                    arr[i][j] = val
            start += 1
            length -= 1
        return arr

print prettyPrint(3)