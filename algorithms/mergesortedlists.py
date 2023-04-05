class ListNode(object):
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next
        
    def __str__(self) -> str:
        return f"{self.val} -> "

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
            
        if list1 or list2:
            cur.next = list1 if list1 else list2
        
        return dummy.next       
    


if __name__ == "__main__":
    c = ListNode(val=5)
    b = ListNode(val=3, next=c)
    a = ListNode(val=1, next=b)
    
    
    z = ListNode(val=6)  
    y = ListNode(val=4, next=z)
    x = ListNode(val=2, next=y)
    
    newList = Solution.mergeTwoLists(Solution, a, x)
    
    string = ""
    while newList:
        if newList.next == None:
            string += f"{newList.val}"
            newList = newList.next
        else:
            string += f"{newList.val} -> "
            newList = newList.next
    print(string)
    
    
    
    
    
    