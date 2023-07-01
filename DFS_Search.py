import time
from maze import Maze, printPathInMaze, printPath

def dfs(maze):
    start = (maze.startRow, maze.startCol)
    goal = (maze.goalRow, maze.goalCol)

    # Record the start time for execution time calculation.
    startTime = time.perf_counter()

    # Create a stack with the entry/starting position and an empty path.
    stack = [(start, [])]

    # Loop until there are no more positions in the stack to explore.
    while stack:

        # Pop the top position and path from the stack.
        (row, col), path = stack.pop()

        # If the current position is the end position, return the path, number of nodes visited, steps taken, and execution time.
        if (row, col) == goal:
            path = path + [(row, col)]
            steps =  len(path) - 1
            nodesVisited = len(maze.visited)
            endTime = time.perf_counter()
            execTime = endTime - startTime
            return path, nodesVisited, steps, execTime

        # If the current position has not been visited and is not a wall, mark it as visited and explore its neighbors.
        if (row, col) not in maze.visited and maze.maze[row][col] != Maze.WALL:
            maze.visited.add((row, col))

            # Slower/Less efficient order of exploration (1)
            # For each possible move (right, left, down, up), add it to the stack with the updated path
            # for moveR, moveC in ((0, 1), (0, -1), (1, 0), (-1, 0)):

            # Faster/More efficient order of exploration (2)
            # For each possible move (up, left, right, down), add it to the stack with the updated path
            for moveR, moveC in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                stack.append(((row + moveR, col + moveC), path + [(row, col)]))

            # Should be one of the least efficient order of exploration (3)
            # For each possible move (down, right, up, left), add it to the stack with the updated path
            # for moveR, moveC in ((1, 0), (0, 1), (0, -1), (-1, 0)):
            #     stack.append(((row + moveR, col + moveC), path + [(row, col)]))



    # If the stack is empty and the end point hasn't been reached, return False
    return False

mazefile = input("Enter maze file: ")
maze = Maze(mazefile)
path, nodesVisited, steps, execTime  = dfs(maze)

print("Nodes visited: ", nodesVisited)
print("Steps in the resulting path: ", steps)
print("Execution time: ", execTime, "seconds")
print("Total Path Nodes that can be visited: ", maze.pathNodes)
percentVisited = (nodesVisited/maze.pathNodes ) * 100
print("Percent visited: ", percentVisited, "%")

printPath(path, mazefile, "dfs")
printPathInMaze(maze, path, mazefile, "dfs")


