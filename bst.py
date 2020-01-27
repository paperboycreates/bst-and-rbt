# ==================================================================== #
# File Name: bst.py
# Authors: Jacob Sheets & Jake Allinson
# Date Created: 20 Sept 2019
# Version: 1.0.1

# Copyright: Copyright 2019
# Course: CS3410 Cedarville University

# Description: Binary Search Tree 
# ==================================================================== #

from node import Node

class BST:
    def __init__(self):
        self.nil = Node(None)
        self.root = self.nil

    # Tree Search takes in start node and key to search for
    def search(self, x, k):
        while (x != self.nil and k != x.key):
            if (k < x.key):
                x = x.left
            else: 
                x = x.right
        return x
    
    # Finds Smallest Key
    def minumum(self, x):
        while (x.left != self.nil):
            x = x.left
        return x
    
    # Finds Largest Key
    def maximum(self, x):
        while (x.right != self.nil):
            x = x.right
        return x
    
    # Fins Successor
    def successor(self, x):
        if (x.right != self.nil):
            return self.minumum(x.right)
        y = x.parent
        while (y != self.nil and x == y.right):
            x = y
            y = y.parent
        return y

    # Finds Predecessor
    def predecessor(self, x):
        if (x.left != self.nil):
            return self.maximum(x.left)
        y = x.parent
        while (y != self.nil and x == y.left):
            x = y
            y = y.parent
        return y

    # Inserts value into tree 
    def insert (self, k):
        z = Node(k)
        y = self.nil
        x = self.root

        # traverse the tree
        while (x != self.nil):
            y = x
            if (z.key < x.key):
                x = x.left
            else:
                x = x.right
        z.parent = y

        # tree is empty
        if (y == self.nil):
            self.root = z 
        elif (z.key < y.key):
            y.left = z
        else:
            y.right = z
        # set left and right children to the nil node
        z.left = self.nil
        z.right = self.nil

    # Transplant replaces subtree rooted at node u
    # with subtree rooted at node v, node u's parent
    # becomes node v's parent, and u's parent ends up having 
    # v as its appropaite child
    def transplant(self, u, v):
        if (u.parent == self.nil):
            self.root = v
        elif (u == u.parent.left):
            u.parent.left = v
        else: 
            u.parent.right = v
        if (v != self.nil):
            v.parent = u.parent

    # Delete find node with value 
    # executes with the four cases
    def delete(self, zvalue):
        z = self.search(self.root, zvalue)
        # No Left Children
        if (z.left == self.nil):
            self.transplant(z, z.right)
        # No Right Children
        elif (z.right == self.nil):
            self.transplant(z, z.left)
        # Has Children
        else: 
            y = self.minumum(z.right)
            if (y.parent != z):
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y

    # Prints Tree
    def printTree(self, node, indent):
        if (node == self.nil):
            return
        s = ""
        for i in range(indent):
            s += " "
        print(s + str(node.key))
        indent += 2

        # recursively call print tree
        self.printTree(node.right, indent)
        self.printTree(node.left, indent)
   
   # Checks to see if all nodes have correct children/parents
    def checkTree(self, node):
        if (self.root == self.nil):
            return "empty tree"

        if (node == self.nil):
            return
        if (node.left != self.nil):
            if (node.left.parent != node):
                print("ERROR: child-parent issue")
                print("node: " + str(node.key))
                return
            self.checkTree(node.left)
        if (node.right != self.nil):
            if (node.right.parent != node):
                print("ERROR: child-parent issue")
                print("node: " + str(node.key))
                return
            self.checkTree(node.right)
