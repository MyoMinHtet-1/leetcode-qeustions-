class Solution:
    def romanToInt(self, s):
        dic = {
            "I": 1,
            'V': 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            'M': 1000
        }
        def split(word):
            return [char for char in word]
        s = split(s)
        current = 0 
        total = 0
        previous= 0
        for a in range(len(s)):
            current = dic.get(s[a])
            if current > previous: total = (total - previous)+ (current - previous)
            elif current == previous: total += current
            elif current<previous: total +=current
            previous = current
        return total
                
