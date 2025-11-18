# Last updated: 11/18/2025, 2:48:38 AM
class Solution:
    def hasCycle(self, head):
        visited = set()
        current = head

        while current:
            if current in visited:
                return True

            visited.add(current)
            current = current.next

        return False
