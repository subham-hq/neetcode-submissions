class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for string in strs:
            encoded += str(len(string)) + "#" + string
        
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        str_length = len(s)
        i = 0
        j = i

        while i < str_length:
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])

            decoded.append(s[j + 1 : j + 1 + length])
            
            i = j + 1 + length
            j = i

        return decoded

            
