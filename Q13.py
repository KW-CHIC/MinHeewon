# 팰린드롬 연결 리스트 (p.201) 풀이2 참조

from typing import List
import collections

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None
 
def is_palindrome(head: ListNode) -> bool:
    q = collections.deque()
 
    if not head:
        return True
 
    node = head
    while node is not None:
        q.append(node.val)
        node = node.next
 
    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
 
    return True
 
list1 = ListNode(1)
list2 = ListNode(2)
list3 = ListNode(2)
list4 = ListNode(1)
 
head = list1
list1.next = list2
list2.next = list3
list3.next = list4
 
print(is_palindrome(head))
