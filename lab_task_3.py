import threading
from collections import deque
from concurrent.futures import ThreadPoolExecutor

# Shared thread-safe list (deque with lock)
shared_list = deque()
lock = threading.Lock()

# Function to write to the shared list
def write_to_list(index):
    with lock:
        shared_list.append(f"Item {index}")
        print(f"Added Item {index}")

# Function to read from the shared list
def read_from_list():
    with lock:
        if shared_list:
            item = shared_list.popleft()
            print(f"Read {item}")
        else:
            print("List is empty")

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=4) as executor:
        # Create threads for writing
        for i in range(10):
            executor.submit(write_to_list, i)

        # Create threads for reading
        for _ in range(5):
            executor.submit(read_from_list)

    print("Lab Task 3 completed!")
