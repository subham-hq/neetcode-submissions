class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        counter = {}
        res = 0

        for r in range(len(s)):
            counter[s[r]] = counter.get(s[r], 0) + 1
            window = r - l + 1
            maxF = max(counter.values())
            if window - maxF <= k:
                res = max(window, res)
            else:
                counter[s[l]] -= 1
                l += 1

        return res