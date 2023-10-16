# Link to problem: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list


# Solution 1: Stack
# We use the two pointer method to efficiently identify the middle of the array
# and copy the front half of the array to a stack. Then, we pop off the end of 
# the stack as we pass through the second half of the array and compute each 
# twin sum.

# Time complexity: O(n) 
# Space complexity: O(n)

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        front_half = []
        max_sum = 0
        p1 = head
        p2 = head

        while p2 != None:
            front_half.append(p1)
            p1 = p1.next
            p2 = p2.next.next

        node = p1
        while node != None:
            twin = front_half.pop()
            max_sum = max(max_sum, node.val + twin.val)
            node = node.next 
        
        return max_sum
    
# Solution 2: Reverse list
# This method starts by identifying the middle point the same way as solution 
# 1, and then flips the second half of the array instead of creating a stack.
# This method modifies the linked list in place, which results in O(1) space
# needed.

# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_sum = 0
        slow, fast = head, head

        while fast != None:
            slow = slow.next
            fast = fast.next.next
        
        curr, prev = slow, None
        while curr != None:
            prev, curr.next, curr = curr, prev, curr.next

        node, twin = head, prev
        while twin != None:
            max_sum = max(max_sum, node.val + twin.val)
            node, twin = node.next, twin.next
        
        return max_sum
