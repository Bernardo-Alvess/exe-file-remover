#TODO - Adicionar remoção expressa de arquivos

import os

print("Este script tem a função de deletar os arquivos .exe dentro de uma pasta")

# Função que é responsável por remover os arquivos .exe de dentro da pasta designada
def remove_exe_files(dir):
    for file in os.listdir(dir):
        if file.endswith(".exe"):
            print(f"Deletando {file}")
            os.remove(f"{dir}\{file}")

#Função para encontrar os arquivos .exe dentro da pasta e mostrar os arquivos
def executable_file_presence(dir, mode):

    hasFiles = False
    files = 0

    if mode == 1:
        for file in os.listdir(dir):
            if file.endswith(".exe"):
                hasFiles = True

    elif mode == 2:
        for file in os.listdir(dir):
            if file.endswith(".exe"):
                print(file)
                files += 1

    return hasFiles, files

#Função responsável por lidar com as escolhas das pastas do usuário e confirmação da remoção de arquivos
def exe_remover(op):

    #Remove os arquivos .exe de dentro da pasta atual
    if op == 1:
        dir = os.getcwd()

    #Remove os arquivos .exe de outra pasta
    elif op == 2:
        dir = input("Local da pasta: ")
        while not os.path.isdir(dir):
            print("Pasta inexistente")
            dir = input("Local da pasta: ")

    print(f"Os arquivos serão deletados da pasta: {dir}")
    print("Verificando a presença de arquivos")

    #Verifica se tem algum arquivo .exe dentro da pasta, se houver retorna True
    if executable_file_presence(dir, 1)[0]:
        print("Arquivos encontrados")

        print(f"Total de {executable_file_presence(dir, 2)[1]} arquivo(s) .exe")
        
        op_final = 0

        while op_final != 1 and op_final != 2 and op_final != 3:
            print("Tem certeza de que deseja deletar estes arquivos?")
            print("1 - Sim")
            print("2 - Não")
            print("3 - Selecionar outra pasta")

            op_final = int(input())

            if op_final != 1 and op_final != 2 and op_final != 3:
                print("Opção inválida. Tente novamente")

        #Remove os arquivos
        if op_final == 1:
            remove_exe_files(dir)

        elif op_final == 3:
            delete_files_program()

    else:
        print("Nenhum arquivo .exe encontrado")

        #Imitação de uma estrutura do while em python
        while True:
            print("Deseja selecionar outra pasta?")
            print("1 - Sim")
            print("2 - Não")
            
            op = int(input())

            if op == 1:
                delete_files_program()
                break;

            elif op == 2:
                break;

            else:
                print("Opção inválida")

#Função mãe - responsável por rodar o script
def delete_files_program():
    while True:
        print("1 - Deletar arquivos .exe presentes nesta pasta")
        print("2 - Deletar arquivos .exe de outra pasta")
        op = int(input())
        
        if op == 1 or op == 2:
            break;
        else:
            print("Opção inválida")

    exe_remover(op)
    
delete_files_program()


print("Aperte qualquer tecla para fechar o terminal")
input()