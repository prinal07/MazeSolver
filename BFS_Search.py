import time
from collections import deque
from maze import Maze, printPath, printPathInMaze


def bfs(maze):
    start = (maze.startRow, maze.startCol)
    goal = (maze.goalRow, maze.goalCol)
    #start timer to calculate execution time
    startTime = time.perf_counter()
    # initialize queue with start node and its parent
    queue = deque([(start, None)])
    # dictionary to store parent nodes
    parentDict = {}
    rows = len(maze.maze)
    cols = len(maze.maze[0])

    while queue:
        # get next node from queue
        (row, col), parent = queue.popleft()

        # skip if node has been visited before
        if (row, col) in maze.visited:
            continue

        # mark node as visited
        maze.visited.add((row, col))

        # save parent node for backtracking later
        parentDict[(row, col)] = parent

        # check if exit node is reached
        if (row, col) == goal:

            # trace back path from goal node to start node
            path = [(row, col)]
            while path[-1] != start:
                path.append(parentDict[path[-1]])
            path.reverse()

             # stop timer and calculate execution time
            endTime = time.perf_counter()
            execTime = endTime - startTime

            # return the path from start to exit node, number of visited nodes, and execution time
            return path, len(maze.visited), execTime
        
        # loop through possible moves/directions
        
        for (moveR, moveC) in ((1, 0), (0, 1), (0, -1), (-1, 0)):

            # calculate the neighbor node
            neighborRow, neighborCol = row + moveR, col + moveC
            if not (rows > neighborRow >= 0 and cols > neighborCol >= 0 and (neighborRow, neighborCol) not in maze.visited and maze.maze[neighborRow][neighborCol] != Maze.WALL):
                continue

            # add the neighbor node and its parent to the queue
            queue.append(((neighborRow, neighborCol), (row, col)))  # add the neighbor node and its parent to the queue

    # return None if goal node is not reachable from the start node
    return "Path not found"


mazeFile = input("Enter filename:")
maze = Maze(mazeFile)

result, nodesVisited, execTime = bfs(maze)
print("Nodes visited: ", nodesVisited)
print("Steps in the resulting path: ", len(result) - 1)
print("Execution time: ", execTime, "seconds")
print("Total Path Nodes that can be visited: ", maze.pathNodes)
percentVisited = (nodesVisited/maze.pathNodes ) * 100
print("Percent visited: ", percentVisited, "%")

printPath(result, mazeFile, "bfs")
printPathInMaze(maze, result, mazeFile, "bfs")



