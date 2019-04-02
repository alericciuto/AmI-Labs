tasks = {"task1":{"todo": "call John for AmI project organization", "urgent": True},
    "task2":{"todo": "buy a new mouse", "urgent": True},
    "task3":{"todo": "find a present for Angelina’s birthday",  "urgent": False},
    "task4":{"todo": "organize mega party (last week of April)",  "urgent": False},
    "task5":{"todo": "book summer holidays",  "urgent": False},
    "task6":{"todo": "whatsapp Mary for a coffee",  "urgent": False}}

urgentTask = {}
for t in tasks.keys():
    if tasks[t]["urgent"]:
        urgentTask[t] = tasks[t]

print(urgentTask)

