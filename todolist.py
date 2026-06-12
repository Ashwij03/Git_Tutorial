tasks = []

while True:
    task = input("Enter task (or 'exit'): ")

    if task.lower() == "exit":
        break

    tasks.append(task)

print("\nTotal Tasks:", len(tasks))
for t in tasks:
    print("-", t)