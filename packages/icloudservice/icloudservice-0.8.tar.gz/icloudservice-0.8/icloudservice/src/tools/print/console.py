import sys
from typing import Any

class Console:
    INFO_COLOR = '\033[94m'    # Blue
    WARNING_COLOR = '\033[93m' # Yellow
    ERROR_COLOR = '\033[91m'   # Red
    RESET_COLOR = '\033[0m'    # Reset to default
    BOLD = '\033[0m'           # Bold text
    UNDERLINE = '\033[4m'      # Underline text
    MAGENTA =  '\033[35m'

    def info(self, message: Any):
        self._print_message(message, self.INFO_COLOR)

    def write(self, message: Any):
        self._print_message(message, self.MAGENTA)
    def warning(self, message: str):
        self._print_message(message, self.WARNING_COLOR)

    def error(self, message: str):
        self._print_message(message, self.ERROR_COLOR)

    def _print_message(self, message: str, color: str):
        formatted_message = f"{color}{self.BOLD}{message}{self.RESET_COLOR}"
        if 'ipykernel' in sys.modules:
            from IPython.display import display, HTML
            display(HTML(f"<pre style='color:{color[2:-1]}; font-weight:bold;'>{message}</pre>"))
        else:
            print(formatted_message)