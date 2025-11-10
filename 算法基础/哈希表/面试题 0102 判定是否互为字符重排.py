class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        
        s1_dict = {}
        for i in range(len(s1)):
            if s1[i] not in s1_dict:
                s1_dict[s1[i]] = 1
            else:
                s1_dict[s1[i]] += 1
        
        s2_dict = {}
        for i in range(len(s2)):
            if s2[i] not in s2_dict:
                s2_dict[s2[i]] = 1
            else:
                s2_dict[s2[i]] += 1
        
        if s1_dict == s2_dict:
            return True
        else:
            return False