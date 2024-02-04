class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if(haystack.find(needle)!=-1):
            return haystack.find(needle)
        else:
            return -1
