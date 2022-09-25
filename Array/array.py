import collections

class Solution:
    def optimalArray(self, n : int, a : list[int]) -> list[int]:
        # code here

        # list of differences
        differences = []

        # loop through the list to find the absolute difference between list[i] and i

        for i in range(len(a)):
            diff = abs(a[i] - i)
            differences.append(diff)

        return differences

    """
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
    """

print(Solution().optimalArray(4, [1, 6, 9, 12]))