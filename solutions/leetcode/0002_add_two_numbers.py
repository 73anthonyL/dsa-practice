# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        answer, carry, l1num, l2num = ListNode(-1), 0, 0, 0
        ret = answer
        while l1 or l2:
            if not l1:
                l1num = 0
            else:
                l1num = l1.val

            if not l2:
                l2num = 0
            else:
                l2num = l2.val

            rem, tens = (l1num + l2num + carry) % 10, (l1num + l2num + carry) // 10
            if answer.val == -1:
                answer.val = rem
                carry = tens
            else:
                answer.next = ListNode(rem)
                answer = answer.next
                carry = tens

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry:
            answer.next = ListNode(carry)
        return ret
