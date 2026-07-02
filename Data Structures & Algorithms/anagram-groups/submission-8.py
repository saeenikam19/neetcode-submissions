from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups={}
        for i in strs:
            result=" ".join(sorted(i))
            if result not in groups:
                groups[result]=[]
            groups[result].append(i)
        return list(groups.values())