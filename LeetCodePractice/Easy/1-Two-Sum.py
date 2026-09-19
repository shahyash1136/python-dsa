class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in num_dict:
                return [num_dict[compliment],i]
            num_dict[nums[i]] = i
