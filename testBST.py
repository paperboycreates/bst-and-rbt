# ==================================================================== #
# File Name: testBST.py
# Authors: Jacob Sheets & Jake Allinson
# Date Created: 20 Sept 2019
# Version: 1.0.1

# Copyright: Copyright 2019
# Course: CS3410 Cedarville University

# Description: Binary Search Tree Main Test
# ==================================================================== #

from bst import BST
from node import Node
import random

# scramble function
def scrambled(orig):
    dest = orig[:]
    random.shuffle(dest)
    return dest

newTree = BST()

# Test with Abitrary Keys
def test1():
    letters = ['b','h','y','f','e','v','b','i','j','a','w','q','z','o','p','l']

    # Adds to Tree
    for i in letters:
            newTree.insert(i)

    # Prints And Checks Tree was built correct
    newTree.printTree(newTree.root, 0)
    newTree.checkTree(newTree.root)
    print("built")

    b = scrambled(letters)
    # Deletes a Section of scrambled 
    for i in b[0:8]:
        newTree.delete(i)

    # Prints And Checks Tree was built correct
    newTree.printTree(newTree.root, 0)
    newTree.checkTree(newTree.root)
    print("done")

# Test 10000 Node Build and 5000 random nodes
def test2():
    # Build Tree
    n = 10000
    used = []
    # Adds Rands
    while (len(used) < n + 1):
        rand = random.randint(0, n)
        if rand not in used:
            newTree.insert(rand)
            used.append(rand)

    # Prints And Checks Tree was built correct
    newTree.printTree(newTree.root, 0)
    newTree.checkTree(newTree.root)

    print(used)

    # Deletes a n/2 size scrambled list of nodes
    i = 0
    b = scrambled(used)
    for i in range(0, int(n/2)):
        print("removing: " + str(b[i]))
        deleteValue = b[i]
        newTree.delete(deleteValue)

    # Check to make sure new tree is correct
    newTree.printTree(newTree.root, 0)
    newTree.checkTree(newTree.root)
    print("done")

# main function
#test1()
#test2()


def test3():
    letters = [3,6,2,4,1,7,5]

    # Adds to Tree
    for i in letters:
            newTree.insert(i)

    # Prints And Checks Tree was built correct
    newTree.printTree(newTree.root, 0)
    newTree.checkTree(newTree.root)
    print("built")


#    b = scrambled(letters)
    # Deletes a Section of scrambled 
 #   for i in b[0:8]:
  #      newTree.delete(i)

    # Prints And Checks Tree was built correct
    newTree.printTree(newTree.root, 0)
    newTree.checkTree(newTree.root)
    print("done")

test3()