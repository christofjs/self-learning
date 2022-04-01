class Solution():
    def preorder(self, root):
        # preorder dfs traversal of nary tree, recursive solution
        preord = []
        if root is None:
            return preord
        self.dfs(root, preord)
        return preord
    
    def dfs(self, root, preord):
        preord.append(root.val)
        for child in root.children:
            self.dfs(child, preord)

    def preorder2(self, root):
        # preorder dfs traversal of nary tree, iterative solution
        if not root:
            return []
        traversal = [root]
        preord = []
        while traversal:
            nextNode = traversal.pop()
            preord.append(nextNode.val)
            for child in nextNode.children[::-1]:
                traversal.append(child)
        return preord
        