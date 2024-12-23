import threading
import time

# Thread to print numbers 1 to 10
def print_numbers():
    for i in range(1, 11):
        print(f"Number: {i}")
        time.sleep(0.1)  # Simulate work

# Thread to print squares of numbers 1 to 10
def print_squares():
    for i in range(1, 11):
        print(f"Square: {i**2}")
        time.sleep(0.1)  # Simulate work

if __name__ == "__main__":
    # Create threads
    thread1 = threading.Thread(target=print_numbers)
    thread2 = threading.Thread(target=print_squares)

    # Start threads
    thread1.start()
    thread2.start()

    # Wait for threads to complete
    thread1.join()
    thread2.join()

    print("Lab Task 1 completed!")
