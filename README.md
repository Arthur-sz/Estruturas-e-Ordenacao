# Estruturas de Dados e Ordenação em Python

Programa de console (terminal) que reúne, em um único menu, **três estruturas de dados** e **três algoritmos de ordenação**:

| Estruturas | Algoritmos de ordenação |
|---|---|
| Pilha | Bubble Sort |
| Fila | Selection Sort |
| Fila Circular | Insertion Sort |

Projeto feito para a disciplina de Estruturas de Dados (UGB). Serve para **aprender e visualizar** como cada estrutura guarda e remove valores dentro de um vetor e como cada algoritmo reorganiza esses valores.

---

## Sumário

1. [Para que serve](#para-que-serve)
2. [Requisitos](#requisitos)
3. [Como executar](#como-executar)
4. [Como usar (passo a passo)](#como-usar-passo-a-passo)
5. [Exemplo de uso](#exemplo-de-uso)
6. [Como funciona](#como-funciona)
7. [Explicação do código](#explicação-do-código)
8. [Correções feitas nos exemplos de aula](#correções-feitas-nos-exemplos-de-aula)
9. [Limitações conhecidas](#limitações-conhecidas)
10. [Estrutura do repositório](#estrutura-do-repositório)

---

## Para que serve

- Praticar o funcionamento de **pilha**, **fila** e **fila circular**.
- Ver, na prática, o resultado de **Bubble Sort**, **Selection Sort** e **Insertion Sort** aplicados a uma estrutura que você mesmo montou.
- Entender como ponteiros (`topo`, `rpos`, `spos`) controlam onde os valores entram e saem.

Regra central: as três estruturas usam **sempre o mesmo vetor, chamado `dados`**. Existe **uma estrutura ativa por vez**; criar outra substitui a anterior (o programa pede confirmação antes).

## Requisitos

- Python **3.6 ou superior** (usa f-strings).
- Nenhuma biblioteca externa. Só a biblioteca padrão.

Para conferir sua versão:

```bash
python --version
```

## Como executar

```bash
# 1. Clone o repositório (troque pelo endereço do seu repositório)
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git

# 2. Entre na pasta
cd SEU_REPOSITORIO

# 3. Execute
python estruturas_ordenacao.py
```

> Em alguns sistemas (Mac/Linux) o comando é `python3 estruturas_ordenacao.py`.

## Como usar (passo a passo)

### Menu principal

```
***********************************
| Estruturas de Dados e Ordenação |
-----------------------------------
| 1 - PILHA                       |
| 2 - FILA                        |
| 3 - FILA CIRCULAR               |
| 4 - ORDENAR                     |
| 5 - SAIR                        |
-----------------------------------
```

### Submenu das estruturas (opções 1, 2 e 3)

| Opção | O que faz |
|---|---|
| 1 - Criar estrutura | Pergunta o **tamanho** e cria o vetor `dados` vazio |
| 2 - Armazenar valor | Pede um número inteiro e o insere (`push`) |
| 3 - Extrair valor | Remove e mostra um valor (`pop`) |
| 4 - Imprimir conteúdo | Mostra os valores na ordem lógica, o vetor interno e os ponteiros |
| 5 - Voltar ao menu anterior | Retorna ao menu principal |

**Importante:** sempre comece por **"1 - Criar estrutura"**. Sem isso, as outras opções avisam que a estrutura ainda não existe.

### Menu Ordenar (opção 4)

Escolha entre Bubble Sort, Selection Sort ou Insertion Sort. O algoritmo é aplicado à estrutura que está ativa. Se nenhuma foi criada, o programa pede que você escolha primeiro 1, 2 ou 3 no menu principal. É preciso ter ao menos 2 valores armazenados.

A ordenação é **crescente**:
- **Fila e fila circular:** o primeiro a sair passa a ser o menor.
- **Pilha:** a base fica com o menor e o **topo com o maior** (o próximo `pop` retira o maior).

## Exemplo de uso

```
Menu principal -> 1 (Pilha)
  1 (Criar)        -> tamanho: 3
  2 (Armazenar)    -> 30
  2 (Armazenar)    -> 10
  2 (Armazenar)    -> 20
  4 (Imprimir)

Pilha (do topo para a base):
  [2] 20  <- topo
  [1] 10
  [0] 30

Vetor interno 'dados': [30, 10, 20]
Ponteiros: topo = 2   tamanho = 3

  5 (Voltar)
Menu principal -> 4 (Ordenar) -> 3 (Insertion Sort)

Antes (Insertion Sort):  [30, 10, 20]
Depois (Insertion Sort): [10, 20, 30]
```

---

## Como funciona

### O vetor `dados`

Ao criar uma estrutura de tamanho `n`, o programa cria uma lista com `n` posições vazias (`None`):

```python
dados = [None] * tamanho    # ex.: tamanho 5 -> [None, None, None, None, None]
```

Cada estrutura usa esse mesmo vetor de um jeito diferente, controlado por variáveis chamadas **ponteiros**.

### Pilha (LIFO: *Last In, First Out*)

O **último a entrar é o primeiro a sair**, como uma pilha de pratos. Só existe um ponteiro: `topo`, o índice do último elemento (`-1` = pilha vazia).

```
push(10), push(20), push(30)

índice:   0    1    2    3    4
dados:  [ 10 | 20 | 30 |None|None]
                     ^
                    topo = 2

pop() -> devolve 30, topo passa a 1
```

- **push:** se `topo == tamanho - 1` a pilha está cheia; senão `topo += 1` e grava o valor.
- **pop:** se `topo < 0` está vazia; senão lê `dados[topo]`, limpa a posição e faz `topo -= 1`.

### Fila (FIFO: *First In, First Out*)

O **primeiro a entrar é o primeiro a sair**, como uma fila de banco. Dois ponteiros:

- `spos`: próxima posição livre (onde o próximo valor entra);
- `rpos`: posição do próximo valor a sair.

```
push(10), push(20), push(30), pop()

índice:   0    1    2    3    4
dados:  [None| 20 | 30 |None|None]
                ^         ^
              rpos=1    spos=3
```

- **Cheia:** `spos == tamanho`.
- **Vazia:** `rpos == spos`.

Na fila simples, as posições à esquerda de `rpos` **não são reaproveitadas**. Isso é uma característica do modelo, e é exatamente o problema que a fila circular resolve.

### Fila circular

Igual à fila, mas quando um ponteiro chega ao fim do vetor ele **volta para o início**. Isso é feito com o operador `%` (resto da divisão):

```python
spos = (spos + 1) % tamanho
```

Exemplo com tamanho 5 (insere 50, 40, 30, 20, 10, remove 2 e insere 5 e 60):

```
índice:   0    1    2    3    4
dados:  [  5 | 60 | 30 | 20 | 10 ]
                    ^
          rpos=2  (spos também = 2, fila cheia: qtd = 5)
```

Como `rpos == spos` ocorre tanto com a fila **vazia** quanto **cheia**, o programa usa uma variável a mais, `qtd` (quantidade de elementos), para diferenciar:

- **Cheia:** `qtd == tamanho`.
- **Vazia:** `qtd == 0`.

### Algoritmos de ordenação

Todos recebem uma lista `A` e a ordenam **no próprio lugar**, em ordem crescente.

| Algoritmo | Ideia | Tempo (pior caso) |
|---|---|---|
| **Bubble Sort** | Compara vizinhos e troca se estiverem fora de ordem. A cada volta, o maior "sobe" para o fim. | O(n²) |
| **Selection Sort** | Procura o menor valor do trecho restante e o coloca na posição atual. | O(n²) |
| **Insertion Sort** | Pega cada elemento e o insere na posição certa dentro da parte já ordenada (como organizar cartas na mão). | O(n²) |

Os três são simples e bons para aprender, mas lentos para listas grandes. Os tempos acima são os valores teóricos conhecidos para esses algoritmos.

### Como a ordenação encontra a estrutura

Os algoritmos trabalham com uma lista comum, então o programa faz uma "ponte" em três passos:

1. `obter_elementos()` copia só os valores **válidos** da estrutura ativa, na ordem lógica (na fila circular ele trata o "dar a volta").
2. O algoritmo escolhido ordena essa lista.
3. `gravar_elementos()` devolve os valores ordenados às **mesmas posições** do vetor `dados`.

Assim os ponteiros (`topo`, `rpos`, `spos`, `qtd`) continuam corretos.

---

## Explicação do código

Tudo está em `estruturas_ordenacao.py`, organizado em blocos:

| Bloco | Funções | Papel |
|---|---|---|
| Estado global | `dados`, `tipo`, `tamanho`, `topo`, `rpos`, `spos`, `qtd` | Guarda a estrutura ativa. `tipo` vale `None`, `"pilha"`, `"fila"` ou `"fila_circular"` |
| Entrada segura | `ler_inteiro` | Repete a pergunta até o usuário digitar um número inteiro (evita erro com letras) |
| Criação | `criar_estrutura` | Pede o tamanho, cria `dados`, zera ponteiros e avisa antes de substituir uma estrutura existente |
| Pilha | `push_pilha`, `pop_pilha`, `show_pilha` | Inserir, remover e mostrar |
| Fila | `push_fila`, `pop_fila`, `show_fila` | Inserir, remover e mostrar |
| Fila circular | `push_circular`, `pop_circular`, `show_circular` | Inserir, remover e mostrar, com `%` |
| Impressão | `imprimir_conteudo` | Mostra valores, vetor interno e ponteiros |
| Ordenação | `ordenacao_bolha`, `ordenacao_selecao`, `ordenacao_insercao` | Os três algoritmos |
| Ponte | `obter_elementos`, `gravar_elementos`, `aplicar_ordenacao` | Liga a estrutura ativa aos algoritmos |
| Menus | `menu_principal`, `menu_estrutura`, `menu_ordenar` | Interface com o usuário |
| Início | `main` | Laço do menu principal |

Detalhe de projeto: `menu_estrutura` é **um submenu único** reutilizado pelas três estruturas. Ele recebe como parâmetros o nome e as funções de `push` e `pop` de cada uma, evitando repetir o mesmo código três vezes.

---

## Correções feitas nos exemplos de aula

Os arquivos de exemplo foram executados antes da integração. Estes problemas foram encontrados e corrigidos:

| Arquivo original | Problema | Correção |
|---|---|---|
| `Estrutura_pilha.py` | `MAX` era definido **dentro** de `inicializa()` sem `global`, causando `NameError` no primeiro `push` (confirmado em teste) | O tamanho agora é uma variável global definida na criação, escolhida pelo usuário |
| `Estrutura_fila.py` | Tamanho fixo (`MAX = 5`) e vetor crescendo com `append` | Tamanho definido pelo usuário e vetor `dados` pré-alocado |
| `Fila_Circular.py` | A mensagem de fila **cheia** dizia "Fila Vazia!!"; o teste de vazio/cheio por `None` e `rpos == MAX` podia gerar índice fora do vetor | Uso de `%` e da contagem `qtd` para vazio/cheio; mensagens corretas |
| `Exemplo_menu.py` | Havia `return` dentro do `while`, então o menu executava **uma única vez** e as opções só imprimiam texto | Laços corrigidos e cada opção chama a função real |
| `Bubble_Sort.py` | Percorria sempre `n-1` posições, mesmo as já ordenadas | Reduz o intervalo a cada volta e para cedo se não houver trocas |
| Vários | Testes soltos no fim dos arquivos (ex.: `input()` na fila circular) | Removidos; tudo parte do menu |

`Insertion_Sort.py` e `Selection_Sort.py` já estavam corretos e foram mantidos praticamente iguais.

## Limitações conhecidas

- **Só aceita números inteiros** como valores (para que a ordenação sempre funcione).
- **Uma estrutura ativa por vez:** criar outra apaga a atual.
- **Fila simples não reaproveita posições** já removidas (comportamento do modelo; use a fila circular para isso).
- Os dados ficam **somente na memória**: ao fechar o programa, tudo é perdido.
- Ainda não há testes automatizados no repositório.

## Estrutura do repositório

```
.
├── estruturas_ordenacao.py   # programa completo
└── README.md                 # este arquivo
```
