#Stack = Push() - Add --- > Pop() - remove. LIFO First In First Out.
Stack = []
def Pushbook():
    UC = int(input("How many items to add?: "))
    for i in range(UC):
        if (len(Stack) < 1):
            UI = int(input("What to add?(INT): "))
            Stack.append(UI)
        else:
            UI = int(input("What to add?(INT): "))
            Stack.insert(0, UI)
def Popbook():
    del Stack[0]
def display():
    print(Stack)
while 1:
    print("")
    print("[1] Add to queue")
    print("[2] Remove first in queue")
    print("[3] Display queue")
    print("[4] Exit")
    print("")
    UI = input("Input: ")
    if UI == "1":
        Pushbook()
    elif UI == "2" and len(Stack) > 0:
        Popbook()
        print("First item removed.")
    elif UI == "3":
        display()
    if UI == "4":
        print("Exiting...")
        break