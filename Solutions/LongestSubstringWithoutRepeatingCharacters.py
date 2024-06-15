# Suggested code may be subject to a license. Learn more: ~LicenseLog:3311609712.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
      
        n = len(s)
        char_set = set()
        left = 0
        max_length = 0

        for right in range(n):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length


solution = Solution()


s1 = "abcabcbb"
print(solution.lengthOfLongestSubstring(s1))  


s2 = "bbbbb"
print(solution.lengthOfLongestSubstring(s2))  


s3 = "pwwkew"
print(solution.lengthOfLongestSubstring(s3))  
