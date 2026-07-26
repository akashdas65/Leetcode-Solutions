# LeetCode 82 - Remove Duplicates from Sorted List II
# Category: Linked List

# Approach:
# Use a dummy node before the head to handle edge cases where the first
# few nodes are duplicates. Maintain a pointer `prev` to the last node
# known to be unique.
# Traverse the list:
# - If the current node has duplicates, skip all nodes with that value
#   and connect `prev` to the next distinct node.
# - Otherwise, move `prev` forward.
# Continue until the end of the list and return `dummy.next`.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next

            head = head.next

        return dummy.next