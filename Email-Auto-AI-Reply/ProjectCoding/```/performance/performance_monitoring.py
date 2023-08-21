
import time

class PerformanceMonitor:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()

    def elapsed_time(self):
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        else:
            return None

if __name__ == "__main__":
    monitor = PerformanceMonitor()
    monitor.start()
    # Code to be monitored goes here
    monitor.stop()
    print(f"Elapsed time: {monitor.elapsed_time()} seconds")
