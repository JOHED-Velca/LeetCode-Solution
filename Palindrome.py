"""
LeetCode Problem: Palindrome Number
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

def reverse_number(num: int) -> int:
    """Helper function to reverse a number"""
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    return reversed_num


class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = x
        if reverse_number(number) == number:
            return True
        else:
            return False


def test_palindrome():
    """Test function for the palindrome solution"""
    solution = Solution()
    
    # Test cases
    test_cases = [
        (121, True),
        (-121, False),
        (10, False),
        (0, True),
        (1, True),
        (12321, True),
        (123, False)
    ]
    
    print("Testing Palindrome Number Solution:")
    print("-" * 40)
    
    for i, (input_val, expected) in enumerate(test_cases, 1):
        result = solution.isPalindrome(input_val)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"Test {i}: isPalindrome({input_val}) = {result} (expected {expected}) {status}")
    
    print("-" * 40)


if __name__ == "__main__":
    test_palindrome()
    
    # Interactive testing
    print("\nInteractive Testing:")
    print("Enter a number to check if it's a palindrome (or 'quit' to exit):")
    
    solution = Solution()
    
    while True:
        user_input = input("Enter number: ").strip()
        if user_input.lower() in ['quit', 'q', 'exit']:
            break
        
        try:
            num = int(user_input)
            result = solution.isPalindrome(num)
            print(f"isPalindrome({num}) = {result}")
        except ValueError:
            print("Please enter a valid integer.")