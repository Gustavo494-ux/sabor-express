import os

restaurantes = [
    {'nome':'Praça','categoria':'Japonesa','ativo':False},
    {'nome':'Pizza Suprema','categoria':'Pizza','ativo':True},
    {'nome':'Cantina','categoria':'Italiano','ativo':False}]

def exibir_nome_do_programa():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair restaurante\n')

def finalizar_app():
    exibir_subtitulo('Finalizar app')

def opcao_invalida():
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def excolher_opcoes():
    try:
        opcaoEscolhida = int(input('Escolha uma opção: '))

        match opcaoEscolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes_cadastrados()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()
       
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    
    restaurantes.append({'nome':nome_do_restaurante, 'categoria':categoria_do_restaurante, 'ativo':False})

    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_do_restaurante  = input('Digite o nome do restaurante que deseja: ')

    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = (f'O resturante {nome_do_restaurante} foi ativado com sucesso' 
            if restaurante['ativo'] else f'O resturante {nome_do_restaurante} fopi desativado com sucesso')
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_ao_menu_principal()


def listar_restaurantes_cadastrados():
    exibir_subtitulo('Listanto os restaurantes')

    print(f' {"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')
    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['nome']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f' - {nome.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)

def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    excolher_opcoes()

if __name__ == '__main__':
    main()