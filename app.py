import json
import os
import tkinter as tk
from tkinter import messagebox


class TodoApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Tarefas v1.0")
        self.root.geometry("400x450")

        # Caminho para salvar os dados na pasta do usuário (evita problemas de permissão)
        self.data_dir = os.path.join(os.path.expanduser("~"), ".todo_app")
        os.makedirs(self.data_dir, exist_ok=True)
        self.data_file = os.path.join(self.data_dir, "tasks.json")

        self.tasks = self.load_data()

        # Interface Gráfica (Tkinter)
        self.label = tk.Label(
            root, text="Minhas Tarefas", font=("Arial", 14, "bold")
        )
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 12), width=30)
        self.entry.pack(pady=5)

        self.add_btn = tk.Button(
            root, text="Adicionar Tarefa", command=self.add_task
        )
        self.add_btn.pack(pady=5)

        self.listbox = tk.Listbox(root, font=("Arial", 11), width=35, height=12)
        self.listbox.pack(pady=10)

        self.remove_btn = tk.Button(
            root, text="Remover Selecionada", command=self.remove_task
        )
        self.remove_btn.pack(pady=5)

        self.update_listbox()

    def load_data(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return []
        return []

    def save_data(self):
        try:
            with open(self.data_file, "w", encoding="utf-8") as f:
                json.dump(self.tasks, f, ensure_ascii=False, indent=4)
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível salvar: {e}")

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.save_data()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Digite uma tarefa válida.")

    def remove_task(self):
        try:
            selected_index = self.listbox.curselection()[0]
            self.tasks.pop(selected_index)
            self.update_listbox()
            self.save_data()
        except IndexError:
            messagebox.showwarning("Aviso", "Selecione uma tarefa para remover.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()