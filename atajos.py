import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        
        # Variables
        self.tasks = []
        
        # Interfaz Gráfica
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Agregar Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=10)
        self.task_listbox.pack(pady=10)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Atajos de teclado
        self.root.bind('<Return>', lambda event: self.add_task())      # Tecla Enter
        self.root.bind('<c>', lambda event: self.complete_task())      # Tecla C
        self.root.bind('<Delete>', lambda event: self.delete_task())   # Tecla Delete
        self.root.bind('<Escape>', lambda event: self.root.quit())      # Tecla Escape

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            completed_task = self.tasks[selected_index] + " (Completada)"
            self.tasks[selected_index] = completed_task
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)  # Limpiar la lista
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)  # Añadir tareas a la lista

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
