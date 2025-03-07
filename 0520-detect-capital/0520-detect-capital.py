class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        # First two conditions        
        # Check if we have one char
        if len(word) == 1:
            return True
        
        if word.isupper() or (word[0].isupper() and word[1:].islower()) or (word.islower()):
            return True
        
        return False
         


