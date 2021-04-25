from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def genBT(vals: List)->TreeNode:
    Root = TreeNode(None)
    def gen(Root:TreeNode, vals: List)->TreeNode:
        if len(vals)==0:
            return Root
        if vals[0]!='#':
            Root = TreeNode(vals.pop(0))
            Root.left = gen(Root.left,vals)
            Root.right = gen(Root.right,vals)
            return Root
        else:
            Root = None
            vals.pop(0)
            return Root
    return gen(Root,vals)

def printBT (Tree: TreeNode)->List:
    res = []
    def dfs(root):
        if not root:
            res.append('#')
            return
        res.append(root.val)
        dfs(root.left)
        dfs(root.right)
    dfs(Tree)
    return res