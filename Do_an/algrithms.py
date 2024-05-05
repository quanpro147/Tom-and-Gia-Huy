import random
from queue import PriorityQueue, Queue
##### GENERATE MAZE ALGRITHM
def depth_first_recursive_backtracker(maze, start_coor):

    row_cur, col_cur = start_coor             # Where to start generating
    path = [(row_cur, col_cur)]               # To track path of solution
    maze.grid[row_cur][col_cur].is_visited = True     # Set initial cell to visited
    visit_counter = 1                       # To count number of visited cells
    visited_cells = list()                  # Stack of visited cells for backtracking

    while visit_counter < maze.grid_size:     # While there are unvisited cells
        neighbour_list = maze.find_neighbours(row_cur, col_cur)    # Find neighbour indicies
        neighbour_list = maze.validate_neighbours_generate(neighbour_list)

        if neighbour_list is not None:   # If there are unvisited neighbour cells
            visited_cells.append((row_cur, col_cur))              # Add current cell to stack
            row_next, col_next = random.choice(neighbour_list)     # Choose random neighbour
            maze.grid[row_cur][col_cur].remove_walls(row_next, col_next)   # Remove walls between neighbours
            maze.grid[row_next][col_next].remove_walls(row_cur, col_cur)   # Remove walls between neighbours
            maze.grid[row_next][col_next].is_visited = True                 # Move to that neighbour
            row_cur = row_next
            col_cur = col_next
            path.append((row_cur, col_cur))   # Add coordinates to part of generation path
            visit_counter += 1

        elif len(visited_cells) > 0:  # If there are no unvisited neighbour cells
            row_cur, col_cur = visited_cells.pop()      # Pop previous visited cell (backtracking)
            path.append((row_cur, col_cur))   # Add coordinates to part of generation path

    maze.grid[maze.start[0]][maze.start[1]].set_entry_exit("entry", maze.num_rows-1, maze.num_cols-1)
    maze.grid[maze.end[0]][maze.end[1]].set_entry_exit("exit", maze.num_rows-1, maze.num_cols-1)

    for i in range(maze.num_rows):
        for j in range(maze.num_cols):
            maze.grid[i][j].is_visited = False      # Set all cells to unvisited before returning grid
    maze.generation_path = path   
    
    return maze
##### SOLVE MAZE ALGRITHMS
#class solver():

def unblock_neighbours(maze, row_cur, col_cur, neighbours):
        """ Thic function use to find neighbours that can move """
        unblock = []
        if neighbours is None: return None
        for row_next, col_next in neighbours:
            if not maze.grid[row_cur][col_cur].walls['top'] and not maze.grid[row_next][col_next].walls['bot'] and row_cur > row_next:
                unblock.append((row_next, col_next))
            elif not maze.grid[row_cur][col_cur].walls['right'] and not maze.grid[row_next][col_next].walls['left'] and col_cur < col_next:
                unblock.append((row_next, col_next))
            elif not maze.grid[row_cur][col_cur].walls['bot'] and not maze.grid[row_next][col_next].walls['top'] and row_cur < row_next:
                unblock.append((row_next, col_next))
            elif not maze.grid[row_cur][col_cur].walls['left'] and not maze.grid[row_next][col_next].walls['right'] and col_cur > col_next:
                unblock.append((row_next, col_next))

        if len(unblock) > 0: return unblock
        else: return None
        
