from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        list_len = len(nums)
        set_len = len(set(nums))
        if list_len == set_len:
            return False
        else:
            return True