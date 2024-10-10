class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merge = ""
        j = 0
        k = 0
        for i in range( 0, len(word1) + len(word2)):
            if j < len(word1):
                merge = merge + word1[j]
                j+= 1
            if k < len(word2):
                merge = merge + word2[k]
                k+= 1

        return merge
        