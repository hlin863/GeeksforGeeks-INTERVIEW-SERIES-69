import collections

class Solution:
    def optimalArray(self, n : int, a : list[int]) -> list[int]:
        # code here        
        
        # find the most common element
        mode = self.most_common(a)

        if a.count(mode) == 1:
            # sort the list and find the median
            a.sort()

            median = a[n // 2]

            return [abs(x - median) for x in a]

        return [abs(x - mode) for x in a]
    
    def most_common(self, lst):
        return max(set(lst), key = lst.count)

print(Solution().optimalArray(5, [1, 2, 3, 4, 5]))