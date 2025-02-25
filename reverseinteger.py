class Solution:
    def reverse(self, interger):

        string = str(interger)
        reversed = list(string[::-1])
        if "-" in reversed:
            index = reversed.index('-')
            del reversed[index]
            reversed.insert(0, '-')
        interger = int(''.join(reversed))
        return interger if interger<2147483647 and interger>-2147483648 else 0
