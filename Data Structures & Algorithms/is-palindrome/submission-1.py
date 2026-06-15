class Solution:
    def isPalindrome(self, s: str) -> bool:
        # #Brute force appraoch
        # cleaned = "".join(ch for ch in s if ch.isalnum()).lower()
        # return cleaned == cleaned[::-1]
        
        #Optimal approach
        cleaned = "".join(c for c in s if c.isalnum()).lower()
        left = 0
        right = len(cleaned) - 1
        while left <= right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right = right - 1
        
        return True
        