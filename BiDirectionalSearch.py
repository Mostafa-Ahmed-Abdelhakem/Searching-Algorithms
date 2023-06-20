### Basic Bidirectional Search ###

# import needed libraries
import queue

# define the Node class
class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = None
        self.visited_right = False   # whether the node was reached by the BFS that started from source
        self.visited_left = False    # whether the node was reached by the BFS that started from destination
        self.parent_right = None     # used for retrieving the final  path from start to the meeting point
        self.parent_left = None      # used for retrieving the final  path from the meeting point to destination


def extract_path(node):
    """return the path when both PFS'S have met"""
    node_copy = node
    path = []

    while node:
        path.append(node.val)
        node = node.parent_right

    path.reverse()
    del path[-1]  # because the meeting node appears twice

    while node_copy:
        path.append(node_copy.val)
        node_copy = node_copy.parent_left
    return path

# the bidirectional search method
def bidirectional_search(s, t):
    q = queue.Queue()
    q.put(s)
    q.put(t)
    s.visited_right = True
    t.visited_left = True

    while not q.empty():
        n = q.get()

        if n.visited_left and n.visited_right:  # if the node visited by both BFS's
            return extract_path(n)

        for neighbor in n.neighbors:
            if n.visited_left == True and not neighbor.visited_left:
                neighbor.parent_left = n
                neighbor.visited_left = True
                q.put(neighbor)
            if n.visited_right == True and not neighbor.visited_right:
                neighbor.parent_right = n
                neighbor.visited_right = True
                q.put(neighbor)
    return False

# defining nodes
n0 = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

# nodes neighbors
n0.neighbors = [n1, n5]
n1.neighbors = [n0, n1, n6]
n2.neighbors = [n1]
n3.neighbors = [n4, n6]
n4.neighbors = [n3]
n5.neighbors = [n0, n6]
n6.neighbors = [n1,n3, n5, n7]
n7.neighbors = [n6]

# printing result
print(bidirectional_search(n0, n4))


