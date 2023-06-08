# Contains Duplicate

## This problem is a good example of a tradeoff between complexity of time and of space. 

### For instance, this block represents an algorithm focusing on optimizing the space a memory needed to perform the task, as we do not create any variable.
```
#  Time: O(nlogn)
#  Space: O(1)
class Solution_3(object):
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False

```
### On the other hand, this block focuses on the time complexity, but therefore needs more space.
```
#  Time: O(1)
#  Space: O(n)
class Solution_2(object):
    def containsDuplicate(self, nums):
        return (len(set(nums)) != len(nums))

```