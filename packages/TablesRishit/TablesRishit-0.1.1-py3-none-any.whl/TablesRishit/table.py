import math

class _internal_functions:
    def __init__(self) -> None:
        pass

    def row_count(self, data: list) -> int:
        return len(data)

    def column_count(self, data: list) -> int:
        return len(data[0])

    def get_max_row_item_length(self, data: list, index: int) -> int:
        return max(len(row[index]) for row in data)

    def calculate_total_column_length(self, max_item_lengths: list, minimum_padding: int, index: int) -> int:
        return max_item_lengths[index] + minimum_padding * 2

    def calculate_padding(self, data: str, max_item_length: int, minimum_padding: int) -> tuple:
        total_padding = max_item_length + minimum_padding * 2 - len(data)
        padding_left = minimum_padding
        padding_right = minimum_padding
        if total_padding % 2 == 0:
            padding_per_side = max((total_padding / 2), minimum_padding)
            padding_left = padding_per_side
            padding_right = padding_per_side
        else:
            padding_per_side = int(max((total_padding / 2), minimum_padding))
            padding_left = padding_per_side
            padding_right = padding_per_side + 1
        return int(padding_left), int(padding_right)

    def print_between_pattern(self, max_item_lengths: list, minimum_padding: int):
        column_count = len(max_item_lengths)
        for i in range(column_count):
            if i == 0:
                print('|', end='')
            if i != column_count - 1:
                print(self.calculate_total_column_length(max_item_lengths, minimum_padding, i) * "-" + '+', end='')
            else:
                print(self.calculate_total_column_length(max_item_lengths, minimum_padding, i) * "-", end='')
        print('|')


class Table:
    def __init__(self):
        self.fn = _internal_functions()

    def create(self, data: list, minimum_padding: int, headings: list):
        row_count = self.fn.row_count(data)
        column_count = self.fn.column_count(data)

        if column_count != len(headings):
            raise ValueError("Headings must match the number of columns")

        max_item_lengths = [max(self.fn.get_max_row_item_length(data, i), len(headings[i])) for i in range(column_count)]

        self.fn.print_between_pattern(max_item_lengths=max_item_lengths, minimum_padding=minimum_padding)
        
        print('|', end='')
        for index, heading in enumerate(headings):
            padding_left, padding_right = self.fn.calculate_padding(
                data=heading,
                max_item_length=max_item_lengths[index],
                minimum_padding=minimum_padding
            )
            print(' ' * padding_left + heading + ' ' * padding_right + '|', end='')
        print('')
        self.fn.print_between_pattern(max_item_lengths=max_item_lengths, minimum_padding=minimum_padding)

        for row in data:
            print('|', end='')
            for index, column in enumerate(row):
                padding_left, padding_right = self.fn.calculate_padding(
                    data=column,
                    max_item_length=max_item_lengths[index],
                    minimum_padding=minimum_padding
                )
                print(' ' * padding_left + column + ' ' * padding_right + '|', end='')
            print('')
            self.fn.print_between_pattern(max_item_lengths=max_item_lengths, minimum_padding=minimum_padding)
