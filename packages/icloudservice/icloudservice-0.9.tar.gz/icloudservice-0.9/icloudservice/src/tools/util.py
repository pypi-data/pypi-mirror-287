import os


class FileUtils:
    @staticmethod
    def get_file_extension(key: str) -> str:
        """Get the file extension from the object key and determine the file type."""
        _, ext = os.path.splitext(key)
        ext = ext.lower()  # Convert to lowercase for consistency

        # Determine file type based on the extension
        if ext in ['.txt']:
            return 'Text File'
        elif ext in ['.json']:
            return 'JSON File'
        elif ext in ['.parquet']:
            return 'Parquet File'
        elif ext in ['.csv']:
            return 'CSV File'
        elif ext in ['.xml']:
            return 'XML File'
        else:
            return 'Unknown Type'
    @staticmethod
    def format_size(size_in_bytes: int) -> str:
        """Converts bytes to a more readable size format (KB, MB, GB)."""
        if size_in_bytes < 1024:
            return f"{size_in_bytes} B"
        elif size_in_bytes < 1024 ** 2:
            return f"{size_in_bytes / 1024:.2f} KB"
        elif size_in_bytes < 1024 ** 3:
            return f"{size_in_bytes / 1024 ** 2:.2f} MB"
        else:
            return f"{size_in_bytes / 1024 ** 3:.2f} GB"
        
    @staticmethod
    def get_file_name(file_path:str)->str:
        if not isinstance(file_path, str):
            return ''
        return os.path.basename(file_path)
    @staticmethod
    def get_pwd():
        return os.getcwd()
    
    @staticmethod
    def get_local_path_default(path:str):
        return os.path.join(FileUtils.get_pwd(), FileUtils.get_file_name(path))
    @staticmethod
    def get_path(path:str,name:str)->str:
        return os.path.join(path, name)