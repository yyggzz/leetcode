class Solution:

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        visited = []
        node = head
        while node:
            if node not in visited: # have not visited current node
                if node.next:
                    visited.append(node) # visited
                    node = node.next
                else:
                    return None
            if node in visited:
                return node
