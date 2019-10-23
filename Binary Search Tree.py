###################################################
### 1.1 - Implementation of Stack Using Array-based List ###
##################################################

class Stack:

    def __init__(self):
        self.stack = []


    def isEmpty(self):
    # DESCRIPTION:
    # -------------------
    #   Checks whether the current stack has any elements. Returns true when stack is empty.

    # PARAMETERS:
    # -------------------

        if len(self.stack) == 0: #check if the length of the stack is zero. Return true if so and false otherwise
            return True
        else:
            return False


    def push(self, x):
    # DESCRIPTION:
    # -------------------
    #    Takes a data item as input and adds it to the top of the current stack

    # PARAMETERS:
    # -------------------
    #   x (int): Value to be pushed to the top of the stack

        self.stack.append(x)


    def pop(self):
    # DESCRIPTION:
    # -------------------
    #   Returns the data item on the top of the current stack and removes it

    # PARAMETERS:
    # -------------------

        # Check if the stack is empty, and return an error if so
        if len(self.stack) <= 0:
            return ("Error: cannot pop from empty stack")
        # Otherwise, remove the element at the top of the stuack and remove it from the stack
        else:
            temp = self.stack[-1]
            del self.stack[-1]
            return temp


    def top(self):
    # DESCRIPTION:
    # -------------------
    #   Returns the element at the top of the current stack without removing it

    # PARAMETERS:
    # -------------------

        return self.stack[-1]


    def size(self):
    # DESCRIPTION:
    # -------------------
    #   Returns the size of the current stack

    # PARAMETERS:
    # -------------------

        return len(self.stack)


############################################
### 1.2 - Implementation of a Binary Search Tree ###
############################################

class BinarySearchTree:
    def __init__(self):
        self.value = None
        self.leftChild = None
        self.rightChild = None
        self.depth = 1

    def insert(self, newNode):
    # DESCRIPTION:
    # -------------------
    #   Insert a new node containing an integer into the tree

    # PARAMETERS:
    # -------------------
    #   newNode: Integer to be inserted into the binary search tree

        # Base case (node is a leaf): create new node with parameter value
        if self.value == None:
            self.value = newNode
        else:
            # When the current node's value is greater than the input, move on to the left subtree
            if self.value > newNode:
                # Create new node with input value if left child is a leaf
                if self.leftChild == None:
                    temp = BinarySearchTree()
                    temp.value = newNode
                    self.leftChild = temp
                # Recursive case for left subtree
                else:
                    (self.leftChild).insert(newNode)
            # When the current node's value is less than the input, move on to the right subtree
            else:
                # Create new node with input value if right child is a leaf
                if self.rightChild == None:
                    temp = BinarySearchTree()
                    temp.value = newNode
                    self.rightChild = temp
                # Recursive case for right subtree
                else:
                    (self.rightChild).insert(newNode)


    def searchPath(self, target):
    # DESCRIPTION:
    # -------------------
    #   Return a list of all values in the nodes on the search path to a particular node (input)

    # PARAMETERS:
    # -------------------
    #   target (int): The node value being searched for

        return self.searchPathHelper(target, [])


    def searchPathHelper(self, target, path):
    # DESCRIPTION:
    # -------------------
    #   Helper function for searchPath that keeps track of the path in a stack

    # PARAMETERS:
    # -------------------
    #    target (int): The node value being searched for
    #    path ([int]): The tail recursion parameter keeping track of the current state of the search path

        # Base case: value is found. Add target to search path list and return it.
        if self.value == target:
            path.append(self.value)
            return path
        # When a node is reached where each child is a leaf and the target is not found, return unsuccessful
        if (self.leftChild == None) and (self.rightChild == None) and (not(self.value == target)):
            print("error: the target is not in the tree")
            return
        # When the current node is greater than target, append current node value to path list and recurse over left subtree
        if self.value > target:
            path.append(self.value)
            (self.leftChild).searchPathHelper(target, path)
        # When the current node is less than target, append current node value to path list and recurse over right subtree
        if self.value < target:
            path.append(self.value)
            (self.rightChild).searchPathHelper(target, path)
        return path


    def getTotalDepth(self):
    # DESCRIPTION:
    # -------------------
    #   Computes the sum of the depths of all nodes in the tree

    # PARAMETERS:
    # -------------------

        return self.getTotalDepthHelper(0)


    def getTotalDepthHelper(self, depth):
    # DESCRIPTION:
    # -------------------
    #   Helper function for total depth which keeps track of the current depth using tail recursion

    # PARAMETERS:
    # -------------------
    #   depth (int): Tail recursion parameter which keeps track of the total depth

        # Return zero when leaf is reached or binary tree has no nodes
        if self.value == None:
            return 0
        leftDepth = 0
        rightDepth = 0
        # When left subtree is not a leaf, recurse over the left subtree increasing the total depth by 1
        if not(self.leftChild == None):
            leftDepth = (self.leftChild).getTotalDepthHelper(depth+1)
        # When right subtree is not a leaf, recurse over the right subtree increasing the total depth by 1
        if not(self.rightChild == None):
            rightDepth = (self.rightChild).getTotalDepthHelper(depth+1)
        # Return total depth of all subtrees
        return depth +  leftDepth + rightDepth


    def getWeightBalanceFactor(self):
    # DESCRIPTION:
    # -------------------
    #   Returns the maximum absolute value of the size of the left subtree - the size of the right subtree for the whole tree

    # PARAMETERS:
    # -------------------

        current = None
        return self.getWeightBalanceFactorHelper(current)


    def getWeightBalanceFactorHelper(self, current):
    # DESCRIPTION:
    # -------------------
    #   Helper function which recurses over the tree, keeping track of the current maximum weight balance factor

    # PARAMETERS:
    # -------------------
    #   current (int): Tail recursion parameter keeping track of maximum weight balance factor

        # Return zero when leaf is reached or binary tree has no nodes
        if self.value == None:
            return 0
        leftSize = 0
        rightSize = 0
        # When left subtree is not a leaf, note its size and recurse over it
        if not(self.leftChild == None):
            leftSize = self.leftChild.getSubtreeSize()
            self.leftChild.getWeightBalanceFactorHelper(current)
        # When right subtree is not a leaf, note its size and recurse over it
        if not(self.rightChild == None):
            rightSize = self.rightChild.getSubtreeSize()
            self.rightChild.getWeightBalanceFactorHelper(current)
        # Calculate the absolute value of the difference of the sizes of each subtree
        temp = abs(leftSize - rightSize)
        # If there is no existing maximum weight balance factor, set it to the current one
        if current == None:
            current = temp
        else:
            # Update the current largest weight balance factor if necessary
            if (temp > current):
                current = temp
        return current


    def getSubtreeSize(self):
    # DESCRIPTION:
    # -------------------
    #   Helper function which returns the total number of nodes in a particular subtree

    # PARAMETERS:
    # -------------------

        # Return zero when leaf is reached or binary tree has no nodes
        if self.value == None:
            return 0
        else:
            leftSize = 0
            rightSize = 0
            # If the left child is not a leaf, recurse over it
            if not(self.leftChild == None):
                leftSize = self.leftChild.getSubtreeSize()
            # If the right child is not a leaf, recurse over it
            if not(self.rightChild == None):
                rightSize = self.rightChild.getSubtreeSize()
            # Iterate total subtree size
            return 1 + leftSize + rightSize


