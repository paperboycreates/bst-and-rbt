# ==================================================================== #
# File Name: testRBT.py
# Authors: Jacob Sheets & Jake Allinson
# Date Created: 20 Sept 2019
# Version: 1.0.1

# Copyright: Copyright 2019
# Course: CS3410 Cedarville University

# Description: Red Black Tree Test Main
# ==================================================================== #

from rbt import RBT
from node import Node
import random

# scramble function
def scrambled(orig):
    dest = orig[:]
    random.shuffle(dest)
    return dest


def test0():
    # test the rotations ON rbt
    # x is root in L -> R, y is root in R -> L
    newTree = RBT()

    x = Node(4)
    y = Node(6)
    newTree.insert(x)
    newTree.insert(Node(3))
    newTree.insert(y)
    newTree.insert(Node(5))
    newTree.insert(Node(7))

    newTree.printTree(newTree.root, 0)
    print("done initial")

    newTree.leftRotate(x)
    newTree.printTree(newTree.root, 0)
    print("done left rotation")

    newTree.rightRotate(y)
    newTree.printTree(newTree.root, 0)
    print("done right rotation")


def test1():
    # put 15 elements on RBT 
    newTree = RBT()
    n = 30
    used = []
    while (len(used) < n + 1):
        rand = random.randint(0, n)
        if rand not in used:
            z = Node(rand)
            newTree.insert(z)
            used.append(rand)

    newTree.checkTreePointers(newTree.root)
    newTree.printTree(newTree.root, 0)
    print("done printing")

def test2():
    # test the cases for the tree from p.317
    newTree = RBT()

    nums    = [11, 2, 14, 1, 7, 15, 5, 8, 4]
    colors  = ["B", "R", "B", "B", "B", "R", "R", "R", "R"]
    for i in nums:
        z = Node(nums[i])
        z.c = colors[i]
        newTree.insert(z)
    
    newTree.printTree(newTree.root, 0)

    newTree.checkTreePointers(newTree.root)
    newTree.checkTreeProperties(newTree.root)
    print("done printing")

def test3():
    newTree = RBT()

    nums = [5, 7, 3, 6, 2, 8, 9, 0, 1, 10, 12, 11, 4]
    for i in nums:
        z = Node(nums[i])
        newTree.insert(z)
    
    newTree.printTree(newTree.root, 0)
    print("done printing")

def test4():
    newTree = RBT()

    # insert into the RBT
    nums = [5, 7, 3, 6, 2, 8, 9, 0, 1, 10, 12, 11, 4]
    for i in nums:
        z = Node(nums[i])
        newTree.insert(z)    
    newTree.printTree(newTree.root, 0)
    print("done inserting")

    # delete from the RBT
    scrambledNums = scrambled(nums)
    for i in scrambledNums:
        newTree.delete(scrambledNums[i])
        print("deleted: " + str(scrambledNums[i]))
    newTree.printTree(newTree.root, 0)
    print("done deleting")

def test5():
    newTree = RBT()

    # insert into the RBT
    n = 10000
    nums = []
    while (len(nums) < n + 1):
        rand = random.randint(0, n)
        if rand not in nums:
            z = Node(rand)
            newTree.insert(z)
            nums.append(rand)   
    newTree.printTree(newTree.root, 0)
    print("done inserting")

    # delete from the RBT
    for i in nums:
        newTree.delete(nums[i])
        print("deleted: " + str(nums[i]))
    newTree.printTree(newTree.root, 0)
    print("done deleting")


# main function
#test0()
#test1()
#test2()
#test3()
#test4()
#test5()



def test10():
    newTree = RBT()

    nums = [3,6,2,4,1,7,5]
    for i in nums:
        z = Node(nums[i])
        newTree.insert(z)
    
    newTree.printTree(newTree.root, 0)
    print("done printing")

test10()