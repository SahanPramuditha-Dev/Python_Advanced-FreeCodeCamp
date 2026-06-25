from threading import Thread
import time

# Shared variable (this is accessed by multiple threads)
database_value = 0

def increase():
    global database_value  # Allows modification of the global variable

    # STEP 1: Read shared value into a local copy
    # (This is NOT atomic — another thread can interfere here)
    local_copy = database_value

    # STEP 2: Modify local copy
    local_copy += 1

    # STEP 3: Simulate delay (this increases chance of race condition)
    # During this time, other threads may also read same value
    time.sleep(0.1)

    # STEP 4: Write back to shared variable
    # This overwrites whatever is currently in database_value
    database_value = local_copy


if __name__ == "__main__":

    # Initial state of shared variable
    print("start value", database_value)

    # Create two threads that will run the same function concurrently
    thread1 = Thread(target=increase)
    thread2 = Thread(target=increase)

    # Start both threads (they run at the same time)
    thread1.start()
    thread2.start()

    # Wait for both threads to complete before continuing
    thread1.join()
    thread2.join()

    # Final value after both threads finish
    print("end Value", database_value)

    print("End Main")