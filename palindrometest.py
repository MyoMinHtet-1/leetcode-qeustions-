class Solution:
    def isPalindrome(self, x):
        reversedx = str(x)
        reversedx = reversedx[::-1]
        if x == 0:
            return True
        if (x % 10) == 0 or x<0:
            return False
        elif reversedx == str(x):
            return True
        else:
            return False
