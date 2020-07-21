"""
Approach

1. Traverse each element in the array and check target - currentNumber is in map or not
2. if target - currentNumber is not in the map then we add the currentNumber in the map as key and its index as value
3. if target - currentNumber is in the map then we return the current index and the value corresponding to target - currentNumber form the map


"""

# Time Complexity : O(n) 
# Space Complexity : O(n) 
# Did this code successfully run on Leetcode : yes	
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = {}
        for i in range(len(nums)):
            if not target-nums[i] in map1:
                map1[nums[i]]=i
            else:
                return [i,map1[target-nums[i]]]
            return output