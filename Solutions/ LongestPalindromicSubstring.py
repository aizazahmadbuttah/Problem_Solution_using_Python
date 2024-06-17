class Solution(object):
    def longestPalindrome(self, s):
       
        # Agar string khali hai to khali string return karo
        if not s:
            return ""
        
        # Yeh function center se expand karta hai jab tak characters match karte hain
        def expandAroundCenter(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Is center ke andar sabse lamba palindrome return karo
            return s[left + 1:right]
        
        longest = ""
        for i in range(len(s)):
            # Wale palindromes jo odd length ke hain
            palindrome1 = expandAroundCenter(s, i, i)
            # Wale palindromes jo even length ke hain
            palindrome2 = expandAroundCenter(s, i, i + 1)
            
            # Sabse lamba palindrome update karo agar naya wala lamba ho
            if len(palindrome1) > len(longest):
                longest = palindrome1
            if len(palindrome2) > len(longest):
                longest = palindrome2
        
        return longest

# Example usage:
solution = Solution()
print(solution.longestPalindrome("babad"))  # Output: "bab" ya "aba"
print(solution.longestPalindrome("cbbd"))   # Output: "bb"
