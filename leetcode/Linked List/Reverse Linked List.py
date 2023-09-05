# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Solution 1: Iterative
# We loop through the list one time and adjust the pointers to the next 
# element. To perform this in place, we use a few variables to store the nodes
# we're updating.

# Computational complexity: O(n) 
# Space complexity: O(1)

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head == None:
        return
    current_node = head
    next_node = head.next
    head.next = None

    while next_node != None:
        current = next_node
        next_node = current.next
        current.next = head
        head = current

    return head



# Solution 2: Recursive
# The same approach is used, but done recursively.

# Computational complexity: O(n)
# Space complexity: O(1)

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    return self.reverseListNext(None, head)

def reverseListNext(self, current, target):
    if target == None:
        return current
    next = target.next
    target.next = current
    return self.reverseListNext(target, next)