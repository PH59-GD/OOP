#Queue FIFO, Deaqueue() adding at the end, enqueue() remove at the start
Queue = []
def enqueue():
    UC = int(input("How many items to add?: "))
    for i in range(UC):
        UI = int(input("What to add?(INT): "))
        Queue.append(UI)
def dequeue():
    del Queue[0]
def display_queue():
    print(Queue)
while 1:
    print("")
    print("[1] Add to queue")
    print("[2] Remove first in queue")
    print("[3] Display queue")
    print("[4] Exit")
    print("")
    UI = input("Input: ")
    if UI == "1":
        enqueue()
    elif UI == "2" and len(Queue) > 0:
        dequeue()
        print("First item removed.")
    elif UI == "3":
        display_queue()
    if UI == "4":
        print("Exiting...")
        break