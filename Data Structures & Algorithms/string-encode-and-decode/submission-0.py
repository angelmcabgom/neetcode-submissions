class Solution:
    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            # Pattern: [length][delimiter][string]
            # Example: "3#lol"
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            # Move j until we hit the delimiter
            while s[j] != "#":
                j += 1
            
            # The number is everything between i and j
            length = int(s[i:j])
            
            # Move i to the start of the actual string (skip the '#')
            i = j + 1
            
            # Extract the string based on the length we found
            res.append(s[i : i + length])
            
            # Move i to the start of the NEXT block
            i += length
            
        return res

solution = Solution()
test1 = ["lol", "xd", "adios"]
encoded = solution.encode(test1)
print(f"Encoded string: {encoded}") # Should look like "3#lol2#xd5#adios"
print(f"Decoded list:   {solution.decode(encoded)}")