# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_str = ''
        l2_str = ''
        head_obj1 = l1.next
        l1_val = l1.val
        l1_str += str(l1_val)
        while head_obj1:
            l1_val = head_obj1.val
            l1_str += str(l1_val)
            head_obj1 = head_obj1.next

        head_obj2 = l2.next
        l2_val = l2.val
        l2_str += str(l2_val)

        while head_obj2:
            l2_val = head_obj2.val
            l2_str += str(l2_val)
            head_obj2 = head_obj2.next

        res_int = int(l1_str[::-1]) + int(l2_str[::-1])
        res_str = str(res_int)[::-1]
        res_l_reverse_lst = [int(i) for i in res_str]

        head_obj = ListNode(int(res_l_reverse_lst[0]))
        head = head_obj

        for data in res_l_reverse_lst[1:]:
            node = ListNode(data)
            head.next = node
            head = node

        return head_obj