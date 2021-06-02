offsets = {'right': (0, 1),
           'left': (0, -1),
           'up': (-1,    0),
           'down': (1, 0)}


def read_maze(file_name):
    """
    Reads a maze stored a text file and returns a 2d list containing the maze representation
    :param file_name: text file
    :return:2d list
    """
    try:
        with open(file_name) as fh:
            # 2d list
            maze = [[char for char in line.strip('\n')] for line in fh]
            num_cols_top_row = len(maze[0])
            for row in maze:
                if len(row) != num_cols_top_row:
                    print('The maze is not rectangular')
                    raise SystemExit
            return maze
    except OSError:
        print('There is problem with the file you have selected')
        raise SystemExit


def is_legal_pos(maze, pos):
    i, j = pos
    num_rows = len(maze)
    num_columns = len(maze[0])
    return 0 <= i < num_rows and 0 <= j < num_columns and maze[i][j] != '*'


def get_path(predecessors, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()
    return path
