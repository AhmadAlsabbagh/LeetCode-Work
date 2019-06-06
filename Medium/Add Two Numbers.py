# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        checker1 = l1
        num1 = ""
        while (checker1 != None):
            num1 = str(checker1.val) + num1
            checker1 = checker1.next
        checker2 = l2
        num2 = ""
        while (checker2 != None):
            num2 = str(checker2.val) + num2
            checker2 = checker2.next

        out1 = int(num1)
        out2 = int(num2)
        output = out1 + out2
        final = str(output)
        final_r = final[::-1]

        head = ListNode(-1)
        temp = head

        for x in final_r:
            temp.val = int(x)
            temp.next = ListNode(-1)
            temp = temp.next
        temp2 = head
        while (temp2 != None):
            if temp2.next.val == -1:
                temp2.next = None
            temp2 = temp2.next
        return head