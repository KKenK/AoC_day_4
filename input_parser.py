class InputParser():

    def __init__(self, input_path):

        input = []

        with open(input_path) as f:
            input = f.read()

        self.parsed_input = self._parse_file(input)

    def _parse_file(self, input):

        lines = [x for x in input.split("\n")]

        return lines

if __name__ == "__main__":

    input_parser = InputParser(r"C:\Users\kylek\Documents\code\Advent_of_code\2024\Day_4\test.txt")

    print(input_parser.parsed_input)