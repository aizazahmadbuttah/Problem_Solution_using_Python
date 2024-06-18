class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        
        rows = [''] * numRows
        index = 0
        direction = 1
        
        for char in s:
            rows[index] += char
            if index == 0:
                direction = 1
            elif index == numRows - 1:
                direction = -1
            index += direction
        
        zigzag_string = ''.join(rows)
        return zigzag_string


sol = Solution()


s1 = "PAYPALISHIRING"
numRows1 = 3
output1 = sol.convert(s1, numRows1)
print("Input: s = '{}', numRows = {}".format(s1, numRows1))
print("Output: '{}'".format(output1))


s2 = "PAYPALISHIRING"
numRows2 = 4
output2 = sol.convert(s2, numRows2)
print("\nInput: s = '{}', numRows = {}".format(s2, numRows2))
print("Output: '{}'".format(output2))

s3 = "A"
numRows3 = 1
output3 = sol.convert(s3, numRows3)
print("\nInput: s = '{}', numRows = {}".format(s3, numRows3))
print("Output: '{}'".format(output3))
