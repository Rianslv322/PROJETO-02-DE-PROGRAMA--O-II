from Gerente import *
from  Funcionario import *
from Folha_de_pagameto import *
import time


def menu_gerente():
    while True:
        print("====================================================")
        print("                LOGUIN(Gerente)                 ")
        print("====================================================")
        
        sair_entrar = input("""
            [1] para Entrar
            [0] para sair.
            """)
        print("====================================================")
        
        if sair_entrar == "0":
            break
        
        else:
            if sair_entrar == "1":
                Nome_gerente = str(input("Nome do Gerente Responsável: "))
                senha_gerente = str(input("Senha do Gerente Responsável: "))
                if Nome_gerente == folhadepagar.gerente.nome and senha_gerente == folhadepagar.gerente.senha:
                    print("Entrando no sistema...")
                    time.sleep(2)
                    print("Aguarde")
                    time.sleep(3)
                
        

        while True:
            print("========================================")
            print("        📋 SISTEMA DE GERENCIAMENTO      ")
            print("========================================")
            print("              MENU PRINCIPAL             ")
            print("========================================")
            
            print("""
        [1] Cadastrar Funcionário
        [2] Editar Dados Funcionário
        [3] Remover Funcioinário
        [4] Listar Funcionário 
        [5] Gerar Folha de Pagamento individual(funcionário) 
        [6] Gerar Relatório Geral 
        [7] Acessar Dados do Funcionário
        [0] Sair 
        """)
            
            opcao = int(input("Opção aqui --> "))
            if opcao ==1:
                nome  = str(input("Nome: "))
                cpf = str(input("CPF: "))
                idade = int(input("Idade: "))
                cargo = str(input("Cargo: "))
                salario = float(input("Salário: "))
                descontos = float(input("Desconto: "))
                folhadepagar.gerente.cadastrar_funcionario(nome,cpf,idade,cargo,salario,descontos)
            
            if opcao ==2:
                folhadepagar.gerente.editar_Funcionario
                
            if opcao == 3:
                folhadepagar.gerente.remover_funcionario() 
                
            if opcao == 4:

                folhadepagar.gerente.listar_funcionarios()
                
            if opcao == 5:
                folhadepagar.gerar_relatorio_individual()
                
            if opcao == 6:
                folhadepagar.gerar_relatorio()

            if opcao ==7:
                folhadepagar.gerente.carregar_dados()
                while True:
                    linha()
                    print("\nMenu de Opções (Digite o número correspondente)")
                    print("1 - Acessar Nome")
                    print("2 - Acessar CPF")
                    print("3 - Acessar Idade")
                    print("4 - Acessar Cargo")
                    print("5 - Acessar Salário Base")
                    print("0 - Sair")
                    linha()

                    op = int(input("Opção aqui --> "))

                    if op == 1:
                        for x in folhadepagar.gerente.lista_F:
                            print(f"Nome: {x.nome}")

                    elif op == 2:
                        for x in folhadepagar.gerente.lista_F:
                            print(f"CPF: {x.cpf}")

                    elif op == 3:
                        for x in folhadepagar.gerente.lista_F:
                            print(f"CPF: {x.idade}")

                    elif op == 4:
                        for x in folhadepagar.gerente.lista_F:
                            print(f"CPF: {x.cargo}")
                            
                    elif op == 5:
                        for x in folhadepagar.gerente.lista_F:
                            print(f"CPF: {x.salario}")
                            
                    elif op == 0:
                        print("Acesso encerrado.")
                        break   
                    
            if opcao == 0:
                break
                
def Menu_funcionario():         
    while True:
        print("====================================================")
        print("                LOGUIN(Funcionário)                 ")
        print("====================================================")
        Nome_Funcionario = str(input("Nome do Funcionário Responsável: "))
        cpf_funcionario = str(input("CPF do Funcionário Responsável: "))
        print("====================================================")
        for x in folhadepagar.gerente.lista_F:
            if Nome_Funcionario == x.nome and cpf_funcionario == x.cpf:
                while True:
                    linha()
                    print("\nMenu de Opções (Digite o número correspondente)")
                    print("1 - Acessar Nome")
                    print("2 - Acessar CPF")
                    print("3 - Acessar Idade")
                    print("4 - Acessar Cargo")
                    print("5 - Acessar Salário Base")
                    print("0 - Sair")
                    linha()

                    op = int(input("Opção aqui --> "))

                    if op == 1:
                        for x in folhadepagar.gerente.lista_F:
                            print(f"Nome: {x.nome}")

                    elif op == 2:
                        for x in folhadepagar.gerente.lista_F:
                            print(f"CPF: {x.cpf}")

                    elif op == 3:
                        for x in folhadepagar.gerente.lista_F:
                            print(f"CPF: {x.idade}")

                    elif op == 4:
                        for x in folhadepagar.gerente.lista_F:
                            print(f"CPF: {x.cargo}")
                            
                    elif op == 5:
                        for x in folhadepagar.gerente.lista_F:
                            print(f"CPF: {x.salario}")
                            
                    elif op == 0:
                        print("Acesso encerrado.")
                        break


for x in range(6,0,-1):
    print("====================================================")
    cargo_1 = str(input("Digite seu Cargo: ")).lower()
    if x ==2:
        print("Você só tem mais uma tentativa.")
    if cargo_1 == "gerente":  
        print("carregando...")  
        time.sleep(3)    
        menu_gerente()
        
    elif cargo_1 == "funcionario":
        print("Entrando no menu de Funcionário")
        time.sleep(3)
        Menu_funcionario()
        
    else:
        print("Nome do cargo incorreto.")