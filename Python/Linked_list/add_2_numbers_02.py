class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def solution(l1, l2):
    """
        You are given two non-empty linked lists representing two non-negative integers. 
        The digits are stored in reverse order, and each of their nodes contains a single digit. 
        Add the two numbers and return the sum as a linked list.

        You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    """
    dummy = ListNode()
    cur = dummy

    courier = 0
    while l1 or l2 or courier:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        val = v1 + v2 + courier
        courier = val // 10
        val = val % 10
        cur.next = ListNode(val)

        cur = cur.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next

