class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = sorted(s)
        str2 = sorted(t)

        if ("".join(str1) == "".join(str2)) :
            return True
        else:
            return False