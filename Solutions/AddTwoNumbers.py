class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):

        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = carry + x + y
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummy.next


def create_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def print_linked_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

solution = Solution()


l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])
result = solution.addTwoNumbers(l1, l2)
print(print_linked_list(result))


l1 = create_linked_list([0])
l2 = create_linked_list([0])
result = solution.addTwoNumbers(l1, l2)
print(print_linked_list(result))


l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = create_linked_list([9, 9, 9, 9])
result = solution.addTwoNumbers(l1, l2)
print(print_linked_list(result))
