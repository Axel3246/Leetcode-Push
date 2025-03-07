class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        mys = set()
        ans = []

        for char in word:
            if char not in mys:
                if (char.lower() in mys and char.lower() not in ans) or (char.upper() in mys and char.lower() not in ans):
                    ans.append(char.lower())
            mys.add(char)
            

        print(mys, ans)
        return len(ans)