# 두 정렬 리스트의 병합 (p.213)

from typing import * 
 
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = mergeTwoLists(l1.next, l2)
    return l1

list11 = ListNode(1)
list12 = ListNode(2)
list13 = ListNode(4)
list21 = ListNode(1)
list22 = ListNode(3)
list23 = ListNode(4)

l1 = list11
list11.next = list12
list12.next = list13
l2 = list21
list21.next = list22
list22.next = list23

mergeTwoLists(l1, l2)
