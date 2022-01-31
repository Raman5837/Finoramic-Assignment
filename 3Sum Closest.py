''' 
Problem Link:- https://www.interviewbit.com/problems/3-sum/
'''


class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
 
    def threeSumClosest(self, A, B):

        A.sort()
        ClosestSum = 0
        MinDifference = 9999999999 # Treat it as INFINITY

        for index in range(len(A) - 2):
            start = index + 1
            end = len(A) - 1

            while start < end:
                currentSum = A[index] + A[start] + A[end]
                Difference = abs(B - currentSum)

                # If currentSum == Target(B)
                if Difference == 0: return currentSum
                
                if Difference < MinDifference:
                    MinDifference = Difference
                    ClosestSum = currentSum

                if currentSum <= B:
                    start += 1
                else:
                    end -= 1

        return ClosestSum

	
 