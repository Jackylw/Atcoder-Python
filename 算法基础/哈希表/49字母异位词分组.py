from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}
        for s in strs:
            str_sort = ''.join(sorted(s))
            if str_sort not in str_dict:
                str_dict[str_sort] = []
            str_dict[str_sort].append(s)
        # 直接返回字典中所有值的列表，确保是二维数组
        return list(str_dict.values())

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(Solution().groupAnagrams([""]))
print(Solution().groupAnagrams(["a"]))