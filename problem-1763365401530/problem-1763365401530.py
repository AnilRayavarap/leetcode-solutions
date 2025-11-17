# Last updated: 11/17/2025, 1:43:21 AM
class Solution:
    def deleteDuplicates(self , head):
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head