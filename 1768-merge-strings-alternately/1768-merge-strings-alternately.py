class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        n = len(word1) if len(word1) < len(word2) else len(word2)
            
        final_answer = []
        word1 = list(word1)
        word2 = list(word2)
        for i in range(0, n):
            
            final_answer.append(word1[i])
            final_answer.append(word2[i])

        if n == len(word1):
            final_answer.extend(word2[n:])
        else:
            final_answer.extend(word1[n:])
            
        return "".join(final_answer)  
            