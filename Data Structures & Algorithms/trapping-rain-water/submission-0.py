class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)

        prefix[0] = height[0]

        for i in range(1, len(height)):
            prefix[i] = max(prefix[i-1], height[i])
        
        suffix = [0] * len(height)

        suffix[-1] = height[-1]

        for i in range(len(height) - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], height[i])

        trapped = 0
        for i in range(len(height)):
            trapped += min(prefix[i], suffix[i]) - height[i]

        return trapped