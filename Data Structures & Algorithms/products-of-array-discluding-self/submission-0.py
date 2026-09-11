class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        output = []

        product = 1
        for num in nums:
            prefix.append(product)
            product *= num

        product = 1
        for num in nums[::-1]:
            suffix.append(product)
            product *= num

        suffix = suffix[::-1]

        for p, s in zip(prefix, suffix):
            output.append(p * s)
        
        return output