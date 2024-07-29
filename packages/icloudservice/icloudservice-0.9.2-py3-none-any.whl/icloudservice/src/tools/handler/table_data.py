from typing import List, Dict, Any, Union

class TableData:
    def __init__(self, data: List[Dict[str, Any]]):
        self.data = data
        if data:
            self.columns = list(data[0].keys())
        else:
            self.columns = []
    def get_column(self, column_name: str) -> List[Any]:
        return [row.get(column_name) for row in self.data]
    def get_row(self, index: int) -> Dict[str, Any]:
        if index < len(self.data):
            return self.data[index]
        else:
            raise IndexError("Row index out of range")
    def __getitem__(self, key: Union[int, str]) -> Union[Dict[str, Any], List[Any]]:
        if isinstance(key, int):
            return self.get_row(key)
        elif isinstance(key, str):
            return self.get_column(key)
        else:
            raise TypeError("Key must be an integer or string")
    def get_count(self) -> int:
        return len(self.data)
    
    def __repr__(self) -> str:
        return str(self.data)
