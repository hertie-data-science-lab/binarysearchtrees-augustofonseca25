# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 2023

@author: Augusto Fonseca
"""

from linkedbinarytree import LinkedBinaryTree

class BinarySearchTree(LinkedBinaryTree):
    # def __init__(self, val=None):
    #     #self.left = None
    #     #self.right = None
    #     self.val = val
    #     super().__init__(val)


    def insert(self, val):
        if not self._Node._element:
            self._Node._element = val
            return

        if self._Node._element == val:
            return

        if val < self._Node._element:
            if self._Node._left:
                self._Node._left.insert(val)
                return
            self._Node._left = BinarySearchTree(val)
            return

        if self._Node._right:
            self._Node._right.insert(val)
            return
        self._Node._right = BinarySearchTree(val)

    def exists(self, val):
        if val == self._Node._element:
            return True

        if val < self._Node._element:
            if self._Node._left == None:
                return False
            return self._Node._left.exists(val)

        if self._Node._right == None:
            return False
        return self._Node._right.exists(val)

    # def preorder(self, vals):
    #     if self.val is not None:
    #         vals.append(self.val)
    #     if self.left is not None:
    #         self.left.preorder(vals)
    #     if self._Node._right is not None:
    #         self._Node._right.preorder(vals)
    #     return vals
    #
    # def inorder(self, vals):
    #     if self.left is not None:
    #         self.left.inorder(vals)
    #     if self.val is not None:
    #         vals.append(self.val)
    #     if self.right is not None:
    #         self.right.inorder(vals)
    #     return vals
    #
    # def postorder(self, vals):
    #     if self.left is not None:
    #         self.left.postorder(vals)
    #     if self.right is not None:
    #         self.right.postorder(vals)
    #     if self.val is not None:
    #         vals.append(self.val)
    #     return vals


    '''
    To convert a binary tree in a binary SEARCH tree we need to follow these steps:
    1-) Get your binarytree and traverse it (any order)
    2-) create an array with the elements of binary tree
    3-) Create a method to order the array
    4-) Find median value of the array - use the formula round((len(our_ordered_array)+1)/2)
    5-) Assign this median value to the node
    6-) Call the function recursively to its left child using the parameters: from 1 to parent`s position -1.
    7-) Call the function recursively to its right child using the parameters: from parent`s position +1 to len(our_ordered_array)+1).
    8-) Create a logic to control the end of the array.
    '''



    def convert_BTnodes_list(self):

        tree_string = self.preorder_print(self._make_position(self._root), "") # traverse the old binarytree
        array_number = [char for char in tree_string if char.isdigit()]  # Extract only the digit(s)
        self._our_ordered_array = list(map(int, sorted(array_number, reverse=False)))
        return self._our_ordered_array # return the sorted elements of the old binarytree


    def get_median_node(self, first_position, last_position):
        if first_position != last_position: # Check if it`s NOT the last element in the array
            median = round((first_position + last_position + 1) / 2)
            return median # return the index in the ordered array

    def load_bst(self, first_position, last_position):

        m = self.get_median_node(first_position, last_position)
        self._Node._element = self.insert(self._our_ordered_array[m])

        
        left = [: m-1]
        right = [m+1 : ]

        if first_position < last_position:
            self._Node._left = self.load_bst(first_position, m-1)
            return
            self._Node._right = self.load_bst(m + 1,last_position)
            return



        # Get the median node
        #insert the median node in a new bst_node
        #call again to the left child using: from 1st to median-1 [:]
        # call again to the right child using: from median+1 to the end [:]
