class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        'get the character count for each value and store and then add matching character words in to sublist'
        'use Counter to count the char in a word. To group combinations'
        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            groups[tuple(count)].append(s)
        return list(groups.values())