import threading
import time

print(threading.active_count())  # how many threads
print(threading.enumerate())  # all the threads


def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")


def drink_coffee():
    time.sleep(4)
    print("You drank coffee")


def workout():
    time.sleep(5)
    print("You did your workout")


eat_breakfast_thread = threading.Thread(target=eat_breakfast, args=())
eat_breakfast_thread.start()

drink_coffee_thread = threading.Thread(target=drink_coffee, args=())
drink_coffee_thread.start()

workout_thread = threading.Thread(target=workout, args=())
workout_thread.start()

eat_breakfast_thread.join()
drink_coffee_thread.join()
workout_thread.join()


print(threading.active_count())  # how many threads
print(threading.enumerate())  # all the threads
print(time.perf_counter())  # How long our main thread took to complete

# daemon threads


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for: " + str(count) + " seconds")

timer_thread = threading.Thread(target=timer, daemon=True)
timer_thread.start()

answer = input("Do you wish to exit?")
