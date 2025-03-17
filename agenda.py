"""Projeto agenda de contatos."""

# Criação da função principal (exibir_menu)
def exibir_menu():
    print('\n--- Agenda de Contatos ---')
    print('1. Adicionar contato')
    print('2. Listar contatos')
    print('3. Editar contato')
    print('4. Marcar/desmarcar contato como favorito')
    print('5. Listar favoritos')
    print('6. Remover contato')
    print('0. Sair')
    print()

# Função auxiliar para obter o índice do usuário
def obter_indice(contatos, mensagem):
    """Exibe os contatos e solicita um índice válido."""
    listar_contatos(contatos)
    try:
        indice = int(input(mensagem)) - 1
        if 0 <= indice < len(contatos):
            return indice
        print('Índice inválido.')
    except ValueError:
        print('Entrada inválida. Digite um número válido.')
    return None

# Função auxiliar para obter o primeiro nome
def primeiro_nome(nome):
    """Retorna apenas o primeiro nome de uma string."""
    return nome.split(" ")[0] if nome else ""

# Criação da função adicionar_contato
def adicionar_contato(contatos):
    """Adiciona um novo contato à agenda."""
    nome = input('Nome: ')
    telefone = input('Telefone: ')
    email = input('Email: ')
    contatos.append({'nome': nome, 'telefone': telefone, 'email': email, 'favorito': False})
    print(f'\nContato de {primeiro_nome(nome)} adicionado com sucesso!')

# Criação da função listar_contatos
def listar_contatos(contatos, apenas_favoritos=False):
    """Exibe a lista de contatos, com opção de filtrar apenas favoritos."""
    contatos_filtrados = contatos if not apenas_favoritos else [c for c in contatos if c['favorito']]
    
    if not contatos_filtrados:
        print('Nenhum contato encontrado.' if not apenas_favoritos else 'Nenhum contato favorito.')
        return
    
    print('\n--- LISTA DE CONTATOS ---' if not apenas_favoritos else '\n--- CONTATOS FAVORITOS ---')
    for i, contato in enumerate(contatos):
        if not apenas_favoritos or contato['favorito']:
            fav = '⭐' if contato['favorito'] else ''
            print(f"{i+1}. {contato['nome']} - {contato['telefone']} - {contato['email']} {fav}")

# Criação da função editar_contato
def editar_contato(contatos):
    """Permite editar um contato pelo índice."""
    if not contatos:
        print('Nenhum contato cadastrado.')
        return
    
    indice = obter_indice(contatos, 'Digite o índice do contato que deseja editar: ')
    if indice is not None:
        contatos[indice]['telefone'] = input('Novo telefone: ')
        contatos[indice]['email'] = input('Novo email: ')
        print(f'Contato de {primeiro_nome(contatos[indice]["nome"])} atualizado com sucesso!')

# Criação da função marcar_favorito
def marcar_favorito(contatos):
    """Alterna o status de favorito pelo índice."""
    if not contatos:
        print('Nenhum contato cadastrado.')
        return

    indice = obter_indice(contatos, 'Digite o índice do contato que deseja favoritar ou desfavoritar: ')
    if indice is not None:
        contatos[indice]['favorito'] = not contatos[indice]['favorito']
        status = 'favorito' if contatos[indice]['favorito'] else 'NÃO favorito'
        print(f'Contato de {primeiro_nome(contatos[indice]["nome"])} agora está marcado como {status}.')

# Criação da função listar_favoritos
def listar_favoritos(contatos):
    """Lista apenas os contatos favoritos."""
    listar_contatos(contatos, apenas_favoritos=True)

# Criação da função remover_contato
def remover_contato(contatos):
    """Remove um contato pelo índice."""
    if not contatos:
        print('Nenhum contato cadastrado.')
        return
    
    indice = obter_indice(contatos, 'Digite o índice do contato que deseja remover: ')
    if indice is not None:
        contato_removido = contatos.pop(indice)
        print(f'Contato de {primeiro_nome(contato_removido["nome"])} removido com sucesso!')

# Criação da função principal (main)
def main():
    """Gerencia o loop principal do programa."""
    contatos = []
    
    opcoes = {
        '1': adicionar_contato,
        '2': listar_contatos,
        '3': editar_contato,
        '4': marcar_favorito,
        '5': listar_favoritos,
        '6': remover_contato,
    }
    
    while True:
        exibir_menu()
        opcao = input('Escolha uma opção: ')
        
        if opcao == '0':
            print('\nSaindo... Até logo!')
            break
        elif opcao in opcoes:
            opcoes[opcao](contatos)
        else:
            print('\nOpção inválida, tente novamente.')

if __name__ == '__main__':
    main()