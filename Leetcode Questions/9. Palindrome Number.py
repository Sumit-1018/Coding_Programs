class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        # Store the number in a variable
        number = (str(x))[::-1]
        # This will store the reverse of the number
        
        return x == int(number)