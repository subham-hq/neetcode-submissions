class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        if len(s) == 0:
            longest = 0
            return longest

        seen = set()
        seen.add(s[l])
        longest = 1

        while r < len(s) and l <= r:
            if s[r] not in seen:
                seen.add(s[r])
                length = r - l + 1
                longest = max(length, longest)
                r += 1
                continue
            if s[r] in seen:
                seen.remove(s[l])
                l += 1
                continue
        
        return longest
