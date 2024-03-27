# Mini Project

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Your tasks:")
            for i in range(len(self.tasks)):
                print(f"{i+1}. {self.tasks[i]}")

    def delete_task(self, index):
        try:
            del self.tasks[index - 1]
            print("Task deleted.")
        except IndexError:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nWelcome to the To-Do List App!\n")
        print("Menu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Quit")

        choice = input("Enter your choice (1,2,3, or 4): ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.view_tasks()
            if todo_list.tasks:
                index = int(input("Enter the task number to delete: "))
                todo_list.delete_task(index)
        elif choice == '4':
            print("Thank you for using the To-Do List App. Goodbye!")
            break
        else:
            print("Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()


# # Read me
# Adding Tasks: You can add a new task to the list by selecting option 1 from the menu and then entering any task you would like to add.
# Viewing Tasks: When you choose option 2, it allows you to view all the tasks thats are currebtly in your To-Do List, and if there are no tasks it will notify you that there are none.
# Delete a Task: You can remove a task from the list by selecting option 3, then you could enter the number corresponding to the task you want to delete.
# Quit: Option 4 exits the app and thanks you for using the To-Do List App.    