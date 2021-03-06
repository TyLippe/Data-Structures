import sys
sys.path.append('../queue_and_stack')
from dll_stack import Stack
from dll_queue import Queue

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #if greater than or equal to we will move to the right
        if value >= self.value:
            #set the current_node to the node to the right of current_node, recursive
            if self.right:
                self.right.insert(value)
            #if none on right, add it
            else:
                self.right = BinarySearchTree(value)
        #if less than, we will move to the left
        elif value < self.value:
            #set current_node to the left node, recursive
            if self.left:
                self.left.insert(value)
            #if no left node we add it
            else:
                self.left = BinarySearchTree(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #when found return true
        #if no left or right return false
        #if given value is equal to default we return true
        if target == self.value:
            return True
        #if given value is greater than, move to right
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        #if given value is less than, move to left
        else:
            if self.left:
                return self.left.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        #set max_value as .right
        max_value = self.value
        #if no .right than default value is max
        if self.right == None:
            return max_value
        #recursive through tree until no more right
        if self.right:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)

    # Messing with delete
    def delete(self, value):
            if self.contains(value) is True:
	            if value == self.value:
	                if self.left:
	                    left_node = self.left
	                    max_value = left_node.get_max()
	                    self.value = max_value
	                    left_node.delete(max_value)
	                elif self.right:
	                    right_node = self.right
	                    self.value = right_node.value
	                    right_node.delete(right_node.value)
	                else:
	                    return True
	            elif value > self.value:
	                delete = self.right.delete(value)
	                if delete:
	                    self.right = None
	            else:
	                delete = self.left.delete(value)
	                if delete:
	                    self.left = None

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self)
        print(self.value)
        if self.right:
            self.right.in_order_print(self)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        #create a queue
        queue = Queue()
        #add self to queue
        queue.enqueue(self)
        #while loop
        while queue.size is not 0:
            #dequeue head into temp var
            temp = queue.dequeue()
            print(temp.value)
            #if temp.left add to queue
            if temp.left:
                queue.enqueue(temp.left)
            #if temp.right add to queue
            if temp.right:
                queue.enqueue(temp.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        #same as bft but stack
        stack = Stack()
        stack.push(self)
        while stack.size is not 0:
            temp = stack.pop()
            print(temp.value)
            if temp.left:
                stack.push(temp.left)
            if temp.right:
                stack.push(temp.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        print(self.value)
        if self.left:
            self.left.pre_order_dft(self)
        if self.right:
            self.right.pre_order_dft(self)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if self.left:
            self.left.post_order_dft(self)
        if self.right:
            self.right.post_order_dft(self)
        print(self.value)
