# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 前序遍历——递归法
class Solution(object):
    def __init__(self):
        self.a = []

    def preorderTraversal(self, root):
        if not root:
            return []
        self.a.append(root.val)   #左子树->根节点->右子树
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return self.a


# 先序打印二叉树（非递归）
def preOrderTravese(node):
    stack = [node]
    res = []
    while len(stack) > 0:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    e = TreeNode(4)
    f = TreeNode(5)
    a.left = b
    a.right = c
    b.left = e
    b.right = f
    print(preOrderTravese(a))