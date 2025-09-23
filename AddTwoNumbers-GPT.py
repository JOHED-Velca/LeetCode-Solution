# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: # 
        dummy = ListNode()   # dummy node to simplify edge cases (used to avoid checking if head is None)
        cur = dummy # pointer to construct the new list
        carry = 0 # carry for sum exceeding 10

        while l1 or l2 or carry: # iterate while there are nodes in l1 or l2 or there's a carry
            v1 = l1.val if l1 else 0 # get value from l1 or 0 if l1 is exhausted
            v2 = l2.val if l2 else 0 # get value from l2 or 0 if l2 is exhausted

            total = v1 + v2 + carry # sum the values and carry
            carry, digit = divmod(total, 10) # update carry and the digit to store in the node (10's place)

            cur.next = ListNode(digit) # create a new node with the digit
            cur = cur.next # move to the next node

            l1 = l1.next if l1 else None # move to the next node in l1 if available
            l2 = l2.next if l2 else None # move to the next node in l2 if available

        return dummy.next # return the next node of dummy which is the head of the result list


# Helper functions to create linked lists and display results
def create_linked_list(nums):
    """Create a linked list from a list of numbers"""
    if not nums:
        return None
    
    head = ListNode(nums[0])
    current = head
    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

def linked_list_to_list(head):
    """Convert linked list to Python list for easy display"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def print_linked_list(head, name="List"):
    """Print linked list in a readable format"""
    values = linked_list_to_list(head)
    print(f"{name}: {' -> '.join(map(str, values))} -> None")

# Test the solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: [2,4,3] + [5,6,4] = [7,0,8] (342 + 465 = 807)
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    
    print("Test Case 1:")
    print_linked_list(l1, "L1")
    print_linked_list(l2, "L2")
    
    result = solution.addTwoNumbers(l1, l2)
    print_linked_list(result, "Result")
    print(f"Represents: 342 + 465 = 807\n")
    
    # Test case 2: [0] + [0] = [0]
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    
    print("Test Case 2:")
    print_linked_list(l1, "L1")
    print_linked_list(l2, "L2")
    
    result = solution.addTwoNumbers(l1, l2)
    print_linked_list(result, "Result")
    print(f"Represents: 0 + 0 = 0\n")
    
    # Test case 3: [9,9,9,9,9,9,9] + [9,9,9,9] = [8,9,9,9,0,0,0,1]
    l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_linked_list([9, 9, 9, 9])
    
    print("Test Case 3:")
    print_linked_list(l1, "L1")
    print_linked_list(l2, "L2")
    
    result = solution.addTwoNumbers(l1, l2)
    print_linked_list(result, "Result")
    print(f"Represents: 9999999 + 9999 = 10009998")
