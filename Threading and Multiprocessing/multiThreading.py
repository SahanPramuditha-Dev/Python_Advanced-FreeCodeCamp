from threading import Thread   # Used to create multiple threads (lightweight concurrency)
import os
import time

# Function that will run in each thread
def square_numbers():
    for i in range(100):
        i * i   # CPU-bound operation (result not stored)
        time.sleep(0.1)  # Simulates work / I/O delay


if __name__ == "__main__":

    threads = []  # Store all thread objects

    # CPU count (used here only as a reference, not strict rule for threads)
    num_threads = os.cpu_count()

    # Create threads
    for i in range(num_threads):
        t = Thread(target=square_numbers)
        threads.append(t)

    # Start all threads
    for t in threads:
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print(f"Num of Threads: {num_threads}")
    print("All threads finished.")