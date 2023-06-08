
#  Time: O(nlogn)
#  Space: O(1)
class Solution_3(object):
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False


#  Time: O(1)
#  Space: O(n)
class Solution_2(object):
    def containsDuplicate(self, nums):
        return (len(set(nums)) != len(nums))


# =================================
# Time: O(n^2)
# Space: O(1)
# class Solution_1(object):
#     def containsDuplicate(self, nums):
#         ite = 0
#         for i in range(len(nums)):
#             ite += 1
#             for k in range(ite, len(nums)):
#                 if nums[i] == nums[k]:
#                     return True
#         return False
