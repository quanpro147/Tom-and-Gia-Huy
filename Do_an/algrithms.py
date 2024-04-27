import random
##### GENERATE MAZE ALGRITHM
def depth_first_recursive_backtracker(maze, start_coor):
    row_cur, col_cur = start_coor             # Where to start generating
    path = [(row_cur, col_cur)]               # To track path of solution
    maze.grid[row_cur][col_cur].is_visited = True     # Set initial cell to visited
    visit_counter = 1                       # To count number of visited cells
    visited_cells = list()                  # Stack of visited cells for backtracking

    # print("\nGenerating the maze with depth-first search...")
    # time_start = time.time()

    while visit_counter < maze.grid_size:     # While there are unvisited cells
        neighbour_indices = maze.find_neighbours(row_cur, col_cur)    # Find neighbour indicies
        neighbour_indices = maze.validate_neighbours_generate(neighbour_indices)

        if neighbour_indices is not None:   # If there are unvisited neighbour cells
            visited_cells.append((row_cur, col_cur))              # Add current cell to stack
            row_next, col_next = random.choice(neighbour_indices)     # Choose random neighbour
            maze.grid[row_cur][col_cur].remove_walls(row_next, col_next)   # Remove walls between neighbours
            maze.grid[row_next][col_next].remove_walls(row_cur, col_cur)   # Remove walls between neighbours
            maze.grid[row_next][col_next].visited = True                 # Move to that neighbour
            row_cur = row_next
            col_cur = col_next
            path.append((row_cur, col_cur))   # Add coordinates to part of generation path
            visit_counter += 1

        elif len(visited_cells) > 0:  # If there are no unvisited neighbour cells
            row_cur, col_cur = visited_cells.pop()      # Pop previous visited cell (backtracking)
            path.append((row_cur, col_cur))   # Add coordinates to part of generation path

        # print("Number of moves performed: {}".format(len(path)))
        # print("Execution time for algorithm: {:.4f}".format(time.time() - time_start))

    maze.grid[maze.start[0]][maze.start[1]].set_entry_exit("entry", maze.num_rows-1, maze.num_cols-1)
    maze.grid[maze.end[0]][maze.end[1]].set_entry_exit("exit", maze.num_rows-1, maze.num_cols-1)

    for i in range(maze.num_rows):
        for j in range(maze.num_cols):
            maze.grid[i][j].is_visited = False      # Set all cells to unvisited before returning grid
    maze.generation_path = path   

##### SOLVE MAZE ALGRITHMS
#class solver():
