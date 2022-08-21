# 두 수의 덧셈 (p.221)

from typing import * 
 
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None
        
# 연결 리스트 뒤집기
def reverseList(head: ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev

# 연결 리스트를 파이썬 리스트로 변환
def toList(node: ListNode) -> List:
    list: List = []
    while node:
        list.append(node.val)
        node = node.next
    return list

# 파이썬 리스트를 연결 리스트로 변환
def toReversedLinkedList(result: str) -> ListNode:
    prev: ListNode = None
    for r in result:
        node = ListNode(r)
        node.next = prev
        prev = node

    return node

# 두 연결 리스트의 덧셈
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    a = toList(reverseList(l1))
    b = toList(reverseList(l2))

    resultStr = int('', join(str(e) for e in a)) + \
                int('', join(str(e) for e in b))

    # 최종 계산 결과 연결 리스트로 변환
    return toReversedLinkedList(str(resultStr))
