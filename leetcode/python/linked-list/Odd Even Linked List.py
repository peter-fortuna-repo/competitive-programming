# Link to problem: https://leetcode.com/problems/odd-even-linked-list/


# Solution:
# This solution firsts finds the end of the linked list and then appends even
# nodes to the end.

# Time complexity: O(n) 
# Space complexity: O(1)

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        tail = head
        while tail.next != None:
            tail = tail.next
        midpoint = tail

        odd = head
        even = head.next
        while odd != midpoint and even != midpoint:
            tail.next = ListNode(even.val)
            tail = tail.next

            odd.next = odd.next.next 
            odd = odd.next
            
            even = odd.next
        
        if even == midpoint:
            tail.next = ListNode(midpoint.val)
            odd.next = odd.next.next

        return head