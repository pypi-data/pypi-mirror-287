import time
import sys
from threading import Thread
from pipsetup.progress.color_text import AnsiColors

class ProgressIndicator:
    def __init__(self, message: str, interval: float = 0.2, color: str = AnsiColors.OKBLUE):
        self.message = message
        self.interval = interval
        self.color = color
        self.reset_color = AnsiColors.ENDC
        self.running = False
        self.thread = None
        self.start_time = None
        self.exception_occurred = False
        self.stopped = False
        self.spinner_chars = ['|', '/', '-', '\\','']
        self.colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
        self.reset_color = '\033[0m'

    def start(self):
        """Starts the progress indicator animation."""
        if self.thread is None:
            self.thread = Thread(target=self._run)
            self.running = True
            self.start_time = time.time()
            self.thread.start()

    def _run(self):
        """Internal logic for the progress indicator thread."""
        idx = 0
        color_idx = 0
        while self.running:
            for i in range(5):
                if not self.running:
                    break
                sys.stdout.write(f'\r{self.color}{self.message} {"." * (i + 1)}{self.reset_color}{self.colors[color_idx]}{self.spinner_chars[idx]}{self.reset_color}')
                sys.stdout.flush()
                idx = (idx + 1) % len(self.spinner_chars)
                color_idx = (color_idx + 1) % len(self.colors)
                time.sleep(self.interval)
        
        # Clear the final line
        sys.stdout.write('\r' + ' ' * (len(self.message) + 6) + '\r')
        sys.stdout.flush()

    def stop(self, final_message: str = None, final_message_color: str = AnsiColors.OKGREEN):
        """Stops the progress indicator animation and shows a final message."""
        self.running = False
        if self.thread:
            self.thread.join()
            self.thread = None
        # Clear the final line
        sys.stdout.write('\r' + ' ' * (len(self.message) + 4) + '\r')
        sys.stdout.flush()
        if final_message:
            duration = time.time() - self.start_time
            sys.stdout.write(f'{final_message_color}{final_message} (Duration: {duration:.2f} seconds){self.reset_color}\n')
            sys.stdout.flush()
        else:
            duration = time.time() - self.start_time
            sys.stdout.write(f'{final_message_color}(Duration: {duration:.2f} seconds){self.reset_color}\n')
            sys.stdout.flush()
        self.stopped = True
    def __enter__(self):
        """Starts the progress indicator animation when entering the context."""
        self.start()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Stops the progress indicator animation when exiting the context."""
        if not self.stopped:
            if exc_type:
                self.exception_occurred = True
                self.stop(final_message=f"Exception: {exc_value}", final_message_color=AnsiColors.FAIL) 
            else:
                self.stop(final_message="Process completed", final_message_color=AnsiColors.OKGREEN)