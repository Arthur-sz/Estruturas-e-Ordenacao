"""
Estruturas de Dados e Ordenação
===============================
Programa de console que integra três estruturas de dados simples
(Pilha, Fila e Fila Circular) com três algoritmos de ordenação
(Bubble Sort, Selection Sort e Insertion Sort).

Regra central do programa: as três estruturas usam SEMPRE o mesmo
vetor, chamado "dados". Só existe uma estrutura ativa por vez; criar
outra substitui a anterior. A ordenação é aplicada à estrutura ativa.

Como executar:
    python estruturas_ordenacao.py
"""

# ---------------------------------------------------------------------------
# ESTADO GLOBAL
# ---------------------------------------------------------------------------
dados = []        # vetor único usado por pilha, fila e fila circular
tipo = None       # None, "pilha", "fila" ou "fila_circular"
tamanho = 0       # capacidade máxima da estrutura ativa
topo = -1         # pilha: índice do último elemento (-1 = vazia)
rpos = 0          # filas: índice do próximo elemento a sair (remoção)
spos = 0          # filas: índice da próxima posição livre (inserção)
qtd = 0           # fila circular: quantidade de elementos armazenados


# ---------------------------------------------------------------------------
# ENTRADA SEGURA
# ---------------------------------------------------------------------------
def ler_inteiro(mensagem):
    """Pede um número inteiro e repete até o usuário digitar um válido."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


# ---------------------------------------------------------------------------
# CRIAÇÃO DA ESTRUTURA
# ---------------------------------------------------------------------------
def criar_estrutura(novo_tipo):
    """Cria (ou recria) a estrutura 'novo_tipo' no vetor 'dados'."""
    global dados, tipo, tamanho, topo, rpos, spos, qtd

    if tipo is not None:
        print(f"\nAtenção: já existe uma {tipo.replace('_', ' ')} ativa. "
              "Criar uma nova apaga os dados atuais.")
        if input("Deseja continuar? (s/n): ").strip().lower() != "s":
            print("Operação cancelada.")
            return

    n = ler_inteiro("Digite o tamanho da estrutura: ")
    while n <= 0:
        print("O tamanho deve ser maior que zero.")
        n = ler_inteiro("Digite o tamanho da estrutura: ")

    tamanho = n
    dados = [None] * tamanho      # posições vazias são representadas por None
    tipo = novo_tipo
    topo = -1
    rpos = 0
    spos = 0
    qtd = 0
    print(f"\n{novo_tipo.replace('_', ' ').capitalize()} criada com capacidade {tamanho}.")


# ---------------------------------------------------------------------------
# PILHA (LIFO: o último a entrar é o primeiro a sair)
# ---------------------------------------------------------------------------
def push_pilha(valor):
    global topo
    if topo == tamanho - 1:
        print("\nPilha cheia!!!")
        return
    topo += 1
    dados[topo] = valor
    print(f"Valor {valor} empilhado.")


def pop_pilha():
    global topo
    if topo < 0:
        print("\nPilha vazia!!!")
        return None
    valor = dados[topo]
    dados[topo] = None
    topo -= 1
    return valor


def show_pilha():
    if topo < 0:
        print("\nPilha vazia.")
        return
    print("\nPilha (do topo para a base):")
    for i in range(topo, -1, -1):
        marca = "  <- topo" if i == topo else ""
        print(f"  [{i}] {dados[i]}{marca}")


# ---------------------------------------------------------------------------
# FILA SIMPLES (FIFO: o primeiro a entrar é o primeiro a sair)
# ---------------------------------------------------------------------------
def push_fila(valor):
    global spos
    if spos == tamanho:
        print("\nFila cheia!!! (a fila simples não reaproveita posições "
              "já removidas; para isso, use a Fila Circular)")
        return
    dados[spos] = valor
    spos += 1
    print(f"Valor {valor} enfileirado.")


def pop_fila():
    global rpos
    if rpos == spos:
        print("\nFila vazia!!!")
        return None
    valor = dados[rpos]
    dados[rpos] = None
    rpos += 1
    return valor


def show_fila():
    if rpos == spos:
        print("\nFila vazia.")
        return
    print("\nFila (do primeiro ao último):")
    for i in range(rpos, spos):
        print(f"  [{i}] {dados[i]}")


# ---------------------------------------------------------------------------
# FILA CIRCULAR (FIFO reaproveitando posições com o operador %)
# ---------------------------------------------------------------------------
def push_circular(valor):
    global spos, qtd
    if qtd == tamanho:
        print("\nFila circular cheia!!!")
        return
    dados[spos] = valor
    spos = (spos + 1) % tamanho   # volta para 0 ao chegar no fim do vetor
    qtd += 1
    print(f"Valor {valor} enfileirado.")


def pop_circular():
    global rpos, qtd
    if qtd == 0:
        print("\nFila circular vazia!!!")
        return None
    valor = dados[rpos]
    dados[rpos] = None
    rpos = (rpos + 1) % tamanho
    qtd -= 1
    return valor


def show_circular():
    if qtd == 0:
        print("\nFila circular vazia.")
        return
    print("\nFila circular (do primeiro ao último):")
    for k in range(qtd):
        i = (rpos + k) % tamanho
        print(f"  [{i}] {dados[i]}")


# ---------------------------------------------------------------------------
# IMPRESSÃO DETALHADA (vetor bruto + ponteiros) — útil para estudar
# ---------------------------------------------------------------------------
def imprimir_conteudo():
    """Mostra os elementos na ordem lógica e o vetor 'dados' por dentro."""
    if tipo == "pilha":
        show_pilha()
        ponteiros = f"topo = {topo}"
    elif tipo == "fila":
        show_fila()
        ponteiros = f"rpos = {rpos}   spos = {spos}"
    else:
        show_circular()
        ponteiros = f"rpos = {rpos}   spos = {spos}   qtd = {qtd}"
    print(f"\nVetor interno 'dados': {dados}")
    print(f"Ponteiros: {ponteiros}   tamanho = {tamanho}")


# ---------------------------------------------------------------------------
# ALGORITMOS DE ORDENAÇÃO (trabalham sobre uma lista A, de forma crescente)
# ---------------------------------------------------------------------------
def ordenacao_bolha(A):
    """Bubble Sort: troca vizinhos fora de ordem; o maior 'sobe' ao fim."""
    n = len(A)
    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):     # os i últimos já estão no lugar
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                trocou = True
        if not trocou:                     # nenhuma troca: já está ordenado
            break


def ordenacao_selecao(A):
    """Selection Sort: escolhe o menor do restante e põe na posição i."""
    n = len(A)
    for i in range(n):
        minimo = i
        for j in range(i + 1, n):
            if A[minimo] > A[j]:
                minimo = j
        A[i], A[minimo] = A[minimo], A[i]


def ordenacao_insercao(A):
    """Insertion Sort: insere cada elemento na posição certa à esquerda."""
    n = len(A)
    for j in range(1, n):
        chave = A[j]
        i = j - 1
        while i >= 0 and A[i] > chave:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = chave


# ---------------------------------------------------------------------------
# PONTE ENTRE A ESTRUTURA ATIVA E OS ALGORITMOS
# ---------------------------------------------------------------------------
def obter_elementos():
    """Copia os elementos válidos da estrutura ativa, na ordem lógica."""
    if tipo == "pilha":
        return dados[0:topo + 1]
    if tipo == "fila":
        return dados[rpos:spos]
    return [dados[(rpos + k) % tamanho] for k in range(qtd)]


def gravar_elementos(lista):
    """Devolve a lista ordenada às mesmas posições dentro de 'dados'."""
    if tipo == "pilha":
        for i, v in enumerate(lista):
            dados[i] = v
    elif tipo == "fila":
        for i, v in enumerate(lista):
            dados[rpos + i] = v
    else:
        for k, v in enumerate(lista):
            dados[(rpos + k) % tamanho] = v


def aplicar_ordenacao(algoritmo, nome):
    elementos = obter_elementos()
    if len(elementos) < 2:
        print("\nÉ preciso ter pelo menos 2 valores armazenados para ordenar.")
        return
    print(f"\nAntes ({nome}):  {elementos}")
    algoritmo(elementos)
    gravar_elementos(elementos)
    print(f"Depois ({nome}): {elementos}")
    print("A estrutura foi atualizada (ordem crescente do primeiro ao último "
          "elemento lógico; na pilha, a base é o menor e o topo é o maior).")


# ---------------------------------------------------------------------------
# MENUS
# ---------------------------------------------------------------------------
def menu_principal():
    print("\n***********************************")
    print("| Estruturas de Dados e Ordenação |")
    print("-----------------------------------")
    print("| 1 - PILHA                       |")
    print("| 2 - FILA                        |")
    print("| 3 - FILA CIRCULAR               |")
    print("| 4 - ORDENAR                     |")
    print("| 5 - SAIR                        |")
    print("-----------------------------------")
    return ler_inteiro("Digite a opção desejada: ")


def menu_estrutura(nome, nome_tipo, push, pop):
    """Submenu genérico, igual para as três estruturas."""
    while True:
        print("\n-----------------------------------")
        print(f"| {nome:<31} |")
        print("-----------------------------------")
        print("| 1 - Criar estrutura             |")
        print("| 2 - Armazenar valor             |")
        print("| 3 - Extrair valor               |")
        print("| 4 - Imprimir conteúdo           |")
        print("| 5 - Voltar ao menu anterior     |")
        print("-----------------------------------")
        opcao = ler_inteiro("Digite a opção desejada: ")

        if opcao == 5:
            print("Voltando ao menu anterior...")
            return
        if opcao == 1:
            criar_estrutura(nome_tipo)
            continue
        if opcao not in (2, 3, 4):
            print("Opção inexistente.")
            continue

        # Opções 2, 3 e 4 exigem que ESTA estrutura exista.
        if tipo != nome_tipo:
            print(f"\nNenhuma {nome.lower()} criada. Escolha '1 - Criar estrutura' primeiro.")
            continue

        if opcao == 2:
            push(ler_inteiro("Digite o valor (inteiro) a armazenar: "))
        elif opcao == 3:
            valor = pop()
            if valor is not None:
                print(f"Valor extraído: {valor}")
        else:
            imprimir_conteudo()


def menu_ordenar():
    while True:
        print("\n-----------------------------------")
        print("| Ordenar                         |")
        print("-----------------------------------")
        print("| 1 - Bubble Sort                 |")
        print("| 2 - Selection Sort              |")
        print("| 3 - Insertion Sort              |")
        print("| 4 - Voltar ao menu anterior     |")
        print("-----------------------------------")
        opcao = ler_inteiro("Digite a opção desejada: ")

        if opcao == 4:
            print("Voltando ao menu anterior...")
            return
        if opcao not in (1, 2, 3):
            print("Opção inexistente.")
            continue

        if tipo is None:
            print("\nNenhuma estrutura criada ainda. Volte ao menu principal e "
                  "escolha primeiro 1 (Pilha), 2 (Fila) ou 3 (Fila Circular).")
            return

        if opcao == 1:
            aplicar_ordenacao(ordenacao_bolha, "Bubble Sort")
        elif opcao == 2:
            aplicar_ordenacao(ordenacao_selecao, "Selection Sort")
        else:
            aplicar_ordenacao(ordenacao_insercao, "Insertion Sort")


# ---------------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------------------------
def main():
    while True:
        opcao = menu_principal()
        if opcao == 5:
            break
        elif opcao == 1:
            menu_estrutura("Pilha", "pilha", push_pilha, pop_pilha)
        elif opcao == 2:
            menu_estrutura("Fila", "fila", push_fila, pop_fila)
        elif opcao == 3:
            menu_estrutura("Fila circular", "fila_circular",
                           push_circular, pop_circular, show_circular)
        elif opcao == 4:
            menu_ordenar()
        else:
            print("Opção inexistente.")
    print("Programa finalizado.")


if __name__ == "__main__":
    main()
