import os

restaurantes = [{'nome': 'The Bear', 'categoria': 'italiana', 'ativo': True}, 
                {'nome': 'Mario pizzas', 'categoria': 'pizzaria', 'ativo': False},
                {'nome': 'sushi-man', 'categoria': 'japonesa', 'ativo': False}
]

def exibir_nome_programa():
    print('''
        
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    ''');

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair \n')

def finalizar_app():
    
    exibir_subtitulo('Encerrando programa....') 

def opcao_invalida():
    print('Opção inválida!\n')

    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto) )

    print(linha)    
    print(texto)
    print(linha)
    print()


def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def cadastrar_novo_restaurante():
   
    exibir_subtitulo('Cadastro de novo restaurante')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'{nome_do_restaurante} foi cadastrado com sucesso\n')

    voltar_ao_menu_principal()

def listar_restaurantes():
    
    exibir_subtitulo('Listando restaurantes')

    print(f'{'Nome do restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | Status\n')
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = f'Ativado' if restaurante['ativo'] else f'Desativado'
        print(f' - {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()


def alterar_estado_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')

    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

    # match opcao_escolhida:
    #     case 1:
    #         print('Cadastrar restaurante\n')
    #     case 2:
    #         print('Listar restaurante\n')
    #     case 3:
    #         print('Ativar restaurante\n')
    #     case 4:
    #         finalizar_app()
    #     case _:
    #         print('Opção inválida!!')

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
