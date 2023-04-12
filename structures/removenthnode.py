class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution():
    """ Leetcode Doesnt like this solution but it works """
    def removeNthFromEnd(self, head: ListNode, n: int):
        nodes = []
        last = -1
        curr = 0
        future = 1
        while head != None:
            nodes.append(head)
            head = head.next
            
        while curr != None:
            if n == 0:
                if future < len(nodes):
                    nodes[last].next = nodes[future]
                    nodes.remove(nodes[curr])
                    return nodes
                else:
                    nodes[last].next = None
                    nodes.remove(nodes[curr])
                    return nodes
            else:
                last += 1
                curr += 1
                future += 1
                n -= 1 
                
    def leetcodeSolution(self, head):
        fast , slow = head, head
        while fast.next:
            if not fast: return head.next
        while fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head
                   
    def test(self, head):
        representation = ""
        while head != None:
            representation += f"{head.val} -> "
            head = head.next
        print(representation)


e = ListNode(val=5)
d = ListNode(val=4, next=e)
c = ListNode(val=3, next=d)
b = ListNode(val=2, next=c)
a = ListNode(val=1, next=b)

Solution().test(a)

Solution().removeNthFromEnd(a, 4)
Solution().test(a)