############################################################
### 1.3 - Reconstruct a Binary Search Tree From a File Using a Stack ###
###########################################################

    def loadTreeFromFile(self, fileName):
    # DESCRIPTION:
    # -------------------
    #   Reads a binary search tree information from a file and reconstructs it

    # PARAMETERS:
    # -------------------
    #   fileName (String): filename containing the nodes of a binary search tree in post-order sequence

        # Create empty stack to keep track of tree
        treeStack = Stack()

        #Open file from parameter directory for reading, and save each line as elements of a list
        file = open(fileName, 'r')
        lis = file.readlines()
        file.close()

        leftTree = None
        rightTree = None
        # Iterate through each line of the file
        for line in lis:
            # Convert line to a list of int characters
            line = line.split()
            rightTree = None
            leftTree = None
            # If the second tag is 1, pop an element from the stack and call it rightTree
            if int(line[2]) == 1:
                rightTree = treeStack.pop()
            # If the first tag is 1, pop an element from the stack and call it leftTree
            if int(line[1]) == 1:
                leftTree = treeStack.pop()

            # Create a new binary search tree with the current data value as the root
            newTree = BinarySearchTree()
            newTree.value = int(line[0])
            # If leftTree exists, set it as the left child of the new tree root
            if not(leftTree == None):
                newTree.leftChild = leftTree
            # If rightTree exists, set it as the right child of the new tree root
            if not(rightTree == None):
                newTree.rightChild = rightTree
            # Push the new tree onto the stack
            treeStack.push(newTree)
        # Set the tree to the finished tree read from the file, and return it
        self = treeStack.top()
        return treeStack.top()


###################
### 1.4 - Test Code ###
###################

def testCode():
# DESCRIPTION:
# -------------------
#   Executes 7 steps test code specified in section 1.4

# PARAMETERS:
# -------------------

    # Get current python file directory and read binary tree from file information
    import os
    directory = os.getcwd() + "\\file.txt"
    print("Reconstructing binary search tree T from file...")
    t = BinarySearchTree()
    # 1) Reconstruct a binary search tree T
    # IMPORTANT FOR TA MARKING: If the directory does not work, please change the parameter below
    t = t.loadTreeFromFile(directory)
    # 2) Calculate the total depth of T
    print("The total depth of T: " + str(t.getTotalDepth()))
    # 3) Calculate the Weight Balance Factor of T
    print("The Weight Balance Factor of T: " + str(t.getWeightBalanceFactor()))
    # 4) Insert a new value (5) into T
    print("Inserting the value 5 into T...")
    t.insert(5)
    # 5) Print path of searching the value 5
    print("The search path for the value 5 in T: " + str(t.searchPath(5)))
    # 6) Calculate the total depth of T
    print("The total depth of T: " + str(t.getTotalDepth()))
    # 7) Calculate the Weight Balance Factor of T
    print("The Weight Balance Factor of T: " + str(t.getWeightBalanceFactor()))

# Call test code
testCode()
# Output should be...

# Reconstructing binary search tree T from file...
# The total depth of T: 8
# The Weight Balance Factor of T: 1
# Inserting the value 5 into T...
# The search path for the value 5 in T: [8, 4, 7, 5]
# The total depth of T: 11
# The Weight Balance Factor of T: 2
