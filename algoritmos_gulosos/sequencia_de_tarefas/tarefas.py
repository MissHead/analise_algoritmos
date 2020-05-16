def programacao_tarefas(tarefas, t): 
    quantidade = len(tarefas) 
    for i in range(quantidade): 
        for j in range(quantidade - 1 - i): 
            if tarefas[j][2] < tarefas[j + 1][2]: 
                tarefas[j], tarefas[j + 1] = tarefas[j + 1], tarefas[j] 
    lucro = [False] * t 
    trabalho = ['-1'] * t 
    for i in range(len(tarefas)): 
        for j in range(min(t - 1, tarefas[i][1] - 1), -1, -1): 
            if lucro[j] is False: 
                lucro[j] = True
                trabalho[j] = tarefas[i][0] 
                break
    print(trabalho) 

tarefas = [['atividade1', 1, 15],
          ['atividade2', 2, 43], 
          ['atividade3', 3, 22], 
          ['atividade4', 1, 75], 
          ['atividade5', 2, 100]] 
programacao_tarefas(tarefas, 3)