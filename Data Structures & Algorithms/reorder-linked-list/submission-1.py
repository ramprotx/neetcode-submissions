# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Your first solution implements the optimal three-step approach:

# Find the middle of the linked list using slow/fast pointers
# Reverse the second half of the list
# Merge the two halves alternately
# Let's trace through it with the example [2,4,6,8,10]:

# Step 1: Find middle
# Initial: slow = 2, fast = 4
# After 1st iteration: slow = 4, fast = 8
# After 2nd iteration: slow = 6, fast = None (loop stops)

# Middle is at node 6
# Step 2: Reverse second half (starting from 8)
# List state: 2 → 4 → 6 → (8 → 10 reversed) → 8 → 10 becomes 10 → 8 → None

# After reversal: 
# - First half: 2 → 4 → 6 → None
# - Second half: 10 → 8 → None
# Step 3: Merge alternately
# Iteration 1:
#   first = 2, second = 10
#   2 → 10 → 4 (rest of first)
#   Now: first = 4, second = 8

# Iteration 2:
#   first = 4, second = 8  
#   4 → 8 → 6 (rest of first)
#   Now: first = 6, second = None

# Loop ends since second is None

# Final result: 2 → 10 → 4 → 8 → 6 ✓

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         if not head:
#             return
#         nodes=[]
#         cur=head
#         while cur:
#             nodes.append(cur)
#             cur=cur.next
        
#         i,j = 0, len(nodes) - 1
#         while i<j:
#             nodes[i].next=nodes[j]
#             i+=1
#             if i>=j:
#                 break
#             nodes[j].next=nodes[i]
#             j-=1
#         nodes[i].next=None

        