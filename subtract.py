class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

def subtract(A):
        arr = []
        while A.next != None:
            arr.append(A.val)
        for i in range(0, len(arr)/2+1):
            arr[i] = arr[::-1][i]-arr[i]
        _list = arr
        head = ListNode(arr[0])
        for i in range(1, len(arr)):
            head.next = ListNode(arr[i])
        return head

def subsub(A):
	arr = A
	for i in range(0, len(A)/2):
		arr[i] = A[::-1][i]-A[i]
	return arr

arr = [ 95 , 59 , 26 , 16 , 31 , 39 , 29 , 8 , 74 , 14 , 41 , 41 , 64 , 88 , 34 , 21 , 67 , 23 , 17 , 41 , 3 , 38 , 4 , 45 , 93 , 92 , 99 , 24 ]
print subsub(arr)