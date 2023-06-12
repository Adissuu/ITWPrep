# Top K Frequent Elements

### Given an array of number nums and a number K, return the K numbers that appear the most frequently in the array.

```
# Time complexity: O(n)
# Space complexity: O(n)
class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0) #adds one to the number present in count or to 0 if it doesn't.
        for n, c in count.items():
            freq[c].append(n)
            
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) >= k:
                    return result
```
### Solution description:
### The first for loop creates a dictionary that counts the number of times a number appears in the array. The second for loop creates a list of lists where the index of the list is the number of times a number appears in the array. The third for loop iterates through the list of lists from the end and appends the numbers to the result list. The if statement checks if the length of the result list is greater than or equal to k and if it is, it returns the result list.
