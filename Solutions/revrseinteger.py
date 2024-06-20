class Solution(object):
    def reverse(self, x):
       
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        
        reversed_num = 0
        
        
        sign = 1 if x >= 0 else -1
        
        
        x = abs(x)
        
        while x != 0:
            
            pop = x % 10
            x //= 10
            
            
            if (reversed_num > INT_MAX // 10) or (reversed_num == INT_MAX // 10 and pop > 7):
                return 0  
            if (reversed_num < INT_MIN // 10) or (reversed_num == INT_MIN // 10 and pop > 8):
                return 0 
            
           
            reversed_num = reversed_num * 10 + pop
        
        return sign * reversed_num


solution = Solution()
print(solution.reverse(123))  
print(solution.reverse(-123)) 
print(solution.reverse(120))   
print(solution.reverse(1534236469))  
