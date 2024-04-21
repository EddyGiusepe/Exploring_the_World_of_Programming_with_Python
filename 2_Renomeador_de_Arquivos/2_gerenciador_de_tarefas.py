#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Tarefa '{task}' adicionada.")

    def list_tasks(self):
        if not self.tasks:
            print("Nenhuma tarefa encontrada.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def mark_task_done(self, task_number):
        if 0 < task_number <= len(self.tasks):
            task = self.tasks.pop(task_number - 1)
            print(f"Tarefa '{task}' marcada como concluída.")
        else:
            print("Número da tarefa inválido.")

    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            task = self.tasks.pop(task_number - 1)
            print(f"Tarefa '{task}' removida.")
        else:
            print("Número da tarefa inválido.")

def main():
    MinhasTarefas = TaskManager()
    while True:
        print("\n1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Remover tarefa")
        print("5. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            task = input("Digite a tarefa: ")
            MinhasTarefas.add_task(task)
        elif choice == "2":
            MinhasTarefas.list_tasks()
        elif choice == "3":
            task_number = int(input("Digite o número da tarefa: "))
            MinhasTarefas.mark_task_done(task_number)
        elif choice == "4":
            task_number = int(input("Digite o número da tarefa: "))
            MinhasTarefas.remove_task(task_number)
        elif choice == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
