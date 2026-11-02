# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif list1 and not list2:
            return list1
        elif list2 and not list1:
            return list2
        else:
            if list1.val < list2.val:
                head = ListNode(list1.val)
                list1 = list1.next
            else:
                head = ListNode(list2.val)
                list2 = list2.next

            progressor = head
        while list1 or list2:
            if not list1:
                progressor.next = ListNode(list2.val)
                progressor = progressor.next
                list2 = list2.next
            elif not list2:
                progressor.next = ListNode(list1.val)
                progressor = progressor.next
                list1 = list1.next
            elif list2.val < list1.val:
                progressor.next = ListNode(list2.val)
                progressor = progressor.next
                list2 = list2.next
            elif list1.val <= list2.val:
                progressor.next = ListNode(list1.val)
                progressor = progressor.next
                list1 = list1.next
        
        return head




        