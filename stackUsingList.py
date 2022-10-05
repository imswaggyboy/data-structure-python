stack= []
size = int(input("Enter the size of the stack: "))
def push():
    if size == len(stack):
        print("Stack is full!")
    else:
        element = input("Enter the element:")
        stack.append(element)
        print(stack)

def pop_element():
    if not stack:
        print("The stack is empty!")
    else:
        e = stack.pop()
        print("Removed element is:",e)
        print(stack)

while True:
    print("Choose the operation 1.push 2.pop 3.exit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break
    else:
        print("Enter the correct choice")
