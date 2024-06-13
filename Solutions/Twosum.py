class Solution:
    def twoSum(self, nums, target):
        num_to_index = {}
        
        for index, num in enumerate(nums):
            complement = target - num
            
            if complement in num_to_index:
                return [num_to_index[complement], index]
            
            num_to_index[num] = index
        
        return []  # Though the problem guarantees a solution, this handles unexpected cases

# Corrected Example Usage:
solution = Solution()  # Create an instance of the Solution class

nums1 = [2, 7, 11, 15]
target1 = 9
print(solution.twoSum(nums1, target1))  # Output: [0, 1]

nums2 = [3, 2, 4]
target2 = 6
print(solution.twoSum(nums2, target2))  # Output: [1, 2]

nums3 = [3, 3]
target3 = 6
print(solution.twoSum(nums3, target3))  # Output: [0, 1]
