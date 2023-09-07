# You are given the head of a linked list. Delete the middle node, and return 
# the head of the modified linked list.


# Solution: Two pointers
# Instead of passing through the list twice - once to determine the length and
# once to find the middle - we can pass through once using two pointers. The
# first pointer moves one step at a time while the second pointer moves two 
# steps at a time. Once the second pointer reaches the end, the first will be
# at the middle.


def deleteMiddle(self, head):
        if head.next == None:
            head = None
            return head
        
        middle = head
        end = head.next.next

        while end != None and end.next != None:
            middle = middle.next
            end = end.next.next 
        
        middle.next = middle.next.next
        return head