from functools import lru_cache
from typing import List, Dict, Any
from icloudservice.src.tools.format.color_text import AnsiColors as color

class TableRenderer:
    def __init__(self, data: List[Dict[str, Any]], columns: List[str]):
        self.data = data
        self.columns = columns
        

    def get_column_widths(self) -> List[int]:
        # Determine the maximum width for each column
        column_widths = [max(len(str(item)) for item in col) for col in zip(*self.data, self.columns)]
        column_widths = [max(width, len(header)) for width, header in zip(column_widths, self.columns)]
        return column_widths

    def render(self) -> str:
        if not self.data:
            return "No structure available"
        
        header_color = color.HEADER_COLOR
        row_color = color.ROW_COLOR
        reset_color = color.ENDC
        
        column_widths = self.get_column_widths()
        headers = self.columns
        rows = [list(row.values()) for row in self.data]
        
        # Calculate the maximum row width
        max_row_width = max(sum(len(str(item)) for item in row) + len(row) * 5 for row in rows)
        border_width = max(max_row_width, sum(column_widths) + len(headers) * 3 + 1)
        
        # Create the table as a string
        table_str = '+' + '-' * (border_width - 2) + '+\n'  # Top border
        
        # Header row
        table_str += f"|{header_color}{' | '.join(header.center(width) for header, width in zip(headers, column_widths))}{reset_color}|\n"
        table_str += '+' + '-' * (border_width - 2) + '+\n'  # Header separator
        
        # Data rows
        for row in rows:
            table_str += f"|{row_color}{' | '.join(str(item).center(width) for item, width in zip(row, column_widths))}{reset_color}|\n"
        
        table_str += '+' + '-' * (border_width - 2) + '+\n'  # Bottom border
        return table_str
