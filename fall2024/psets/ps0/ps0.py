#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        """
        :param root: the root of the binary tree
        """
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        """
        :param: the key associated with the vertex of the binary tree
        """
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None


#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    if (v.right==None and v.left==None): # Check if we're dealing with leaves
        v.size = 1

    else:
        if (v.left):
            calculate_sizes(v.left)
        if (v.right):
            calculate_sizes(v.right)

        sum = 1
        if (v.right):
            sum += v.right.size

        if (v.left):
            sum += v.left.size

        v.size = sum

#
# Problem 1c
#

# Input: a positive integer t, 
# ...BTvertex v, the root of a BinaryTree of size n >= 1
# Output: BTvertex, descendent of v such that its size is between 
# ... t and 2t (inclusive)
# Runtime: O(h) 

def FindDescendantOfSize(t, v):
    # Your code goes here
    if (v.size <= 2*t and v.size >= t):
        return v
    
    else:
        if (v.left and v.right):
            if (v.left.size > v.right.size):
                return FindDescendantOfSize(t, v.left)
            else:
                return FindDescendantOfSize(t, v.right)
        elif (v.left):
            return FindDescendantOfSize(t, v.left)
        elif (v.right):
            return FindDescendantOfSize(t, v.right)