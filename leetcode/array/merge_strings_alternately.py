class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # merge concac
        # python
        # java
        # = pjyatvhaon

        word1.strip()
        word2.strip()

        n = min(len(word1), len(word2))
        
        resStr = ""

        i = 0

        while i < n :
            resStr += word1[i]
            resStr += word2[i]
            i+=1
        
        while i < len(word1):
            resStr += word1[i]
            i+=1

        while i < len(word2):
            resStr += word2[i]
            i+=1


        return resStr


if __name__ == "__main__":
    sol = Solution()
    res = sol.mergeAlternately("abc", "pqr")
    print(res)