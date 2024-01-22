class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x<0):
            return False
        else:
            pal_check=0
            num=x
            while(num!=0):
                temp=n%10
                pal_check=pal_check*10+temp
                num//=10
            return pal_check==x
