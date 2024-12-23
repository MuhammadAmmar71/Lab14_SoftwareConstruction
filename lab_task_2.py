import threading

# Shared counter variable
counter = 0
lock = threading.Lock()

# Function to increment the counter
def increment_counter():
    global counter
    for _ in range(100):
        with lock:  # Ensures synchronization
            counter += 1

if __name__ == "__main__":
    # Create three threads
    threads = [threading.Thread(target=increment_counter) for _ in range(3)]

    # Start threads
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print(f"Final counter value: {counter}")
    print("Lab Task 2 completed!")
