# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def merge(low, high):
            if low > high:
                return None
            mid = (low + high) // 2
            root = TreeNode(nums[mid])
            root.left = merge(low, mid - 1)
            root.right = merge(mid + 1, high)
            return root
        return merge(0, len(nums) - 1)
        
            
        