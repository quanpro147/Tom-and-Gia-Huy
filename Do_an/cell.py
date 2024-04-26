
class cell():

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.neibour = []
        self.walls = {'top': True, 'bot': True, 'right': True, 'left': True}
        self.is_visited = False
        self.is_start = False

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
        if self.row - neighbour.row == 1 and self.walls["top"] and neighbour.walls["bottom"]:
            return True
        elif self.row - neighbour.row == -1 and self.walls["bottom"] and neighbour.walls["top"]:
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
            self.walls["bottom"] = False
            return True, ""
        elif self.col - neighbour_col == 1:
            self.walls["left"] = False
            return True, ""
        elif self.col - neighbour_col == -1:
            self.walls["right"] = False
            return True, ""
        return False
    