class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        freq = [[] for _ in range(len(nums) + 1)]

        for num, frequency in count.items():
            freq[frequency].append(num)
        
        topk = []

        for bucket in reversed(freq):
            for num in bucket:
                topk.append(num)

                if len(topk) == k: 
                    return topk
