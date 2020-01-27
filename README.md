# TreeAlgorithms

*Authors: Jacob Sheets & Jake Allinson*

*Homework 4: CS3410 - Algorithms @ Cedarville University*

### Purpose

Project creates Binary Serach Tree (BST) and Red Black Tree (RBT) classes with nil nodes as leafs for key insertion and deletion.

### Analysis

1. BST
* Time: O(h), where h is the height of the tree
* Height: O(lg(n))

2. RBT
* Time: O(lg(n))
* Height: at most 2lg(n + 1)

RBT builds on the BST and adds the 5 properties making it a balanced binary search tree. BST has the possibility of being a linked-list, so the RBT outperforms with its ability to stay balanced regardless of keys inserted and order given.

### Testing

`testBST.py` and `testRBT.py` are provided for testing the trees. Unit testing is down through the different methods - simply change the methods called in the 2 test files.

`python3 testRBT.py`

**Copyright 2019**