def bfs(maze):

    start = tuple(maze.start) # lay pos start va end
    end = maze.end
    paths = [[]] # tao duong di co san o start
    paths[0].append(start)
    cur_cell = start
    maze.grid[cur_cell[0]][cur_cell[1]].is_visited = True # cho o start da duoc tham
    Flag = True
    while Flag:
        path = paths[0] # lay path dau tien cua paths
        paths = paths[1:]   # xoa path dau tien
        cur_cell = path[-1] # lay cur_cell la o cuoi cung cua path dang xet
        neighbour_list = maze.find_neighbours(cur_cell[0], cur_cell[1])  # tim tat ca cac o ke ben co the di 
        neighbour_list = maze.validate_neighbours_generate(neighbour_list)
        neighbour_list = unblock_neighbours(maze, cur_cell[0], cur_cell[1], neighbour_list)
        if neighbour_list is not None:
            for neighbour in neighbour_list: # xet tung o trong cac o lien ke
                maze.grid[neighbour[0]][neighbour[1]].is_visited = True # cho cac o duoc xet da dc tham
                add = path.copy() # tao bien phu add de luu duong di dang xet + o ke tiep dang duoc xet
                add.append(neighbour)
                paths.append(add) # them duong di moi vao sau paths
                if neighbour == end: # neu o ke tiep la end thi dung lap
                    Flag = False

    for i in range(maze.num_rows):
        for j in range(maze.num_cols):
            maze.grid[i][j].is_visited = False
    return paths[-1]

def dfs(maze):
    start = maze.start
    end = maze.end
    cur_cell = start            
    path = [cur_cell]              
    maze.grid[cur_cell[0]][cur_cell[1]].is_visited = True     
    visited_cells = []               
    
    while cur_cell != end:     
        neighbour_list = maze.find_neighbours(cur_cell[0], cur_cell[1])    
        neighbour_list = maze.validate_neighbours_generate(neighbour_list)
        neighbour_list = unblock_neighbours(maze, cur_cell[0], cur_cell[1], neighbour_list)

        if neighbour_list is not None:   
            visited_cells.append(cur_cell)             
            next_cell = random.choice(neighbour_list)   
            maze.grid[next_cell[0]][next_cell[1]].is_visited = True     
            cur_cell = next_cell
            path.append(cur_cell)  
        else:  
            cur_cell = visited_cells.pop()    
            path.pop()  
    for i in range(maze.num_rows):
        for j in range(maze.num_cols):
            maze.grid[i][j].is_visited = False 
    return path

def A_star(maze):

    start = maze.start
    end = maze.end

    grid = []
    for i in range(maze.num_rows):
        for j in range(maze.num_cols):
            grid.append((i, j))

    def manhattan_dis(cell1, cell2):
        x1, y1 = cell1
        x2, y2 = cell2
        return abs(x1 - x2) + abs(y1 - y2)
    # check
    g_score = {cell: float('inf') for cell in grid}
    g_score[start] = 0
    f_score = {cell: float('inf') for cell in grid}
    f_score[start] = manhattan_dis(start, end)
    open = PriorityQueue()
    open.put((f_score[start], manhattan_dis(start, end), start))
    path = {}

    while not open.empty():
        cur_cell = open.get()[2]
        if cur_cell == end: break
        for direction in ['top', 'right', 'left', 'bot']:
            if not maze.grid[cur_cell[0]][cur_cell[1]].walls[direction]:
                next_cell = None
                if direction == 'top' and cur_cell[0] != 0:
                    next_cell = (cur_cell[0] - 1, cur_cell[0])
                elif direction == 'right' and cur_cell[1] != maze.num_cols - 1:
                    next_cell = (cur_cell[0], cur_cell[1] + 1)
                elif direction == 'bot' and cur_cell[0] != maze.num_rows - 1:
                    next_cell = (cur_cell[0] + 1, cur_cell[1])
                elif direction == 'left' and cur_cell[1] != 0:
                    next_cell = (cur_cell[0], cur_cell[1] - 1)
                if next_cell is None and cur_cell == start:
                    continue
                g_score_tmp = g_score[cur_cell] + 1
                f_score_tmp = g_score_tmp + manhattan_dis(next_cell, end)

                if f_score_tmp < f_score[next_cell]:
                    g_score[next_cell] = g_score_tmp
                    f_score[next_cell] = f_score_tmp
                    open.put((f_score_tmp, manhattan_dis(next_cell, end), next_cell))
                    path[next_cell] = cur_cell
    
    solution = {}
    cell = end
    while cell != start:
        solution[path[cell]] = cell
        cell = path[cell]
    
    return solution


    


    
    
