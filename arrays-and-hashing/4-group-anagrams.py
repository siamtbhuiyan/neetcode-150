class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = collections.defaultdict(list)
        for string in strs:
            count = [0]*26
            for char in string:
                count[ord(char) - ord("a")] += 1
            results[tuple(count)].append(string)
        return results.values()
