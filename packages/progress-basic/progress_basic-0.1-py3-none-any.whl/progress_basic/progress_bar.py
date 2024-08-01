import sys
import time
import threading
from progress_basic.format.color_text import AnsiColors

class ProgressBar:
    def __init__(self, total, message='', interval=0.4, bar_length=40, color: str = AnsiColors.OKBLUE):
        self.total = total
        self.message = message
        self.interval = interval
        self.bar_length = bar_length
        self.running = False
        self.current = 0
        self.thread = None
        self.start_time = None
        self.color = color
        self.reset_color = AnsiColors.ENDC

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

    def start(self):
        self.running = True
        self.start_time = time.time()
        self.thread = threading.Thread(target=self._run)
        self.thread.start()

    def stop(self, final_message: str = None):
        self.running = False
        if self.thread:
            self.thread.join()
            self.thread = None
        sys.stdout.write('\r' + ' ' * (self.bar_length + 100) + '\r')
        sys.stdout.flush()

        if final_message:
            duration = time.time() - self.start_time
            sys.stdout.write(f'{AnsiColors.OKGREEN}{final_message} (Duration: {duration:.2f} seconds){self.reset_color}\n')
        else:
            duration = time.time() - self.start_time
            sys.stdout.write(f'{AnsiColors.OKGREEN}(Duration: {duration:.2f} seconds){self.reset_color}\n')

        sys.stdout.flush()

    def update(self, value):
        self.current = value
        self._display()

    def _display(self):
        percent = self.current / self.total
        filled_length = int(self.bar_length * percent)
        bar = '█' * filled_length + '-' * (self.bar_length - filled_length)
        sys.stdout.write(f'\r{self.color}{self.message} |{bar}| {AnsiColors.MAGENDA}{percent * 100:.0f}%{self.reset_color}')
        sys.stdout.flush()

    def _run(self):
        while self.running:
            self._display()
            time.sleep(self.interval)
