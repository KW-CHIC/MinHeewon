# 역순 연결 리스트 (p.219)

#입력
#12345NULL

from typing import * 
 
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

def reverseList(head: ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev

list1 = ListNode(1)
list2 = ListNode(2)
list3 = ListNode(3)
list4 = ListNode(4)
list5 = ListNode(5)
list6 = ListNode('NULL')

head = list1
list1.next = list2
list2.next = list3
list3.next = list4
list4.next = list5
list5.next = list6

reverseList(head)
