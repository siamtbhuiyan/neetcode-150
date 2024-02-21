class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary
        dic = {}
        for index, value in enumerate(nums):
            if target - value in dic:
                return [index, dic[target - value]]
            else:
                dic[value] = index
                
        # Bruteforce
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
