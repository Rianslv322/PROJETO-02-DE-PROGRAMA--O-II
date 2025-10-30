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
[5] Gerar Folha de Pagamento(funcionário)
[6] Acessar Dados do Funcionário
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
        folhadepagar.gerente.Salvar_Dados()

    if opcao == 1:
        folhadepagar.gerente.cadastrar_funcionario
        
    if opcao ==2:
        folhadepagar.gerente.editar_Funcionario
        
        
    if opcao == 3:
        folhadepagar.gerente.remover_funcionario
        
        
    if opcao == 4:
        folhadepagar.gerente.listar_funcionarios
        
        
    # if opcao == 5:
    #     folhadepagar.gerente.gerar_folha_de_pagamento()
        
        
        
    
        
        