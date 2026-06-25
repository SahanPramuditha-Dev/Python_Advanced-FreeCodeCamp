from multiprocessing import Process  # Used to create multiple processes (parallel execution)
import os   # Used to get system information like number of CPU cores
import time  # Used to simulate delay (workload simulation)

# This function will run inside each process
def square_numbers():
    for i in range(100):
        i * i  # CPU-bound operation (result is not stored, just computed)
        time.sleep(0.1)  # Simulates work being done (slows execution for demo)


# This ensures the code runs safely on Windows
# (Windows requires this guard for multiprocessing)
if __name__ == "__main__":

    processes = []  # List to store all process objects

    # Get number of CPU cores in the system
    # Example: if CPU has 8 cores → 8 processes will be created
    num_processes = os.cpu_count()

    # Create processes equal to number of CPU cores
    for i in range(num_processes):
        p = Process(target=square_numbers)  # Assign function to process
        processes.append(p)  # Store process for later control

    # Start all processes (they begin running in parallel)
    for p in processes:
        p.start()

    # Wait for all processes to complete before continuing
    for p in processes:
        p.join()


    print(f"Num of Processers in Cpu: {num_processes}")
    # This runs only after all processes are finished
    print("All processes finished.")