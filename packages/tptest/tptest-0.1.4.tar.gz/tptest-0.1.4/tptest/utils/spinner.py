import threading
import itertools
import time
import sys


class SpinnerThread(threading.Thread):
    def __init__(self, message):
        super().__init__()
        self.message = message
        self.spinner_chars = itertools.cycle(['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷'])
        self.running = True
        self.start_time = time.time()

    def run(self):
        print(self.message)
        while self.running:
            elapsed_time = int(time.time() - self.start_time)
            sys.stdout.write(f'\r{next(self.spinner_chars)} Executing Test (Elapsed Time: {elapsed_time}s)')
            sys.stdout.flush()
            time.sleep(0.1)

    def stop(self):
        self.running = False
        sys.stdout.write('\r \r')  # Clear the spinner line
        sys.stdout.flush()
