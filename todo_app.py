import requests
import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do App")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        # API endpoint
        self.api_url = "http://localhost:5000/api/todos"  # Updated port to 5000

    def refresh_tasks(self, event=None):
        # Clear current items
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            # Get all tasks
            response = requests.get(self.api_url)
            if response.status_code == 200:
                tasks = response.json()
                
                # Apply filters
                category_filter = self.filter_category_var.get()
                status_filter = self.filter_status_var.get()

                for task in tasks:
                    if (category_filter == "All Categories" or task['category'] == category_filter) and \
                       (status_filter == "All" or task['status'] == status_filter):
                        self.tree.insert("", "end", values=(
                            task['id'],
                            task['task'],
                            task['category'] or "",
                            task['due_date'] or "",
                            task['status']
                        ))
            else:
                error_msg = response.json().get('error', 'Failed to fetch tasks')
                messagebox.showerror("Error", error_msg)
        except requests.exceptions.ConnectionError:
            messagebox.showerror("Error", "Could not connect to the server. Make sure the Flask server is running on port 5000.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}") 