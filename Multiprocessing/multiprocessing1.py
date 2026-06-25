from multiprocessing import Process
import os
import time

# Function that will run in separate processes
def worker(name):
    print(f"Process {name} started | PID: {os.getpid()}")
    time.sleep(2)  # simulate work
    print(f"Process {name} finished | PID: {os.getpid()}")


if __name__ == "__main__":

    print("Main process started | PID:", os.getpid())

    # Create processes
    p1 = Process(target=worker, args=("A",))
    p2 = Process(target=worker, args=("B",))

    # Start processes (run in parallel)
    p1.start()
    p2.start()

    # Wait for completion
    p1.join()
    p2.join()

    print("Main process finished")