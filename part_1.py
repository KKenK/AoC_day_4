import input_parser
import copy
from collections import namedtuple
from char_grid_class import CharGrid

Coordinate_Transformation = namedtuple("Coordinates_Transformation", ["x","y"])

class WordSearch(CharGrid):
    
    def __init__(self, word_grid):
        super().__init__(word_grid)

    def count_word_instance(self, target_word):

        target_word_length = len(target_word)

        self._grid_with_borders = self._add_border(target_word_length)

        line_length = len(self._grid_with_borders[0])

        instance_counter = 0

        for y in range(target_word_length - 1 , len(self._grid_with_borders) - (target_word_length - 1)):
            for x in range(target_word_length - 1 , line_length - (target_word_length - 1)):       
                instance_counter += self._scan_adjacent_positions_for_word_instances(target_word, y, x)
  
        return instance_counter
    
    def _scan_adjacent_positions_for_word_instances(self, target_word, starting_y, starting_x):
        
        starting_char = self._grid_with_borders[starting_y][starting_x]

        if not starting_char == target_word[0]:
            return 0
        
        instance_counter = 0 

        for adjacent_position in [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:

            coordinate_transformation = Coordinate_Transformation(x = adjacent_position[0], y = adjacent_position[1])
            
            y = copy.copy(starting_y)
            x = copy.copy(starting_x)

            scanned_sequence = ""

            for i in range(len(target_word) - 1):
                y += coordinate_transformation.y
                x += coordinate_transformation.x
                
                scanned_sequence += self._grid_with_borders[y][x]
            
            scanned_sequence = starting_char + scanned_sequence

            if scanned_sequence == target_word:
                instance_counter += 1

        return instance_counter
        
        
if __name__ == "__main__":

    input_parser = input_parser.InputParser(r"C:\Users\kylek\Documents\code\Advent_of_code\2024\Day_4\input.txt")

    word_search = WordSearch(input_parser.parsed_input)

    print(word_search.count_word_instance("XMAS"))

