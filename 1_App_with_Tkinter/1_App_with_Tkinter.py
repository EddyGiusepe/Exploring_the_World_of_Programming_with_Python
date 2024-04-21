#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro


Setup:

$ pip install tk-tools
"""
import tkinter as tk
from tkinter import ttk
from tkinter import font

window = tk.Tk()
window.title("Meu App com tkinter")
window.configure(bg="white")
window.geometry("500x530")

def add_task():
    task = entry_task.get()
    if task:
        #task_listbox.insert(tk.END, task)
        add_task_item(task)
        entry_task.delete(0, tk.END)
    if not task:
        entry_task.delete(0, tk.END)
        entry_task.insert(0, "Escreva sua tarefa aqui")
        entry_task.configure(fg="black", width=50)

    
def add_task_item(task):
    task_frame = tk.Frame(task_listbox, bg="white")

    task_label = tk.Label(task_frame, text=task, font=("Garamond", 16), bg="white", width=20, height=1, anchor="w")
    task_label.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=2, anchor="w")

    edit_button = tk.Button(task_frame, text="Edit", command=lambda t=task: edit_task(t), bg="#E31248", fg="white", height=1, width=8,
                        font=("Roboto", 10), relief=tk.FLAT, borderwidth=0, cursor="hand2")
    edit_button.pack(side=tk.RIGHT, padx=5, pady=2)

    delete_button = tk.Button(task_frame, text="Delete", command=lambda f=task_frame, l = task_label.cget("text"): delete_task(f, l), bg="#E31248", fg="white", height=1, width=8,
                        font=("Roboto", 10), relief=tk.FLAT, borderwidth=0, cursor="hand2")
    delete_button.pack(side=tk.RIGHT, padx=5, pady=2)

    task_frame.pack(fill=tk.X)
    
    checkbutton = ttk.Checkbutton(task_frame, text="", command=lambda label=task_label: toggle_strike(label))
    checkbutton.pack(side=tk.RIGHT)

    # Adiciona a nova tarefa para o listbox:
    task_listbox.insert(tk.END, task)


def edit_task(task):
    entry_task.delete(0, tk.END)
    entry_task.insert(0, task)

def delete_task(task_frame, task_label_text):
    task_frame.destroy()
    task_listbox.delete(tk.ACTIVE)
    
def toggle_strike(label):
    current_font = label.cget("font")
    if "overstrike" in current_font:
        new_font = current_font.replace("overstrike", "")
    else:
        new_font = current_font + " overstrike"
    label.config(font=new_font)


def on_entry_click(event):
    if entry_task.get() == "Escreva sua tarefa aqui":
        entry_task.delete(0, tk.END)  # Limpe o campo de entrada
        entry_task.configure(fg="black")  # Alterar a cor do texto para preto

def on_focus_out(event):
    if not entry_task.get().strip():
        entry_task.delete(0, tk.END)  # Limpe o campo de entrada
        entry_task.insert(0, "Escreva sua tarefa aqui")  # Inserir texto de espaço reservado
        entry_task.configure(fg="black")  # Alterar a cor do texto para cinza


# Crie um rótulo para o título no lado direito:
heading_font = font.Font(family="Garamond", size=20, weight="bold")

# Crie o rótulo do título com a fonte personalizada:
heading_label = tk.Label(window, text="Bem-Vindo ao meu App", font=heading_font, bg="white")
heading_label.pack(pady=20)  # Adicione algum preenchimento ao redor do título


# Quadro para conter o campo de entrada e botão:
frame = tk.Frame(window)
frame.configure(bg="white")
frame.pack(pady=20)

# Tarefas:
entry_task = tk.Entry(frame, font=("Garamond", 14), relief=tk.FLAT, bg="white")

entry_task.insert(0, "Escreva sua tarefa aqui")  # Inserir texto de espaço reservado
entry_task.bind("<FocusIn>", on_entry_click)  # Vincule o evento click à função on_entry_click
entry_task.bind("<FocusOut>", on_focus_out)  # Vincule o evento focus out à função on_focus_out
entry_task.pack(side=tk.LEFT, padx=0) # Coloque o campo de entrada no lado esquerdo do quadro com algum preenchimento


# Agora vamos criar um Botão para adicionar tarefas:
add_button = tk.Button(frame, text="Adicionar tarefa", command=add_task, bg="#E31248", fg="white", height=1, width=20,
                        font=("Roboto", 11), relief=tk.FLAT, borderwidth=0, cursor="hand2")
add_button.pack(side=tk.LEFT, padx=0)  # Coloque o botão no lado esquerdo da moldura

task_listbox = tk.Listbox(window, font=("Garamond", 16), width=80, height=10, bg="white", relief=tk.FLAT,  highlightthickness=0)
task_listbox.pack(padx=5, pady=5)





window.mainloop()
