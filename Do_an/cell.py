class cell():

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.neibour = []
        self.walls = {'top': True, 'bot': True, 'right': True, 'left': True}
        self.is_visited = False
        self.is_entry_exit = None

    def is_walls_between(self, neighbour):
        """
        Function that checks if there are walls between self and a neighbour cell.
        Returns true if there are walls between. Otherwise returns False.

        Args:
            neighbour The cell to check between

        Return:
            True: If there are walls in between self and neighbor
            False: If there are no walls in between the neighbors and self

        """
        if self.row - neighbour.row == 1 and self.walls["top"] and neighbour.walls["bot"]:
            return True
        elif self.row - neighbour.row == -1 and self.walls["bot"] and neighbour.walls["top"]:
            return True
        elif self.col - neighbour.col == 1 and self.walls["left"] and neighbour.walls["right"]:
            return True
        elif self.col - neighbour.col == -1 and self.walls["right"] and neighbour.walls["left"]:
            return True

        return False
    
    def remove_walls(self, neighbour_row, neighbour_col):
        """
        Function that removes walls between neighbour cell given by indices in grid.

            Args:
                neighbour_row (int):
                neighbour_col (int):

            Return:
                True: If the operation was a success
                False: If the operation failed
                
        """

        if self.row - neighbour_row == 1:
            self.walls["top"] = False
            return True, ""
        elif self.row - neighbour_row == -1:
            self.walls["bot"] = False
            return True, ""
        elif self.col - neighbour_col == 1:
            self.walls["left"] = False
            return True, ""
        elif self.col - neighbour_col == -1:
            self.walls["right"] = False
            return True, ""
        
        return False
    
    def set_entry_exit(self, entry_exit, row_limit, col_limit):
        """
        Function that sets the cell as an entry/exit cell by disabling the outer boundary wall.
        First, we check if the entrance/exit is on the top row. Next, we check if it should
        be on the bottom row. Finally, we check if it is on the left wall or the bottom row.

        Args:
            entry_exit: True to set this cell as an exit/entry. False to remove it as one
            row_limit:
            col_limit:

        """
        if self.row == 0:
            self.walls["top"] = False
        elif self.row == row_limit:
            self.walls["bot"] = False
        elif self.col == 0:
            self.walls["left"] = False
        elif self.col == col_limit:
            self.walls["right"] = False

        self.is_entry_exit = entry_exit