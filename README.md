# 📒 Agenda de Contatos - Desafio Rocketseat 🚀  

Este repositório contém a implementação do **Desafio 01** do módulo **Introdução ao Python** da Rocketseat. O projeto consiste em uma **Agenda de Contatos** funcional no terminal, permitindo adicionar, editar, excluir e marcar contatos como favoritos.

## 📝 Sobre o Projeto  

A **Agenda de Contatos** é uma aplicação desenvolvida em Python para reforçar os conceitos básicos da linguagem. O usuário pode interagir com o sistema através de um menu no terminal, onde pode realizar diversas ações, como:

✅ **Adicionar um contato** com nome, telefone e e-mail.  
✅ **Listar todos os contatos** cadastrados com seus respectivos índices.  
✅ **Editar um contato** pelo índice.  
✅ **Marcar ou desmarcar um contato como favorito**.  
✅ **Listar apenas os contatos favoritos**.  
✅ **Remover um contato** pelo índice.  

O objetivo principal do projeto é praticar o uso de **listas**, **dicionários**, **funções** e **controle de fluxo em Python**, aplicando boas práticas de código.

## 📌 Tecnologias Utilizadas  

- **Python 3.10+**  
- Manipulação de **listas e dicionários**  
- Interação via **input/output no terminal**  
- Estruturas de controle **if, while e try/except**

## 🚀 Como Executar  

1️⃣ **Clone este repositório**  
```bash
git clone https://github.com/seu-usuario/agenda-contatos.git
```

2️⃣ **Acesse a pasta do projeto**  
```bash
cd agenda-contatos
```

3️⃣ **Execute o script no terminal**  
```bash
python agenda.py
```

💡 **Observação:** Certifique-se de ter o **Python 3.10+** instalado.

## 📌 Funcionalidades  

### ▶️ **1. Exibição do Menu Inicial**
Ao iniciar o programa, o menu será exibido no terminal para que o usuário escolha a ação desejada.

```
--- Agenda de Contatos ---
1. Adicionar contato
2. Listar contatos
3. Editar contato
4. Marcar/desmarcar contato como favorito
5. Listar favoritos
6. Remover contato
0. Sair
```

### 🆕 **2. Adicionar um Contato**
O usuário informa **Nome, Telefone e E-mail**, e o contato é salvo na agenda.

```
Nome: João Silva
Telefone: (11) 99999-9999
Email: joao@email.com
Contato de João adicionado com sucesso!
```

### 📋 **3. Listar Contatos**
Os contatos são exibidos numerados, e os favoritos são indicados com um **⭐**.

```
--- LISTA DE CONTATOS ---
1. Ana Souza - (21) 90000-0000 - ana@email.com
2. Carlos Lima - (31) 98888-8888 - carlos@email.com ⭐
```

### ✏️ **4. Editar um Contato**
O usuário escolhe o **índice** do contato para editar telefone e e-mail.

```
Digite o índice do contato que deseja editar: 1
Novo telefone: (21) 95555-5555
Novo email: ana.nova@email.com
Contato de Ana atualizado com sucesso!
```

### ⭐ **5. Marcar/Desmarcar Favorito**
O usuário escolhe o contato pelo **índice** e altera o status de favorito.

```
Digite o índice do contato que deseja favoritar ou desfavoritar: 2
Contato de Carlos agora está marcado como NÃO favorito.
```

### 📌 **6. Listar Favoritos**
Exibe apenas os contatos que estão marcados como favoritos.

```
--- CONTATOS FAVORITOS ---
1. Carlos Lima - (31) 98888-8888 - carlos@email.com ⭐
```

### 🗑️ **7. Remover um Contato**
O usuário seleciona o **índice** do contato a ser removido.

```
Digite o índice do contato que deseja remover: 1
Contato de Ana removido com sucesso!
```

## 📌 Estrutura do Código  

O projeto é composto pelas seguintes funções:

🔹 `exibir_menu()` → Exibe as opções do sistema.  
🔹 `adicionar_contato(contatos)` → Adiciona um novo contato.  
🔹 `listar_contatos(contatos, apenas_favoritos=False)` → Lista os contatos (com opção de exibir só favoritos).  
🔹 `editar_contato(contatos)` → Permite editar telefone e e-mail pelo índice.  
🔹 `marcar_favorito(contatos)` → Alterna o status de favorito.  
🔹 `listar_favoritos(contatos)` → Exibe apenas contatos favoritos.  
🔹 `remover_contato(contatos)` → Remove um contato pelo índice.  
🔹 `obter_indice(contatos, mensagem)` → Exibe contatos e pede um índice válido.  
🔹 `primeiro_nome(nome)` → Retorna apenas o primeiro nome.  

## 📌 Melhorias Implementadas  

✅ **Uso de índices para seleção de contatos**, tornando a navegação mais intuitiva.  
✅ **Validações de entrada** para evitar erros ao inserir índices inválidos.  
✅ **Exibição automática da lista de contatos** antes de editar, remover ou marcar como favorito.  
✅ **Código modularizado** com funções auxiliares para evitar repetição.  
✅ **Dicionário de opções no loop principal**, eliminando múltiplos `if/elif`.  

## 💡 Possíveis Melhorias Futuras  

🔹 Persistência dos contatos em **arquivo JSON** para manter os dados após o fechamento.  
🔹 Interface gráfica simples com **Tkinter** ou **PyQt**.  
🔹 Adicionar suporte a **busca de contatos** por nome.  

## 🏆 Conclusão  

Este projeto foi um excelente exercício para reforçar os fundamentos do **Python**, como manipulação de listas e dicionários, funções e controle de fluxo. Além disso, foi possível aplicar boas práticas de código e refatoração. 🚀  

## 📌 Autor  

👤 **Matheus Vaz**  
🔗 [Datacamp](https://www.datacamp.com/portfolio/matheusvazdata) | [LinkedIn](https://www.linkedin.com/in/matheusvazdata/)  