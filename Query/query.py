from ast import main
from typing import List
import collections


class Solution:
    def solveQueries(self, N : int, num : int, A : List[int], Q : List[List[int]]) -> List[int]:
        # code here
        
        result = []
        
        for q in Q:

            temp_result = []
            
            for index in range(q[0], q[1] + 1):

                element = A[index]

                A_temp = A[index:]

                # count the number in A_temp that are the same as element

                count = A_temp.count(element)

                temp_result.append(count)

            # count the number of elements in temp_result that equal q[2]
            count = temp_result.count(q[2])

            result.append(count)
            

        return result


#{ 
#  Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()
 
print(Solution().solveQueries(5, 3, [1, 1, 3, 4, 3], [[0, 2, 2], [0, 2, 1], [0, 4, 2]]))

print()

print(Solution().solveQueries(5, 2, [1, 1, 1, 1, 1], [[0, 4, 4], [0, 4, 5]]))