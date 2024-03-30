# thread = a flow of execution. lick a separate order of instruction.
#          however each thread takes a turn running to archive concurrency
#           GIL = (global interpreter lock),
#           allow only one thread to hold the control of the python interpreter at any one time

# cpu bound = program/task spends most of its time waiting for internal events (CPU intensive)
#             use multiprocessing
# oi bound = program/task spends most of its time waiting for external events (CPU input, web scraping)
#             use multithreading

import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You have done your breakfast")

def eat_lunch():
    time.sleep(4)
    print("You have been finished your lunch")

def eat_dinner():
    time.sleep(5)
    print("You have done your dinner")

x = threading.Thread(target=eat_breakfast(), args=())
x.start()

y = threading.Thread(target=eat_lunch(), args=())
y.start()

z = threading.Thread(target=eat_dinner(), args=())
z.start()

x.join()
y.join()
z.join()

#eat_breakfast()
#eat_lunch()
#eat_dinner()


print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())