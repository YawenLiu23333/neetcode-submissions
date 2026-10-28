class Solution:

    def encode(self, strs: List[str]) -> str:
        t = ""
        for s in strs:
            print(s)
            t += s
            t += "|"
        print(t)
        return t

    def decode(self, s: str) -> List[str]:
        output = []
        word = ""
        for i in range(len(s)):
            
            if s[i] != "|":
                word += s[i]
                print(word)
            else:
                output.append(word)
                word = ""
            i += 1

        return output
