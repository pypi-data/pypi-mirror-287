class AnsiColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ROW_COLOR = '\033[33m'
    HEADER_COLOR = '\033[96m'
    
    @staticmethod
    def color_text(text, color):
        return f"{color}{text}{AnsiColors.ENDC}"
