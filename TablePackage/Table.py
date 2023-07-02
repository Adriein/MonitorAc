class Table:

    def __init__(self, data: any, column_widths):
        self.data = data
        self.column_widths = column_widths

    @staticmethod
    def create(data: any) -> 'Table':
        # Determine the maximum width for each column
        column_widths = [max(len(str(row[i])) for row in data) for i in range(len(data[0]))]
        print(column_widths)
        return Table(data, column_widths)

    def print(self) -> None:
        # Print the table header
        self.print_row(self.data[0], self.column_widths)
        self.print_row_separator(self.column_widths)

        # Print the table rows
        for row in self.data[1:]:
            self.print_row(row, self.column_widths)

    def print_row(self, row, column_widths):
        # Print each cell of a row with proper spacing and vertical separators
        for i, cell in enumerate(row):
            print(f"| {str(cell).ljust(column_widths[i])} ", end='')
        print("|")

    def print_row_separator(self, column_widths):
        # Print a row separator using dashes and vertical separators
        for width in column_widths:
            print('+' + '-' * (width + 2), end='')
        print('+')
