#implementing Queue using list
queue = []
#add element 
def enqueue():
    element = input("Enter the element:")
    queue.append(element)
    print(element, " is add to Queue")

#removing element
def dequeue():
    if not queue:
        print("Queue is empty!")
    else:
        e = queue.pop(0)
        print(e, " is Removed from Queue")

#display the queue
def display():
    print(queue)

while True:
    print("Select the operation 1.add 2.remove 3.display 4.exit")
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice ==3:
        display()
    elif choice == 4:
        break
    else:
        print("Please enter the correct choice!")
