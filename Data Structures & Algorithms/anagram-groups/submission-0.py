class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            sorted_s = "".join(sorted(i))
            if sorted_s not in res:
                res[sorted_s] = [i]
            else:
                res[sorted_s].append(i)
        return list(res.values())