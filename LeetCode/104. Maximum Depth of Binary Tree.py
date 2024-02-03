# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#BFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None :
            return 0
        q = deque()
        max_depth = 0
        q.append(root, max_depth)
        while q :
            current_node, max_depth = q.popleft()
        
            if current_node.left :
                q.append(current_node.left, max_depth + 1)
            if current_node.right :
                q.append(current_node.right, max_depth + 1)
        return max_depth

#DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None :
            return 0
        
        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1
        
        if left > right :
            return left
        else :
            return right