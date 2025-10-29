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
        Gerente_geral_da_Empresa.cadastrar_funcionario(nome,cpf,idade,cargo,salario,descontos)
        Gerente_geral_da_Empresa.salvar()
        
    if opcao ==2:
        Gerente_geral_da_Empresa.editar_Funcionario
        
    if opcao == 3:
        Gerente_geral_da_Empresa.remover_funcionario
        
    if opcao == 4:
        Gerente_geral_da_Empresa.listar_funcionarios
        
        
    if opcao == 5:
        Gerente_geral_da_Empresa.gerar_folha_de_pagamento()
        
    Gerente_geral_da_Empresa.salvar()
        
    
        
        