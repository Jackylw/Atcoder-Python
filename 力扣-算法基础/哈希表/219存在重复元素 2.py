from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] not in nums_dict:
                nums_dict[nums[i]] = i
            else:
                if abs(i - nums_dict[nums[i]]) <= k:
                    return True
                else:
                    nums_dict[nums[i]] = i
        return False

print(Solution().containsNearbyDuplicate([1,2,3,1], 3))
print(Solution().containsNearbyDuplicate([1,0,1,1], 1))
print(Solution().containsNearbyDuplicate([1,2,3,1,2,3], 2))