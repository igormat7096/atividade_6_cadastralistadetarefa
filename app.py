tarefas= []
while True:
    
    try:
        nova_tarefa = input("Informe a nova tarefa ou 'Enter' para exibir a lista: ")
        if nova_tarefa:
            tarefas.append(nova_tarefa)
            print(f"{nova_tarefa} Cadastrado com sucesso!")
            continue
        else:
            break
    except Exception as e:
        print(f"Não foi possível cadastrar a tarefa. {e}.")

tarefas.sort
for tarefa in tarefas:
    print(tarefa)
    