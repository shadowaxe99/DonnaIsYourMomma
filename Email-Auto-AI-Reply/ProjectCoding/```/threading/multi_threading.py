
import threading
import time

class WorkerThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print(f"Thread {self.name} starting.")
        time.sleep(2)
        print(f"Thread {self.name} finished.")

def main():
    threads = []

    for i in range(5):
        thread = WorkerThread(name=f"Thread-{i}")
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
