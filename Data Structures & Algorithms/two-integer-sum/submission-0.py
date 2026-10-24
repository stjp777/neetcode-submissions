class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if nums[i] in result:
                return [result[nums[i]], i]
            result[difference] = i