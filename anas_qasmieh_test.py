# Code by: Anas Qasmieh
# Last updated: 2019-04-01

######################################################################
######################################################################

# Question 1
# Function to return a boolean if 2 tuples of lines on x-axis overlap.

def doesOverlap (l1,l2):
    if max(l1)>min(l2) and max(l2)>min(l1):
        return True
    return False

# Collection of test cases
print(doesOverlap( (1,5) , (2,6) ))
print(doesOverlap( (1,5) , (6,8) ))
print(doesOverlap( (5,1) , (8,5) ))
print(doesOverlap( (-1,3) , (4,3) ))
print(doesOverlap( (4,1) , (7,3) ))




######################################################################
######################################################################

# Question 2
# Function to compare software version numbers.

def versionCompare (v1,v2):
    try:
        v1_list = [int(i) for i in v1.split('.')]
        v2_list = [int(i) for i in v2.split('.')]
    except:
        return "Error: at least one input is invalid."
    
    v1_len, v2_len = len(v1_list), len(v2_list)
    if v1_len > v2_len:
        for i in range(v1_len - v2_len):
            v2_list.append(0)
    elif v1_len < v2_len:
        for i in range(v2_len - v1_len):
            v1_list.append(0)
    
    for i in range(len(v1_list)):
        if v1_list[i] > v2_list[i]:
            return f'\"{v1}\" is greater than \"{v2}\"'
        elif v1_list[i] < v2_list[i]:
            return f'\"{v1}\" is less than \"{v2}\"'
        
    return f'\"{v1}\" is equal to \"{v2}\"'

# Collection of test cases:
print(versionCompare('1.0','1.1'))
print(versionCompare('1.0','0.9'))
print(versionCompare('1.5','1.5.1'))
print(versionCompare('1.4','1.3.9'))
print(versionCompare('2.2.0','2.2'))
print(versionCompare('2.2.0','2.2.0.0'))
print(versionCompare('7.8.0.4','7.8.0'))
print(versionCompare('3.5.10','3.5.1'))
print(versionCompare('3.6.9','3.6.0.9'))
print(versionCompare('1.','1.0'))
print(versionCompare('1.0','1.0.0.0.0'))
print(versionCompare('1.1','1.1.0.0.0.1'))
print(versionCompare('1.x','2.x'))
print(versionCompare('1.2.','1.3.'))




######################################################################
######################################################################

# Question 3
# Implementation of an LRU Cache

# Note: The cache expiration feature is not implemented.



# First, define a Node class to represent one LRU Cache element
# Each Node has a pointer to the next and previous nodes in the LRU Cache
# The data takes the form of a dictionary (key + value)
# The key stores the input given to a given function
# The value stores the output corresponding to the given input, to be retrieved if the input is cached

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None



# Define the LRU Cache class using the Node class above
# LRU Cache is implemented as a doubly-linked list of Nodes
# Doubly linked list is used due to its efficiency in insertion and removal of elements at any position, 
# which happens often in an LRU Cache as elements are added, removed, or moved to another position.

class LRU_Cache:
    cache_size = 4 #number of cache elements
    
    def __init__(self, func):
        self.func = func
        self.cache = {}
        self.head = Node(0,0) #Used as placeholder head pointer Node instead of using None
        self.tail = Node(0,0) #Used as placeholder tail pointer Node instead of using None
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def __call__(self, *args, **kwargs):
        # If output is cached, move it to the head of the doubly linked list, then return it
        if args in self.cache:
            self.reorderList(args)
            return f'\nFound in cache: {self.cache[args]}\nCache state: {self.cache}'
        
        # Remove least recently used element from node list if cache limit is reached, 
        # to free up a cache spot for the result to be obtained below
        if len(self.cache) == self.cache_size:
            node = self.head.next
            self._remove(node)
            del self.cache[node.key]
        
        # Now, if the element is not in the cache, get the result and cache it
        result = self.func(*args, **kwargs)
        self.cache[args] = result
        node = Node(args, result)
        self._add(node)
        print(f'Cache updated!\nCache state: {self.cache}')
        return result
    
    # Basic doubly-linked list function to add a node
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
    
    # Basic doubly-linked list function to remove a node
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
    
    # Function to reorder the cache by moving LRU element to the head of the list
    def reorderList(self, args):
        current = self.head
        while True:
            if current.key == args:
                node = current
                self._remove(node)
                self._add(node)
                break
            else:
                current = current.next



# Testing the LRU Cache:
import time

@LRU_Cache
def square(n):
    print(f'\nComputing ({n}^2)')
    time.sleep(1)
    return n*n

# Given a cache of size 4, the cache should contain {1:1, 3:9, 4:16, 5:25} 
# after the following sequence of function calls:
print(square(1))
print(square(2))
print(square(3))
print(square(1))
print(square(4))
print(square(5))

