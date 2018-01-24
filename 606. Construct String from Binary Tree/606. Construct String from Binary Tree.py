class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        #对每个树节点进行判断  迭代
        def tree(t):
            #TreeNode   (left right val)
            if t.left != None and t.right != None:
                return str(t.val)+'('+tree(t.left)+')'+'('+tree(t.right)+')'
            elif t.left != None and t.right == None:
                return str(t.val)+'('+tree(t.left)+')'
            elif t.left == None and t.right != None:
                return str(t.val)+'()'+'('+tree(t.right)+')'
            else:
                return str(t.val)
        try:
            return tree(t)
        except:
            return ""
