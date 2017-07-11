from collections import Counter
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def __init__(self):
    	self.res = []

    def permute(self, A):
        #1. create a dict to store the frequency of all elements
        c = Counter(A)
        self.permute_rec(dict(c), 0, len(A), [None]*len(A))
        res = []
        for ss in self.res:
        	res.append([int(s) for s in ss.split(',')])
        return res
        
    #2. create a function that takes the counter set as a carrier of recursion
    def permute_rec(self, C, level, length, permute):
		# this function key recurse through the items of the dictionary C
		# 3. use a for loop to loop through each item until the count is zero
		if level == length:
			
			self.res.append(','.join(str(e) for e in permute))
			return

		for val, count in C.items():
			# if the usage is a element is off, skip to the next one
			if count == 0:
				continue
			# there are at least one element in the dict, update dict
			permute[level] = val
			C[val] -= 1
			#print "C:", C, "level: ", level
			#print "permute before recursive call: ", permute
			self.permute_rec(C, level+1, length, permute)
			C[val] += 1


sol = Solution()
arr = [10, 10, 12]
print sol.permute(arr)