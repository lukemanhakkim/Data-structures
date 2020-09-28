"""
Author: Lukeman hakkim Sheik Alavudeen
Description: Depth First Search - Inorder, Preorder, Postorder traversals
"""

"""
Binary Tree Node     
         |
         |
  |-------------|
  |    data     |
  |-------------|
  | left | right|
  |-------------|
"""

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

#Inorder Traversal(left, root, right)

def Inorder(root):
    if root:

        Inorder(root.left)
        print(root.data, end = " ")
        Inorder(root.right)

def Preorder(root):
    if root:
        print(root.data, end=" ")
        Preorder(root.left)
        Preorder(root.right)

def Postorder(root):
    if root:

        Postorder(root.left)
        Postorder(root.right)
        print(root.data, end=" ")


#Driver code
if __name__ == '__main__':

    root = Node(8)
    root.left = Node(9)
    root.right = Node(7)
    root.left.left = Node(5)
    root.left.right = Node(6)

    print("\nInorder traversal")
    Inorder(root)

    print("\nPreorder traversal")
    Preorder(root)

    print("\nPostorder traversal")
    Postorder(root)