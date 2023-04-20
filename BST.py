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
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BinarySearchTree(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BinarySearchTree(val)

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    def delete(self, val):
        if self == None:
            return self
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)

        if self.right == None:
            return False
        return self.right.exists(val)

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals


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
            return median # return the position in the ordered array

    def load_bst(self, first_position, last_position):
        for i in self.get_median_node(0, len(self._our_ordered_array)):
            min_i = self._our_ordered_array[0]
            max_i = len(self._our_ordered_array)-1
        first_position = min_i
        last_position = max_i
        first_and_last = min_i + max_i

        if self._
        median_node = self.get_median_node(0, len(self._our_ordered_array))
        self._Node._element = self.insert(self._our_ordered_array[median_node])

        else
            median_node = self.get_median_node(0, len(self._our_ordered_array))
            self.get_median_node(0,len(self._our_ordered_array))

        # Get the median node
        #insert the median node in a new bst_node
        #call again to the left child using: from 1st to median-1 [:]
        # call again to the right child using: from median+1 to the end [:]
