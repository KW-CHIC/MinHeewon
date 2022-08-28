# 페어의 노드 스왑 (p.229) 풀이3 참조

from typing import * 
 
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None
        
def swapPairs(head: ListNode) -> ListNode:
    if head and head.next:
        p = head.next
        # 스왑된 값 리턴 받음
        head.next = self.swapPairs(p.next)
        p.next = head
        return p
    return head