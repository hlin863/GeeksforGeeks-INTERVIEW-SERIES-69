from ast import main
from typing import List
import collections


class Solution:
    def solveQueries(self, N : int, num : int, A : List[int], Q : List[List[int]]) -> List[int]:
        # code here

        """
        MAP = map()
        foreach(int x in A){
            if map contains a
                map[a] += 1
        }

        map = collections.defaultdict(int)

        for a in A:
            # check if map contains a
            if a in map:
                map[a] += 1
            else:
                map[a] = 1

        # display the array
        print("A : {}".format(A))

        # display the map
        print("Map: {}".format(map))

        print()


        """

        result = map(lambda x : self.get_count(A, x), Q)

        result = list(result)    

        return result
        
        """
        Version 1: loop versin

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

        """
    
    def get_count(self, A, x):

        temp_result = []

        # generate a list of values from x[0] to x[1]
        temp_list = list(range(x[0], x[1] + 1))

        # replace the for loop with another map
        temp_result = list(map(lambda a : self.get_count_val(A, a), list(range(x[0], x[1] + 1))))

        """
            
        for index in range(x[0], x[1] + 1):

            element = A[index]

            A_temp = A[index:]

            # count the number in A_temp that are the same as element

            count = A_temp.count(element)

            temp_result.append(count)
        
        """

        # count the number of elements in temp_result that equal q[2]
        count = temp_result.count(x[2])

        return count
    
    def get_count_val(self, A, x):

        element = A[x]

        A_temp = A[x:]

        # count the number in A_temp that are the same as element

        count = A_temp.count(element)

        return count
    
    def test_optimisation(self):
        """
        Test function to check if there is a suitable method to optimise 
        the code.
        """

        arr = [1, 2, 3, 4, 5]

        return [self.times_five(x) for x in arr]

    def times_five(self, x):
        return x * 5

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

# query : [a, b, c]

# a = start index
# b = last index
# c = number to track the occurences. 

print()

print(Solution().solveQueries(5, 2, [1, 1, 1, 1, 1], [[0, 4, 4], [0, 4, 5]]))

print()

print(Solution().test_optimisation())