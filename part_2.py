import input_parser
import copy
from collections import namedtuple
from char_grid_class import CharGrid

Coordinate_Transformation = namedtuple("Coordinates_Transformation", ["x","y"])

class PatternSearch(CharGrid):
    
    def __init__(self, word_grid):
        super().__init__(word_grid)

    def count_pattern_instances(self, pattern_perimeter, pattern_checker_function):

        self._grid_with_borders = self._add_border(pattern_perimeter)

        line_length = len(self._grid_with_borders[0])

        instance_counter = 0

        for y in range(pattern_perimeter - 1 , len(self._grid_with_borders) - (pattern_perimeter - 1)):
            for x in range(pattern_perimeter - 1 , line_length - (pattern_perimeter - 1)):       
                instance_counter += pattern_checker_function(self._grid_with_borders, (x , y))
  
        return instance_counter

class Position():
    def __init__(self, char, x, y):
        self.char = char
        self.relative_x = x
        self.relative_y = y

class PatternChecker():
    def __init__(self, pattern_relative_coordinates):
        
        self.pattern_relative_coordinates = pattern_relative_coordinates
        
        self.pattern_permuation_strings = self._generate_pattern_permutations_strings()
 
    def _rotate_pattern_by_90_degrees_clockwise(self):
        
        for position in range(len(self.pattern_relative_coordinates)):
            
            position = self.pattern_relative_coordinates[position]
                       
            position.relative_x, position.relative_y= position.relative_y * -1, position.relative_x
        
    def _generate_pattern_permutations_strings(self):
        
        pattern_permutation_strings = []

        for x in range(4):
            pattern_relative_coordinates_sorted = sorted(self.pattern_relative_coordinates, 
                   key= lambda relative_coordinate : [relative_coordinate.relative_y, relative_coordinate.relative_x])
            
            pattern_permutation_strings.append("".join([y.char for y in pattern_relative_coordinates_sorted]))
                    
            self._rotate_pattern_by_90_degrees_clockwise()

        return pattern_permutation_strings

    def check_for_pattern(self, input, current_coordinate):

        pattern_string = "".join([input[current_coordinate[1] + coordinate.relative_y][current_coordinate[0] + coordinate.relative_x] for coordinate in self.pattern_relative_coordinates])

        if pattern_string in self.pattern_permuation_strings:
            return True
        
        return False
    
    def print_pattern_coordinates(self):
        
        for coordinates in self.pattern_relative_coordinates:

            print(f"char: {coordinates.char}, x: {coordinates.relative_x}, y: {coordinates.relative_y}", end="; ")
        
        print("")

class PatternDimensionAnalyser():
    def __init__(self, pattern_coordinates):
        self._longest_pattern_dimension = self._check_longest_dimension_of_pattern_perimeter(pattern_coordinates)
        
    def _check_longest_dimension_of_pattern_perimeter(self, pattern_coordinates):

        smallest_x = 0
        largest_x = 0
        smallest_y = 0
        largest_y = 0

        for coordinate in pattern_coordinates:
            
            if smallest_x > coordinate.relative_x:
                smallest_x = coordinate.relative_x
            elif largest_x < coordinate.relative_x:
                largest_x = coordinate.relative_x
            
            if smallest_y > coordinate.relative_y:
                smallest_y = coordinate.relative_y
            elif largest_y < coordinate.relative_y:
                largest_y = coordinate.relative_y

        x_difference = largest_x - smallest_x
        y_difference =  largest_y - smallest_y

        if x_difference > y_difference:
            return x_difference
        else:
            return y_difference

    def get_longest_dimension_of_pattern_perimeter(self):
        return self._longest_pattern_dimension

if __name__ == "__main__":

    input_parser = input_parser.InputParser(r"C:\Users\kylek\Documents\code\Advent_of_code\2024\Day_4\input.txt")

    x_mas_pattern_search = PatternSearch(input_parser.parsed_input)

    x_mas_pattern_coordinates =  [Position("M", -1, -1),
                                  Position("S", 1, -1),
                                  Position("A", 0, 0),
                                  Position("M", -1, 1),
                                  Position("S", 1, 1)]
    
    x_mas_pattern_checker = PatternChecker(x_mas_pattern_coordinates)

    x_mas_pattern_analyser = PatternDimensionAnalyser(x_mas_pattern_coordinates)

    print(x_mas_pattern_search.count_pattern_instances(x_mas_pattern_analyser.get_longest_dimension_of_pattern_perimeter(), x_mas_pattern_checker.check_for_pattern))
