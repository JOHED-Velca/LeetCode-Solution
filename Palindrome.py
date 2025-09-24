class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = x
        if number.reversed() == number:
            return true
        else:
            return false