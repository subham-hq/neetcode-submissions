class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0

        for num in nums_set:
            if num - 1 in nums_set:
                continue
            current_length = 1
            while num + 1 in nums_set:
                current_length += 1
                num += 1
            max_length = max(max_length, current_length)
        
        return max_length