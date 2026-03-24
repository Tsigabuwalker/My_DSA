class Solution:
    def getAllElements(self, root1, root2):
        
        # inorder traversal
        def inorder(root, arr):
            if not root:
                return
            inorder(root.left, arr)
            arr.append(root.val)
            inorder(root.right, arr)
        
        list1, list2 = [], []
        
        inorder(root1, list1)
        inorder(root2, list2)
        
        # merge two sorted lists
        i = j = 0
        result = []
        
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1
        
        # add remaining elements
        result.extend(list1[i:])
        result.extend(list2[j:])
        
        return result