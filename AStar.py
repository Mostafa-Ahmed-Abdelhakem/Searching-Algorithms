# import required libraries
import queue as Q

def BESTFS(graph, start, end):
    if start not in graph:
        raise TypeError(str(start) + ' not found in graph !')
        return
    if end not in graph:
        raise TabError(str(end) + ' not found i graph !')
        return

    queue = Q.PriorityQueue()
    queue.put((graph[start]['heuristic'], [start]))
    visited = []
    while not queue.empty():
        node = queue.get()
        current = node[1][len(node[1]) - 1]
        
        if end in node[1]:
            print("Path found: " + str(node[1]))
            break

        for neighbor in graph[current]['neighbor']:
            temp = node[1][:]
            temp.append(neighbor)
            queue.put((graph[neighbor]['heuristic'], temp))

# define the AStar algorithm
def AStar(graph, start, end):
    if start not in graph:
        raise TypeError(str(start) + ' not found in graph !')
        return
    if end not in graph:
        raise TabError(str(end) + ' not found i graph !')
        return
    queue = Q.PriorityQueue()
    queue.put((graph[start]['heuristic'], [start]))
    visited = []
    while not queue.empty():
        node = queue.get()
        current = node[1][len(node[1]) - 1]
        if end in node[1]:
            print("Path found: " + str(node[1]))
            break
        for neighbor in graph[current]['neighbor']:
            temp = node[1][:]
            temp.append(neighbor)
            queue.put((graph[neighbor]['heuristic'], temp))

def readGraph():
    lines = int( input() )
    graph = {}
    for line in range(lines):
        line = input()
        tokens = line.split()
        node = tokens[0]
        graph[node] = {}
        graph[node]['heuristic'] = tokens[1]
        graph[node]['neighbor'] = tokens[2:]
    return graph

def main():
    graph = readGraph()
    BESTFS(graph, 'S', 'G')

# main function
if __name__ == "__main__":
    main()

### Sample input ###
# 5
# S 7 B 2 A 1
# A 6 B 2 C 5 G 0
# B 2 C 1 
# C 1 G 3 
# G 0
