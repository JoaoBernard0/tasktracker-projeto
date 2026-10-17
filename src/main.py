tarefas = []


def cadastrar_tarefa():
    print("\n--- Cadastro de Tarefa ---")

    while True:
        titulo = input("Título: ").strip()

        if titulo:
            break

        print("Erro: o título não pode ficar vazio.")

    descricao = input("Descrição: ").strip()

    while True:
        prioridade = input(
            "Prioridade (Alta/Média/Baixa): "
        ).strip().lower()

        prioridades = {
            "alta": "Alta",
            "média": "Média",
            "media": "Média",
            "baixa": "Baixa"
        }

        if prioridade in prioridades:
            prioridade = prioridades[prioridade]
            break

        print("Erro: informe Alta, Média, Media ou Baixa.")

    data_limite = input(
        "Data limite (DD/MM/AAAA ou outro formato): "
    ).strip()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente"
    }

    tarefas.append(tarefa)
    print("\nTarefa cadastrada com sucesso!")


def visualizar_tarefas():
    print("\n--- Tarefas Cadastradas ---")

    if not tarefas:
        print("Não existem tarefas cadastradas no momento.")
        return

    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {numero}")
        print(f"Título: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Data limite: {tarefa['data_limite']}")
        print(f"Status: {tarefa['status']}")


def menu():
    while True:
        print("\n==============================")
        print("         TASKTRACKER")
        print("==============================")
        print("1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Sair da aplicação")
        print("==============================")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            visualizar_tarefas()
        elif opcao == "3":
            print("Encerrando o TaskTracker. Até mais!")
            break
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    menu()
