class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # 1. Create a variable holding the first string
        ans = strs[0]

        # 2. Iterate through each word from the index one of the list
        for word in strs[1:]:

            # 3. Generate an empty string that will hold the prefix and an iterator
            currStr = ""
            i = 0

            # 4. Iterate the current word while the iterator is less than the min lenght of the two words
            # and while the characters match in each word
            while i < len(min(ans, word)) and word[i] == ans[i]:
                # 5. Append each char to the currStr and add 1 to iterator
                currStr += word[i] 
                i += 1

            # 5. ANS will be updated to "" or the new prefix if the while managed to run
            ans = currStr
        
        return ans 


        