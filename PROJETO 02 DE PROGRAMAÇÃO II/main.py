from Gerente import *
from  Funcionario import *
from Folha_de_pagameto import *


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
        

    if opcao == 1:
        folhadepagar.gerente.cadastrar_funcionario
        
    if opcao ==2:
        folhadepagar.gerente.editar_Funcionario()
        
        
    if opcao == 3:
        folhadepagar.gerente.remover_funcionario
        
        
    if opcao == 4:
        folhadepagar.gerente.listar_funcionarios
        
        
    if opcao == 5:
        folhadepagar.gerar_relatorio_individual()
        
    if opcao == 6:
        folhadepagar.gerar_relatorio()

    if opcao ==7:
        while True:
            print("\nMenu de Opções (Digite o número correspondente)")
            print("1 - Acessar Nome")
            print("2 - Acessar CPF")
            print("3 - Acessar Idade")
            print("4 - Acessar Cargo")
            print("5 - Acessar Salário Base")
            print("0 - Sair")

            op = int(input("Opção aqui --> "))


            if op == 1:
                for x in folhadepagar.gerente.lista_F:
                    print(f"Nome: {x.nome}")
                break
            elif op == 2:
                for x in folhadepagar.gerente.lista_F:
                    print(f"CPF: {x.cpf}")

            elif op == 3:
                for x in folhadepagar.gerente.lista_F:
                    print(f"CPF: {x.idade}")

            
    
        
        