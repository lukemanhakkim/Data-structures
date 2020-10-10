"""
Author: Lukeman hakkim Sheik Alavudeen

Description:
Depth First Search - Inorder, Preorder, Postorder traversals
Breadth First Search - Level order Traversal
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

import queue

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

#With Recursion

#Inorder Traversal(left, root, right)

def Inorder(root):
    if root:

        Inorder(root.left)
        print(root.data, end = " ")
        Inorder(root.right)

#IPreorder Traversal(root, left, right)

def Preorder(root):
    if root:
        print(root.data, end=" ")
        Preorder(root.left)
        Preorder(root.right)

#Postorder Traversal(left, right, root)

def Postorder(root):
    if root:

        Postorder(root.left)
        Postorder(root.right)
        print(root.data, end=" ")

#Without Recursion

def Inorder_without_recursion(root, result):

    if root is None:
        return
    stack=[]
    curr=root

    while stack or curr:

        if curr:
            stack.append(curr)
            curr=curr.left
        else:
            curr=stack.pop()
            result.append(curr.data)
            curr=curr.right
    return result


# Without Recursion

def Preorder_without_recursion(root, result):

    if root is None:
        return

    stack = []
    stack.append(root)

    while stack:
            curr = stack.pop()
            result.append(curr.data)
            if curr.right:
               stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

    return result

# Without Recursion

def Postorder_without_recursion(root, result):

    if root is None:
        return

    stack = []
    stack.append(root)

    while stack:
            curr = stack.pop()
            result.append(curr.data)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
               stack.append(curr.right)

    #Its in stack so have to print in reverse or use pop function to print
    return result[::-1]



#Breadth First Search (Level Order Traversal)

def levelordertraversal(root, result):
    if root is None:
        return

    q = queue.Queue()
    q.put(root)
    node = None

    while not q.empty():
        node = q.get()
        result.append(node.data)

        if node.left is not None:
            q.put(node.left)
        if node.right is not None:
            q.put(node.right)

    return result

#Driver code
if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("\nInorder traversal")
    Inorder(root)

    print("\nPreorder traversal")
    Preorder(root)

    print("\nPostorder traversal")
    Postorder(root)

    result=[]
    inorder = Inorder_without_recursion(root, result)
    print("\nInorder traversal without recursion")
    print(inorder)

    result=[]
    preorder=Preorder_without_recursion(root, result)
    print("Preorder traversal without recursion")
    print(preorder)

    result = []
    postorder = Postorder_without_recursion(root, result)
    print("Postorder traversal without recursion")
    print(postorder)

    result = []
    levelorder = levelordertraversal(root, result)
    print("Levelorder traversal")
    print(levelorder)



























