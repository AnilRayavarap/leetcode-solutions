# Last updated: 11/21/2025, 1:10:06 AM
class Solution:
    def getIntersectionNode(self , headA , headB):
        if not headA or not headB:
            return None
        
        p1 , p2 = headA , headB

        while p1 != p2:
            if p1 is None:
                p1 = headB
            else:
                p1 = p1.next
            if p2 is None:
                p2 = headA
            else:
                p2 = p2.next
        return p1 or p2