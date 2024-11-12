import json
import os

class Task:
    def _init_(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {"id": self.id, "title": self.title, "completed": self.completed}

class TaskManager:
    def _init_(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, title):
        task_id = len(self.tasks) + 1
        task = Task(task_id, title)
        self.tasks.append(task)
        print("Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for task in self.tasks:
            status = "Completed" if task.completed else "Incomplete"
            print(f"[{task.id}] {task.title} - {status}")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]
        print("Task deleted successfully.")

 def mark_task_as_complete(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                print("Task marked as complete.")
                return
        print("Task not found.")

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file)
        print("Tasks saved to file.")

    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as file:
                tasks_data = json.load(file)
                self.tasks = [Task(**task_data) for task_data in tasks_data]
            print("Tasks loaded from file.")

    def run(self):
        while True:
            print("\nOptions: (1) Add Task (2) View Tasks (3) Delete Task (4) Complete Task (5) Save (6) Exit")
            choice = input("Enter option number: ")
            if choice == "1":
                title = input("Enter task title: ")
                self.add_task(title)
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                task_id = int(input("Enter task ID to delete: "))
                self.delete_task(task_id)
            elif choice == "4":
                task_id = int(input("Enter task ID to mark as complete: "))
                self.mark_task_as_complete(task_id)
            elif choice == "5":
                self.save_tasks()
            elif choice == "6":
                print("Exiting.")
                break
            else:
                print("Invalid option. Please try again.")

if _name_ == "_main_":
    manager = TaskManager()
    manager.run()
