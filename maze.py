import os

# Represents a maze that can be loaded from a .txt file. The file should contain '#' as Walls and '-' as Paths that can be travelled.
# Determines the entry and exit points, converting the maze to be represented using 0s and 1s (1s = Walls, 0s = Paths)
# Keeps track of visited nodes cells and resulting path.
class Maze:
    WALL = 1
    PATH = 0

    def __init__(self, filename):
        # Initialize the maze and load it from the given file
        self.maze = []
        self.pathNodes = 0
        newFileName = "Mazes/" + filename
        with open(newFileName) as f:
            # Read all non-empty lines from the file and remove any trailing whitespace
            lines = [line.rstrip() for line in f.readlines() if line.strip()]

            # Determine the number of rows in the maze
            lineCount = len(lines)

            # Determine the entry position of the maze
            firstLine = lines[0].split()
            self.startRow, self.startCol = 0, firstLine.index('-')

            # Determine the exit position of the player
            lastLine = lines[lineCount - 1].split()
            self.goalRow, self.goalCol = lineCount - 1, lastLine.index('-')

            # Convert each line of the maze into a list of integers representing the cells
            # Replacing walls with 1 (Maze.WALL) and paths to travel with 0 (Maze.PATH)
            for line in lines:
                row = []
                for c in line.strip():
                    if c == '#':
                        row.append(Maze.WALL)
                    elif c == '-':
                        row.append(Maze.PATH)
                        self.pathNodes += 1
                self.maze.append(row)

        # Initialize the sets for visited cells and the resulting path
        self.visited = set()

    def __repr__(self):
        # Generate a string representation of the maze for debugging purposes
        s = ''
        for row in self.maze:
            s += ' '.join(str(c) for c in row) + '\n'
        return s


def printPathInMaze(maze, path, mazeFile, search):

    if not os.path.exists("VisualPath"):
        os.makedirs("VisualPath")
    
    outputFileName = "VisualPath/" + search + mazeFile

    with open(outputFileName, "w") as f:

        # loop through the maze rows
        for r, row in enumerate(maze.maze):

            # loop through the maze cells in the row
            for c, cell in enumerate(row):
                if (r, c) in path:

                    # if the cell is on the path, print '=' instead of the cell value
                    f.write('= ')
                else:

                    # otherwise, print the cell value
                    f.write(str(cell) + ' ')

            # write a newline character at the end of the row
            f.write('\n')


def printPath(path, mazeFile, search):

    if not os.path.exists("Paths"):
        os.makedirs("Paths")
    
    outputFileName = "Paths/" + search + mazeFile 

    with open(outputFileName, "w") as f:
        f.write(str(path))



