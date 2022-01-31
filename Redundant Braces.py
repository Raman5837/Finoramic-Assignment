''' 
Problem Link:- https://www.interviewbit.com/problems/redundant-braces/
'''


class Solution:
	# @param A : string
	# @return an integer
 
    def braces(self, A):

        stack = []
        OperatorFound = False

        for char in A:
            if char == '(':
                stack.append(char)
                OperatorFound = False

            elif char == ')':
                Previous = stack.pop()
                if Previous == '(':
                    return 1
                stack.pop()
                OperatorFound = False

            elif char in ['+', '-', '*', '/'] and not OperatorFound:
                stack.append('#')
                OperatorFound = True
        return 0
