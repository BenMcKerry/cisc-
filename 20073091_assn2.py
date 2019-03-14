class Stack:
    def __init__(self):             #initializing stack with array to hold contents and var for top item
        self.contents = []
        self.top = None

    def isEmpty(self):
        if len(self.contents) == 0:     #returns true if contents array is empty
            return True
        return False

    def top(self):                  #returns top item
        return self.top

    def size(self):                 #returns num of items in stack contents array
        return len(self.contents)

    def push(self, item):               #appends pushed item to top of stack, updates top var
        self.contents.append(item)
        self.top = item

    def pop(self):
        temp = self.contents[-1]        #temp var holds item to be returned
        del self.contents[-1]
        if self.isEmpty():              #sets top to None if stack is empty
            self.top = None
        else:
            self.top = self.contents[-1]    #else top var is new top item
        return temp                  #returns deleted item

class BinarySearchTree:
    def __init__(self, info = None, lChild = None, rChild = None):  #BST is automatically set to initialize with no info or children unless overwritten
        self.data = info
        self.leftChild = lChild
        self.rightChild = rChild

    def insert(self, data):
        newNode = BinarySearchTree(data)        #new node holds info to be inserted
        if self.data == None:                   #if parent node was initialized without data, give it the inserted data
            self.data = data
        elif newNode.data < self.data:
            if self.leftChild == None:          #if inserted data is less than current node's data and node has no left child:
                self.leftChild = newNode         #new node becomes left child
            else:
                self.leftChild.insert(data)     #if current node has left child, call insert on that child
        elif newNode.data > self.data:
            if self.rightChild == None:         #if inserted data is greater than current node's data and node has no right child:
                self.rightChild = newNode        #new node becomes right child
            else:
                self.rightChild.insert(data)    #if current node has right child, call insert on that child

    def searchPath(self, num, path = []):                   #path is a list that stores the path to the searched for number
        path.append(self.data)                              #appends current node's data to path
        if self.data == num:                                #returns path list when node is found
            return path
        if num < self.data and self.leftChild != None:
            path = self.leftChild.searchPath(num, path)     #if num is less than current node, call searchPath on left child and set this path equal to result
        if num > self.data and self.rightChild != None:
            path = self.rightChild.searchPath(num, path)    #if num is greater than current node, call searchPath on right child and set this path equal to result
        return path                                         #returns path even if node is not found

    def getTotalDepth(self, currentNodeDepth = 0):          #getTotalDepth starts with depth = 0 when called on root node
        sum = 0                                                         #sum is total depth of the tree
        if self.leftChild is None and self.rightChild is None:          #if node is a leaf, return depth of that node
            return currentNodeDepth
        if self.leftChild != None:
            sum += self.leftChild.getTotalDepth(currentNodeDepth+1)     #if current node has a left child, call getTotalDepth on that and increment node depth
        if self.rightChild != None:
            sum += self.rightChild.getTotalDepth(currentNodeDepth+1)    #if current node has a right child, call getTotalDepth on that and increment node depth
        sum += currentNodeDepth
        return sum

    def countNodes(self):  #counts the number of child nodes + node it's called on, helper function for getWeightBalanceFactor()
        if self.data is None:
            return 0
        rChildren = 0                                   #stores the number of right children the node has
        lChildren = 0                                   #stores number of left children node has
        if self.leftChild != None:
            lChildren = self.leftChild.countNodes()     #if current node has left child, call countNodes on that child
        if self.rightChild != None:
            rChildren = self.rightChild.countNodes()    #if current node has right child, call countNodes on that child
        return lChildren+rChildren+1                    #return number of left children + right children + 1 (for current node)

    def getWeightBalanceFactor(self):        #returns highest child imbalance in tree
        lNodes = 0              #keeps track of number of left child nodes
        rNodes = 0              #keeps track of number of right child nodes
        lMax = 0                #keeps track of max imbalance on left side
        rMax = 0                #keeps track of max imbalance on right side
        maximum = 0             #store whichever imbalance is higher (right or left)
        if self.leftChild != None:
            lNodes = self.leftChild.countNodes()                #if left child exists, count number of node on that side
            lMax = self.leftChild.getWeightBalanceFactor()      #also call getWeightBalanceFactor to find imbalance on left side
        if self.rightChild != None:
            rNodes = self.rightChild.countNodes()               #if right child exists, count number of node on that side
            rMax = self.rightChild.getWeightBalanceFactor()     #also call getWeightBalanceFactor to find imbalance on right side
        nodeDif = abs(lNodes - rNodes)                  #stores imbalance of current node
        maximum = max(lMax, rMax)                       #stores whichever side's imbalance is higher
        return max(maximum, nodeDif)                    #returns higher imbalance

    def loadTreeFromFile(self, fileName):               #loads BST from file
        treeStack = Stack()
        file = open(fileName).readlines()               #file is a list of lines in fileName
        for i in range(0,len(file)):                    #for each line in file
            left_tree = None
            right_tree = None
            currentLine = file[i].split()               #currentLine is a list of string representations of the number in current file line, split by spaces
            if currentLine[2] == '1':                   #if 3rd number in file is a 1:
                right_tree = treeStack.pop()                #pop from treeStack, set this to be right_tree
            if currentLine[1] == '1':                   #if 2nd number in file is a 1:
                left_tree = treeStack.pop()                 #pop from treeStack, set this to be left_tree
            newTree = BinarySearchTree(int(currentLine[0]), left_tree, right_tree)      #create new node with data = 1st number in file line, left and right children are set to either nodes popped from stack or None
            treeStack.push(newTree)             #push this node to the stack
        return treeStack.pop()                  #return final fully-formed tree

    def __str__(self):          #helper function which prints string representation of node
        return str(self.data)

def main():
    tree = BinarySearchTree()
    fileTree = tree.loadTreeFromFile("tree.txt")
    print("Depth of tree: ", fileTree.getTotalDepth())
    print("Weight Balance Factor of tree: ", fileTree.getWeightBalanceFactor())
    print("Inserting 5 into tree...")
    fileTree.insert(5)
    print("Search path of 5 in tree: ", fileTree.searchPath(5))
    print("Depth of tree: ", fileTree.getTotalDepth())
    print("Weight Balance Factor of tree: ", fileTree.getWeightBalanceFactor())

main()
