# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:18:23 2023

@author: Hannah
"""

from mlbt import MutableLinkedBinaryTree

lbt = MutableLinkedBinaryTree()

# Test the Initialization
print("Test Initialization", "\n")
print("Initial length:", len(lbt)) # Expected value: 0
print("Root position:", lbt.root(), "\n") # Expected value: None

# Populate tree
lbt.add_root(1)
lbt.add_left(lbt.root(), 2)
lbt.add_right(lbt.root(), 3)

l = lbt.left(lbt.root())
r = lbt.right(lbt.root())

lbt.add_left(l, 4)
lbt.add_right(l, 5)

lbt.add_left(r, 6)
lbt.add_right(r, 7)

# Test population of tree
print("Test tree:", "\n")
print("Length of Tree:", len(lbt)) # Expected value: 7
print("Height of Tree from root:", lbt.height(lbt.root())) # Expected value: 2
print("Number of children of root:", lbt.num_children(lbt.root())) # Expected value: 2
print("Root element:", lbt.root().element()) # Expected value: 1
print("Element of left child of root:", lbt.left(lbt.root()).element()) # Expected value: 2
print("Element of right child of root:", lbt.right(lbt.root()).element()) # Expected value: 3
print("Element of left child of left child of root:", lbt.left(lbt.left(lbt.root())).element(), "\n") # Expected value: 4

# Test traverse methods
print("Test Traverse:", "\n")

print("Preoder:")
preorder = lbt.preorder()
for i in preorder:
    print(i.element(), end=" ")
print("\n")

print("Postorder:")
postorder = lbt.postorder()
for i in postorder:
    print(i.element(), end=" ")
print("\n")

print("In-Order:")
inorder = lbt.inorder()
for i in inorder:
    print(i.element(), end=" ")
print("\n")
