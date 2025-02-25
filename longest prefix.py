class Solution:
    def longestCommonPrefix(self ,strs):
        if '' in strs: return ''
        elif len(strs) == 1: return strs[0]
        prev = []
        current = []
        strs.sort()
        lenstrs = len(strs[0])
        for a in range(lenstrs):
            for num in strs:
                current.append(num[a])
            if all(x == current[0] for x in current):
                prev.append(list(set(current)))
            else:
                break
            current = []
        return ''.join([' '.join([str(elem) for elem in sublist]) for sublist in prev])
