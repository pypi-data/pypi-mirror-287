from icloudservice.src.tools.handler.table_data import TableData
from icloudservice.src.tools.format.table_render import TableRenderer

from typing import List, Dict, Any


class ITableData(TableData):
    def __init__(self, structure: List[Dict[str, Any]]):
        super().__init__(structure)
    
    def as_table(self) -> TableRenderer:
        return TableRenderer(self.data, self.columns)
    
    def __repr__(self) -> str:
        return self.as_table().render()
    