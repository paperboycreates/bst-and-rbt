# ==================================================================== #
# File Name: rbt.py
# Authors: Jacob Sheets & Jake Allinson
# Date Created: 20 Sept 2019
# Version: 1.0.1

# Copyright: Copyright 2019
# Course: CS3410 Cedarville University

# Description: Red Black Tree
# ==================================================================== #

from node import Node
class RBT:
    # constructor
    def __init__(self):
        # set nil node
        self.nil = Node(None)
        self.nil.setBlack()
        # set root to the nil node
        self.root = self.nil

    # insert node z into BST by traversing
    def insert(self, z):
        y = self.nil
        x = self.root
        # traverse tree until at a leaf
        while (x != self.nil):
            # set y to x's parent
            y = x
            if (z.key < x.key):
                x = x.left
            else:
                x = x.right
        z.parent = y
        if (y == self.nil):
            self.root = z
        elif (z.key < y.key):
            y.left = z
        else:
            y.right = z
        
        # attach pointers
        z.left = self.nil
        z.right = self.nil
        z.setRed()
        self.insertFixup(z)


    # method fixes the RBT to ensure the 5 properties
    def insertFixup(self, z):
        while (z.parent.isRed()):
            # z's parent is a left child
            if (z.parent.isLChild()):
                # set y to be z's uncle (right of gparent)
                y = z.parent.parent.right
                if (y.isRed()):
                    # CASE 1
                    z.parent.setBlack()
                    y.setBlack()
                    z.parent.parent.setRed()
                    # set z to gparent
                    z = z.parent.parent
                else:
                    if (z.isRChild()):
                        # CASE 2
                        z = z.parent 
                        self.leftRotate(z)
                    # CASE 3
                    z.parent.setBlack()
                    z.parent.parent.setRed()
                    self.rightRotate(z.parent.parent)
            # z's parent is a right child
            else:
                # set y to be z's uncle (left of gparent)
                y = z.parent.parent.left 
                if (y.isRed()):
                    # CASE 1
                    z.parent.setBlack()
                    y.setBlack()
                    z.parent.parent.setRed()
                    # set z to gparent
                    z = z.parent.parent
                else:
                    if (z.isLChild()):
                        # CASE 2
                        z = z.parent
                        self.rightRotate(z)
                    # CASE 3
                    z.parent.setBlack()
                    z.parent.parent.setRed()
                    self.leftRotate(z.parent.parent)
        self.root.setBlack()


    # method performs a left rotate on x moving y (x's right subtree)
    def leftRotate(self, x):
        # set y as x's r child
        y = x.right
        # set y's left subtree as x's right subtree
        x.right = y.left 
        if (y.left != self.nil):
            y.left.parent = x
        # link x's parent to y
        y.parent = x.parent 
        if (x.parent == self.nil):
            self.root = y
        elif (x.isLChild()):
            x.parent.left = y
        else:
            x.parent.right = y
        # make x y's left child
        y.left = x
        x.parent = y


    # method performs a right rotate on y moving x (y's left subtree)
    def rightRotate(self, y):
        # set x as y's l child
        x = y.left
        # set x's right subtree as y's left subtree
        y.left = x.right
        if (x.right != self.nil):
            x.right.parent = y 
        # link y's parent to x
        x.parent = y.parent
        if (y.parent == self.nil):
            self.root = x
        elif (y.isRChild()):
            y.parent.right = x
        else:
            y.parent.left = x
        # make y x's right child
        x.right = y
        y.parent = x


    # recursive method to print each node of the RBT
    def printTree(self, x, indent):
        if (x == self.nil):
            return
        space = ""
        for i in range(indent):
            space += " "
        print(space + str(x.key) + ":" + x.color)
        indent += 4

        # recursively call print tree
        self.printTree(x.right, indent)
        self.printTree(x.left, indent)


    # method checks the 5 properties of the BST
    def checkTreeProperties(self, x):
        if (x.color == None):
            print("BROKEN 1: a node is neither red nor black")
        if (not self.root.isBlack()):
            print("BROKEN 2: tree is not black")
        if (x.isRed()):
            if (x.left and not x.left.isBlack()):
                print("BROKEN 4: a red node has a red child")
            if (x.right and not x.right.isBlack()):
                print("BROKEN 4: a red node has a red child")


    # recursive method to check each node's pointers to children
    def checkTreePointers(self, x):
        # hit leaf
        if (x == self.nil):
            return
        # check l and r children
        if (x.left != self.nil):
            if (x.left.parent != x):
                print("ERROR: child-parent issue")
                print("node: " + str(x.v))
                return
            self.checkTreePointers(x.left)
        if (x.right != self.nil):
            if (x.right.parent != x):
                print("ERROR: child-parent issue")
                print("node: " + str(x.v))
                return
            self.checkTreePointers(x.right)

    # Transplant replaces subtree rooted at node u
    # with subtree rooted at node v, node u's parent
    # becomes node v's parent, and u's parent ends up having 
    # v as its appropaite child
    def transplant(self, u, v):
        if (u.parent == self.nil):
            self.root = v
        elif (u.isLChild()):
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
    
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
        if (x.left != None):
            return self.maximum(x.left)
        y = x.parent
        while (y != self.nil and x == y.left):
            x = y
            y = y.parent
        return y

    def delete(self, k):
        # Find node z
        z = self.search(self.root, k)
        y = z
        yColor = y.color
        # if Left Child is nill node
        if (z.left == self.nil):
            x = z.right
            self.transplant(z, z.right)
        # if right child is nill node
        elif (z.right == self.nil):
            x = z.left
            self.transplant(z, z.left)
        # if has children 
        else: 
            y = self.minumum(z.right)
            yColor = y.color
            x = y.right
            if (y.parent == z):
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        # check to see if violated r-b properties
        if (yColor == "B"):
            self.deleteFixup(x)
    
    def deleteFixup(self, x):
        while (x != self.root and x.isBlack()):
            # x is a left child
            if (x.isLChild()):
                w = x.parent.right
                if (w.isRed()):
                    # CASE 1
                    w.setBlack()
                    x.parent.setRed()
                    self.leftRotate(x.parent)
                    w = x.parent.right
                if (w.left.isBlack() and w.right.isBlack()):
                    # CASE 2
                    w.setRed()
                    x = x.parent
                else:
                    # CASE 3
                    if (w.right.isBlack()):
                        w.left.setBlack()
                        w.setRed()
                        self.rightRotate(w)
                        w = x.parent.right
                    # CASE 4
                    w.color = x.parent.color
                    x.parent.setBlack()
                    w.right.setBlack()
                    self.leftRotate(x.parent)
                    x = self.root
            # x is a right child
            else:
                w = x.parent.left
                if (w.isRed()):
                    # CASE 1
                    w.setBlack()
                    x.parent.setRed()
                    self.rightRotate(x.parent)
                    w = x.parent.left
                if (w.right.isBlack() and w.left.isBlack()):
                    # CASE 2
                    w.setRed()
                    x = x.parent
                else:
                    # CASE 3
                    if (w.left.isBlack()):
                        w.right.setBlack()
                        w.setRed()
                        self.leftRotate(w)
                        w = x.parent.left
                    # CASE 4
                    w.color = x.parent.color
                    x.parent.setBlack()
                    w.left.setBlack()
                    self.rightRotate(x.parent)
                    x = self.root
        x.setBlack()