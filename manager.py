def add_task(tasks, task_name):
    task = {"task": task_name, "completed": False}
    tasks.append(task)
    print(f"Tarefa {task_name} foi adicionada com sucesso!")
    return

def view_tasks(tasks):
    print("\nLista de tarefas:")
    for index, task in enumerate (tasks, start=1):
        status ="✓" if task["completed"] else " "
        task_name = task["task"]
        print(f"{index}. [{status}] {task_name}")

def update_task_name(tasks, index_task, new_name_task):
    index_task_adjusted = int(index_task) -1
    if index_task_adjusted >= 0 and index_task_adjusted < len(tasks):
        tasks[index_task_adjusted]["task"] = new_name_task
        print(f"Tarefa {index_task} atualizada para {new_name_task}")
    else:
        print("Tarefa não existe!")
    return

def complete_task(tasks, index_task):
    index_task_adjusted = int(index_task) -1
    tasks[index_task_adjusted]["completed"] = True
    print(f"Tarefa {index_task} completada!")
    return

def delete_completed_task(tasks):
    for task in tasks:
        if task["completed"]:
            tasks.remove(task)
    print("Tarefas completadas foram deletadas!")
    return

tasks = []
while True:
    print("\nMenu do Gerenciador de Lista de tarefas:")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefas")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completas")
    print("6. Sair")

    choice = input("Digite a sua escolha: ")

    if choice == "1":
        task_name = input("Digite o nome da tarefa que deseja adicionar: ")
        add_task(tasks, task_name)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        view_tasks(tasks)
        index_task = input("Digite o número da tarefa que deseja atualizar: ")
        new_name_task = input("Digite o novo nome da tarefa: ")
        update_task_name(tasks, index_task, new_name_task)
    elif choice == "4":
        view_tasks(tasks)
        index_task = input("Digite o número da tarefa a ser completada: ")
        complete_task(tasks, index_task)
    elif choice == "5":
        delete_completed_task(tasks)
        view_tasks(tasks)
    elif choice == "6":
        break

print("Programa finalizado!")