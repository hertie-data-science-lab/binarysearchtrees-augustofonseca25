# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:18:23 2023

@author: Hannah
"""

from mlbt import MutableLinkedBinaryTree
from linkedbinarytree import LinkedBinaryTree
from BST import BinarySearchTree



# nums = [range(16)]
# #bst = BSTNode()
# #lbt = LinkedBinaryTree()
# #for num in nums:
#     #bst.insert(num)

lbt = BinarySearchTree()
bst_test = BinarySearchTree()

#Load BST with elements from previous binarytree
#bst_test.load_bst(0, len(self._our_ordered_array))

lbt._add_root(15)
lbt._add_left(lbt.root(), 14)
lbt._add_right(lbt.root(), 13)

l = lbt.left(lbt.root())
r = lbt.right(lbt.root())

lbt._add_left(l, 17)
lbt._add_right(l, 16)
lbt._add_left(r, 11)
lbt._add_right(r, 12)

print("The preoder is:", list(lbt.preorder_print(lbt.root(),"")))
print("the ordered list is:", lbt.convert_BTnodes_list())
lbt.load_bst(0,len(lbt._our_ordered_array))

print(lbt.root())

#print(lbt._make_position(lbt._root))


#print(len(lbt))
#print(lbt.height(lbt.root()))

'''
If you want to get the elements of the tree, you need to traverse it.
In this script, you can choose three kind of ordenation: preorder, inorder or postorder.
Where:
- preorder: gets the elements of the node at position p, its left child and its right child.
- inorder: gets the elements of the left child of the node at position p, the node at position p and its right child.
- postorder: gets the elements of the left child of the node at position p, its right child and the node at position p.
'''
# For the preorder from the root, please run the code below.
# If you want to start from another position, just replace the argument "lbt.root()" for the position of the respective node.
# tree_string = lbt.preorder_print(lbt.root(),"")
# array_number = [char for char in tree_string if char.isdigit()]  # Extract only the digit(s)
# list_numbers = list(map(int, sorted(array_number, reverse = False)))

#print(lbt.get_median_node(1,3))


#p = lbt.preorder_print(lbt.root(),"")



# For the inorder from the root, please run the code below.
# If you want to start from another position, just replace the argument "lbt.root()" for the position of the respective node.
#print("The inorder is:", lbt.inorder_print(lbt.root(),""))

# For the postorder from the root, please run the code below.
# If you want to start from another position, just replace the argument "lbt.root()" for the position of the respective node.
#print("The postorder is:", lbt.postorder_print(lbt.root(),""))

