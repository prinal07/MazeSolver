import time
from queue import PriorityQueue
from maze import Maze, printPath, printPathInMaze



# Define a class to represent nodes in the search space
class Node:
    def __init__(self, row, col, gScore=float('inf'), hScore=float('inf'), parent=None):
        #Row and col index of the node in the maze
        self.row = row 
        self.col = col 
        # The cost to reach this node from the start node
        self.gScore = gScore
        # The estimated cost to reach the goal node from this node
        self.hScore = hScore
        # The parent node in the search path
        self.parent = parent  

    def f_score(self):
        # The total estimated cost to reach the goal node through this node
        return self.gScore + self.hScore

    def __lt__(self, other):
        # Compare nodes by their f-score for use in the priority queue
        return self.f_score() < other.f_score()

# Define the heuristic function for estimating the cost to reach the goal node from a given node
def heuristic(node, goalNode):
    return abs(node[0] - goalNode[0]) + abs(node[1] - goalNode[1])


def AStarSearch(maze):
    # Create the start and goal nodes
    start = Node(maze.startRow, maze.startCol, gScore=0, hScore=heuristic((maze.startRow, maze.startCol), (maze.goalRow, maze.goalCol)))
    goal = Node(maze.goalRow, maze.goalCol)

    # Create the priority queue and add the start node
    queue = PriorityQueue()
    queue.put((start.f_score(),  start))

    # Loop until the queue is empty or the goal node is found
    while not queue.empty():
        # Get the node with the lowest f-score from the priority queue
        (fScore, currentNode) = queue.get()

        # Check if the goal node has been reached
        if (currentNode.row, currentNode.col) == (maze.goalRow, maze.goalCol):
            # Construct the path by backtracking from the goal node to the start node
            path = []
            while currentNode is not None:
                path.append((currentNode.row, currentNode.col))
                currentNode = currentNode.parent
            return path[::-1], maze.visited

        # Mark the current node as visited
        maze.visited.add((currentNode.row, currentNode.col))

        # Check the neighbors/four directions of the current node
        for r, c in [(currentNode.row-1, currentNode.col),  
                     (currentNode.row, currentNode.col-1),
                     (currentNode.row+1, currentNode.col), 
                     (currentNode.row, currentNode.col+1)]:
            # Check if the neighbor is a valid path node
            if (0 <= r < len(maze.maze)) and (0 <= c < len(maze.maze[0])) and (maze.maze[r][c] == Maze.PATH) and ((r, c) not in maze.visited):
                # Create a neighbor node and add it to the queue
                neighborNode = Node(r, c, gScore=currentNode.gScore+1, hScore=heuristic((r, c), (maze.goalRow, maze.goalCol)), parent=currentNode)
                queue.put((neighborNode.f_score(), neighborNode))

    # If the queue is empty and the goal node was not found, return None
    return None

mazeInput = input("Enter maze: ")
maze = Maze(mazeInput)
startTime = time.perf_counter()
path, visited = AStarSearch(maze)
endTime = time.perf_counter()
execTime = endTime - startTime

print("Nodes visited: ", len(visited))
print("Steps in the resulting path: ", len(path) - 1)
print("Execution time: ", execTime, "seconds")
print("Total Path Nodes that can be visited: ", maze.pathNodes)
percentVisited = (len(visited)/maze.pathNodes ) * 100
print("Percent visited: ", percentVisited, "%")

printPath(path, mazeInput, "AStar")
printPathInMaze(maze, path, mazeInput, "AStar")




