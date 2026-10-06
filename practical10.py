# =========================
# TASK MANAGEMENT SYSTEM
# =========================
from asyncio import Task
from collections import deque

# Queue for task scheduling(FIFO)
tasks_queue = deque()

#Stack for Undo Operation(LIFO)
undo_stack = []

def add_task(task):
    tasks_queue.append(task)
    print(f"Task added:{task}")

def process_task():
    if tasks_queue:
        task = tasks_queue.popleft()
        print(f"Processing task:{task}")
        undo_stack.append(task)
    else:
        print("No tasks to process.")
        
def undo_task():
    print("\n Pending Tasks (Queue):", list (tasks_queue))
    print("Undo Stack:", undo_stack)
    
# ====================
# MENU DRIVEN PROGRAM
# ====================
while True:
    print("\n ==== TASK MANAGER ====")
    print("1. Add Task")
    print("2. Process Task")
    print("3. Undo Task")
    print("4. Show Task")
    print("5. Exit")
    
    choice = input("Enter Choice:")
    
    if choice == "1":
        task = input("Enter task:")
        add_task(task)
    elif choice == "2":
        process_task()
    elif choice == "3":
        undo_task()
    elif choice == "4":
        show_task()
    elif choice == "5":
        print("Exiting System.....")
        break
    else:
        print("invalid choice")
        