from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def max_level_sum(root):
    if not root:
        return 0

    queue = deque([root])
    max_sum = float('-inf')
    level = 0

    while queue:
        level += 1
        level_sum = 0
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            level_sum += node.val

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        if level_sum > max_sum:
            max_sum = level_sum
            max_level = level

    return max_level

#Example:
# create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

max_level = max_level_sum(root)
print(max_level) 
