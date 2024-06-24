class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            current_area = width * h
            max_area = max(max_area, current_area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

# Example usage with the first two inputs
inputs = [
    [1, 8, 6, 2, 5, 4, 8, 3, 7],
    [1, 1]
]

solution = Solution()
for i, height in enumerate(inputs):
    result = solution.maxArea(height)
    print("Input {}: {} => Output: {}".format(i+1, height, result))
