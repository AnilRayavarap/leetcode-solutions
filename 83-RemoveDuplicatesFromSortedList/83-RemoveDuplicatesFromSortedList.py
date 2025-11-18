# Last updated: 11/18/2025, 2:48:54 AM
class Solution:
    def deleteDuplicates(self , head):
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head