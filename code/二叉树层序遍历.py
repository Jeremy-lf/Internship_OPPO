
# 广度优先遍历
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            length = len(queue)
            level = []
            for i in range(length):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(level)
        return res


class Solution2(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        queue = [[root]]
        res = []
        while queue:
            layer = queue.pop(0)
            temp_queue = []
            temp_res = []
            for node in layer:
                if not node:
                    continue
                temp_res.append(node.val)
                temp_queue += [node.left, node.right]
                print(node.right)
                print(temp_queue)
            if not temp_queue:
                break
            res.append(temp_res)
            queue.append(temp_queue)
        return res