# ==================================================================== #
# File Name: node.py
# Authors: Jacob Sheets & Jake Allinson
# Date Created: 20 Sept 2019
# Version: 1.0.1

# Copyright: Copyright 2019
# Course: CS3410 Cedarville University

# Description: Node Class for BST & RBT
# ==================================================================== #

class Node:

    # each node has an element, parent, right child, and left child
    def __init__(self, k):
        self.key = k
        self.parent = None
        self.right = None
        self.left = None
        self.color = None


    # methods to check/update color status
    def setRed(self):
        self.color = "R"

    def isRed(self):
        return (self.color == "R")

    def setBlack(self):
        self.color = "B"

    def isBlack(self):
        return (self.color == "B")

    # getters to check relationships

    def hasParent(self):
        return (self.parent != None)

    def hasLChild(self):
        return (self.left != None)

    def hasRChild(self):
        return (self.left != None)

    def isLChild(self):
        if (self.hasParent):
            if (self.parent.left == self):
                return True
        return False

    def isRChild(self):
        if (self.hasParent):
            if (self.parent.right == self):
                return True
        return False

    def hasSibling(self):
        if (self.hasParent):
            return (self.parent.right != None and self.parent.left != None)
        return False

    def hasRUncle(self):
        if (self.hasParent):
            if (self.parent.hasSibling):
                if (self.parent.isLChild):
                    # parent is l child, so uncle is r child
                    return (self.parent.parent.right.isRed)
                else:
                    # parent is r child, so uncle is l child
                    return (self.parent.parent.left.isRed)
        return False

    # setters for updating relationships
