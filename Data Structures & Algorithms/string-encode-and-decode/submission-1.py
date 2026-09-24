class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in strs:
            result += str(len(i))
            result += '#'
            result += i
        return result

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        result = []
        i = 0
        n = len(s)
        while i < n:
            j = i

            while s[j] != '#':
                j += 1
            
            length = int(s[i : j])

            i = j + 1
            j = i + length

            result.append(s[i : j])

            i = j
        return result 
