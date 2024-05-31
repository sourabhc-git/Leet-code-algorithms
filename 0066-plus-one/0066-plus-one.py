class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Convert the list of digits to a string
        number_str = ''.join(map(str, digits))
        # Convert the string to an integer
        number = int(number_str)
        # Add 1 to the number
        incremented_number = number + 1
        # Convert the incremented number back to a string
        incremented_number_str = str(incremented_number)
        # Convert the string to a list of digits
        result_list = [int(digit) for digit in incremented_number_str]
        return result_list