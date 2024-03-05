# Criador         : Brayan vieira 
# função          : Um sistema de gerenciamento de gastos 
# versão          : 1.0
# data da criação : 04/03/2024
import os
import platform

# Definindo o caminho do arquivo onde os gastos serão armazenados
caminho_do_arquivo = "compras.txt"

# Mensagens para o usuário
qualquer_tecla = " \n Insira qualquer Tecla para continuar \n \n Insira : "

# Banner para o menu principal
banner = '''
 ___________________________________________________________
|                                                          |
|     $$$$$$\  $$\   $$\ $$$$$$$$\ $$$$$$$\  $$\   $$\     |
|    $$  __$$\ $$ |  $$ |$$  _____|$$  __$$\ $$ |  $$ |    |
|    $$ /  $$ |$$ |  $$ |$$ |      $$ |  $$ |$$ |  $$ |    |
|    $$ |  $$ |$$ |  $$ |$$$$$\    $$ |  $$ |$$ |  $$ |    |
|    $$ |  $$ |$$ |  $$ |$$  __|   $$ |  $$ |$$ |  $$ |    |
|    $$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |$$ |  $$ |    |
|     $$$$$$  |\$$$$$$  |$$ |      $$$$$$$  |\$$$$$$  |    |
|     \______/  \______/ \__|      \_______/  \______/     |
|                                                          |
|                  Gerencie suas finanças                  |
|               Controle seus gastos e compras             |
|__________________________________________________________|
                
    Menu de comandos :

    [ Add ] Adiciona novos gastos no registro

    [ Del ] Apaga todos os gastos 

    [ See ] Mostra todos os gastos e compras 
                

    Insira um comando para continuar : '''

# Função para limpar a tela do console de acordo com o sistema operacional
def limpador():
    sistema_operacional = platform.system()
    if sistema_operacional == "Windows":
        limpador = "cls"
    elif sistema_operacional == "Linux" or sistema_operacional == "Mac":
        limpador = "clear"
    return os.system(limpador)

# Função para inserir gastos no arquivo
def inserir_gastos():
    limpador()
    print(" \n \n Insira as informações dos seus gastos : \n \n  ")
    try :
        gasto1 = int(input("insira o valor da compra : "))
    except ValueError:
        limpador()
        print("Erro \n \n Insira somente numeros \n ")
        return exit()
    if gasto1 <= 0:
         limpador()
         print(" \n \n Erro \n \n Insira um valor maior que 0  \n")
         exit ()
    data_compra = input(" \n Insira a data da compra : ")
    compra = input(" \n Oq você comprou ? : ")
    with open(caminho_do_arquivo,"a", encoding="utf-8") as arquivo1:
                arquivo1.write(f"Item comprado : {compra} \n ")
                arquivo1.write(f"Gasto : {gasto1} \n")
                arquivo1.write(f"Data da compra : {data_compra} \n")
                arquivo1.write("\n")
    limpador()
    return print(" \n Gasto adicionado com sucesso \n ")

# Função para mostrar todos os gastos e calcular o total
def mostrar_gastos():
    total = 0.0
    limpador()
    with open(caminho_do_arquivo, "r", encoding="utf-8") as gastos_totais:
        for linhas in gastos_totais:
            print(f" \n{linhas}")
            if "Gasto" in linhas:
                indice, linhas = linhas.split(":")
                calculo = linhas 
                total += float(calculo)    
        if total == 0.0:
            print(" \n Você não tem compras registradas \n ")
        return print(f"O seu gasto total e : {total:.2f} R$ \n ")

# Função para redefinir o arquivo de gastos
def redefinir_arquivo():
     limpador()
     certeza = input("Você têm certeza que deseja apagar Tudo ?\n \n[S] sim | [N] não \n \n Insira : ").lower().startswith("n")
     if certeza:
        print(" \n \n Operação cancelada \n \n Saindo..... \n ")
        return input(qualquer_tecla)
     with open(caminho_do_arquivo, "w")as arquivo:
        limpador()
        arquivo.write("\n")
     print("\n Compras limpas com sucesso! \n")
     return input(qualquer_tecla)

# Tentativa de abrir o arquivo de gastos. Se não existir, ele é criado.
try : 
    with open(caminho_do_arquivo, "r+") as arquivo:
        arquivo.write("\n")
except FileNotFoundError:
    with open(caminho_do_arquivo, "w") as arquivo:
        arquivo.write("\n")

# Loop principal para exibir o menu e processar os comandos
while True:
    limpador()
    input_do_menu = input(banner).lower()
    match input_do_menu:
        case "add":
            limpador()
            inserir_gastos()
            input(qualquer_tecla)
        case "del":
            redefinir_arquivo()
        case "see":
            limpador()
            mostrar_gastos()
            input(qualquer_tecla)
        case _:
            limpador()
            print("Você inseriu algo inválido \n ")
            input(qualquer_tecla)
