#Importa Biblioteca os que permite escrever no terminal
import os

restaurantes = [{'nome': 'The Bear', 'categoria': 'italiana', 'ativo': True}, 
                {'nome': 'Mario pizzas', 'categoria': 'pizzaria', 'ativo': False},
                {'nome': 'sushi-man', 'categoria': 'japonesa', 'ativo': False}
]

def exibir_nome_programa():
    '''Essa função exibe o titulo do programa'''
    print('''
        
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    ''');

def exibir_opcoes():
    '''Essa função exibe as opções que o cliente tem'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair \n')

def finalizar_app():
    '''Essa função exibe o encerramento do programa e o finaliza'''
    exibir_subtitulo('Encerrando programa....') 

def opcao_invalida():
    '''Essa função exibe Opção inválida e retorna ao menu principal'''
    print('Opção inválida!\n')

    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Essa função formata e exibe o subtitulo das opções'''
    os.system('cls')
    linha = '*' * (len(texto) )

    print(linha)    
    print(texto)
    print(linha)
    print()


def voltar_ao_menu_principal():
    '''Recebe um input qualquer para retornar ao menu principal'''
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def cadastrar_novo_restaurante():
    ''' Essa função é respónsavel por cadastrar um novo restaurante
    
    Inputs:
    Nome do restaurante
    Categoria do restaurante

    Outputs:
    Adiciona esses dados a lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de novo restaurante')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'{nome_do_restaurante} foi cadastrado com sucesso\n')

    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função exibe todos os restaurantes que temos na nossa lista
    
    Outputs:
    titulos 
    nome do restaurante
    categoria do restaurante
    Ativo ou não
    '''
    exibir_subtitulo('Listando restaurantes')

    print(f'{'Nome do restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | Status\n')
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = f'Ativado' if restaurante['ativo'] else f'Desativado'
        print(f' - {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()


def alterar_estado_restaurante():
    '''Essa função altera o estado do nosso restaurante de ativo para desativado e vice-versa
    
    Inputs:
    Nome do restaurante que será alterado

    Outputs:
    Altera o valor de ativo na lista no indice do restaurante selecionado
    '''
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
    '''Verifica a opção escolhida e retorna a função correspondente
        Verifica valores invalidos e manda para a função de opcao_invalida
    '''
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
    '''Função main do código que inicia as outras'''
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
