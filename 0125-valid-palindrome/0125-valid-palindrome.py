import re
class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_text = re.sub(r'[^a-z0-9]','',s.lower())
        print(new_text)
        if new_text == new_text[::-1]:
            return True
        else:
            return False