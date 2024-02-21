class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Sets
        setNums = set(nums)
        if len(nums) > len(setNums):
            return True
        else:
            return False
        
        # List Loopup (Time Limit Exceeded)
        # newArr = []
        # for num in nums:
        #     if num in newArr:
        #         return True
        #     else:
        #         newArr.append(num)
        # return False

        # Bruteforce (Time Limit Exceeded)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True

        # return False