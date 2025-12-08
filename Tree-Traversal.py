# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ---------- Recursive Traversals ----------
def preorder(root):
    if not root:
        return []
    # Root -> Left -> Right
    return [root.val] + preorder(root.left) + preorder(root.right)

def inorder(root):
    if not root:
        return []
    # Left -> Root -> Right
    return inorder(root.left) + [root.val] + inorder(root.right)

def postorder(root):
    if not root:
        return []
    # Left -> Right -> Root
    return postorder(root.left) + postorder(root.right) + [root.val]

# ---------- Iterative Traversals ----------
def preorder_iter(root):
    if not root:
        return []
    stack, res = [root], []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res

def inorder_iter(root):
    res, stack = [], []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res

def postorder_iter(root):
    if not root:
        return []
    stack, res = [root], []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return res[::-1]  # reverse the result

# ---------- Level-order Traversal (BFS) ----------
from collections import deque
def level_order(root):
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res

# ---------- Example Usage ----------
if __name__ == "__main__":
    # Tree: 
    #      1
    #     / \
    #    2   3
    #   / \
    #  4   5
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))

    print("Preorder:", preorder(root))
    print("Inorder:", inorder(root))
    print("Postorder:", postorder(root))
    print("Preorder Iter:", preorder_iter(root))
    print("Inorder Iter:", inorder_iter(root))
    print("Postorder Iter:", postorder_iter(root))
    print("Level-order:", level_order(root))
