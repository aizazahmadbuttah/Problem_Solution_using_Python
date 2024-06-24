class Solution(object):
    def isPalindrome(self, x):
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Numbers ending in 0 (except 0 itself) are not palindromes
        if x != 0 and x % 10 == 0:
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # When the length is an odd number, we can get rid of the middle digit by reversed_half // 10
        return x == reversed_half or x == reversed_half // 10

# Example usage
sol = Solution()
print(sol.isPalindrome(121))  
print(sol.isPalindrome(-121)) 
print(sol.isPalindrome(10))   
print(sol.isPalindrome(0))    
        