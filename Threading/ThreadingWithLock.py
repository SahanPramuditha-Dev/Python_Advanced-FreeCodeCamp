from threading import Thread, Lock
import time

# Shared resource (critical section target)
database_value = 0

# Lock object to ensure only one thread modifies shared data at a time
lock = Lock()

def increase():
    global database_value

    # Enter critical section (only one thread allowed at a time)
    with lock:
        # STEP 1: Safely read shared value
        local_copy = database_value

        # STEP 2: Modify local copy
        local_copy += 1

        # STEP 3: Simulate processing delay
        # Even if other threads are waiting, they cannot enter this block
        time.sleep(0.1)

        # STEP 4: Write back safely
        database_value = local_copy
    # Lock is automatically released here


if __name__ == "__main__":

    print("start value", database_value)

    # Create threads
    thread1 = Thread(target=increase)
    thread2 = Thread(target=increase)

    # Start execution
    thread1.start()
    thread2.start()

    # Wait for completion
    thread1.join()
    thread2.join()

    print("end Value", database_value)
    print("End Main")