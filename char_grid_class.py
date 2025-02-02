import copy

class CharGrid():
    
    def __init__(self, word_grid):
        self.grid = word_grid
        self._grid_with_borders = []
    
    def _add_border(self, target_word_length):

        grid_copy = copy.copy(self.grid)

        grid_with_borders = ["." * (target_word_length - 1) + x + "." * (target_word_length - 1) for x in grid_copy]

        line_length = len(grid_with_borders[0])
        
        for i in range(target_word_length - 1):
            grid_with_borders = ["." * line_length] + grid_with_borders + ["." * line_length]

        return grid_with_borders
    