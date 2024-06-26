class Solution:
        
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        
        # Count the frequency of each character in the text
        char_count = Counter(text)
        
        # Define the required counts for each character in the word "balloon"
        balloon_count = Counter("balloon")
        
        # Calculate the maximum number of "balloon" that can be formed
        return min(char_count[char] // balloon_count[char] for char in balloon_count)