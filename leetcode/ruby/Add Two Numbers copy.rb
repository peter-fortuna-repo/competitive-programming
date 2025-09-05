# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def add_two_numbers(l1, l2)
    return l1 if l2.nil?
    return l2 if l1.nil?
    result = ListNode.new(0)
    current = result
    carry = 0
    while !l1.nil? || !l2.nil?
        sum = carry
        sum += l1.val if !l1.nil?
        sum += l2.val if !l2.nil?
        carry = sum / 10
        current.next = ListNode.new(sum % 10)
        current = current.next
        l1 = l1.next if !l1.nil?
        l2 = l2.next if !l2.nil?
    end
    current.next = ListNode.new(carry) if carry > 0
    result.next
end
