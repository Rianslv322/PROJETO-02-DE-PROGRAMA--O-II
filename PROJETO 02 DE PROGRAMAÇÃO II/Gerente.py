import json
from Funcionario import *
# from Folha_de_pagameto import *

class Gerente(Funcionario):
    dados = "Arquivo.json"
    def __init__(self, nome, cpf, idade, cargo, salario_base, descontos, senha):
        super().__init__(nome, cpf, idade, cargo, salario_base, descontos)
        self.senha = senha
        self.lista_F= []




    def cadastrar_funcionario(self, nome, cpf, idade, cargo, salario_base, descontos):
        funcionario = Funcionario(nome,cpf,idade,cargo,salario_base,descontos)
        self.lista_F.append(funcionario)
        print("Funcionário cadastrado.")

      
    def Salvar_Dados(self):
        try:
        # Tenta carregar os dados existentes
            with open(self.dados, "r", encoding="utf-8") as f:
                lista = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # Se o arquivo não existir ou estiver vazio, começa com uma lista vazia
            lista = []
            
            
        

        # Adiciona os novos funcionários
        for x in self.lista_F:
            ja_existe = False
            lista.append(x.salvar())
            
            for func in lista:
                if func["Cpf"] == x.cpf:
                    ja_existe = True
                    break
                
            if not ja_existe:
                lista.append(x.salvar())

        # Salva tudo de uma vez
        with open(self.dados, "w", encoding="utf-8") as f:
            json.dump(lista, f, indent=4, ensure_ascii=False)

        print("Dados salvos.")


    @property
    def editar_Funcionario(self):
        while True:
            print("""
        [1] Editar Nome    
        [2] Editar Cargo
        [3] Editar Salário
        [4] Sair
        """)
            opcao = input("Opçao aqui --> ")

            nome = input("Digite o Nome do Funcnionário --> ")
            
            for func in self.lista_F:
                if func.nome == nome:
                    if opcao == "1":
                        novo_nome = input("Novo Nome: ")
                        self.nome = novo_nome
                        print(f"Nome alterado.")

                    if opcao == "2":
                        novo_cargo  = input("Novo Cargo: ")
                        self.cargo = novo_cargo
                        print(f"Cargo alterado.")

                    
                    if opcao == "3":
                        novo_salario = float(input("Novo salário: "))
                        self.salario = novo_salario
                        print("Salário alterado.")

                    
                    if opcao == "4":
                        print("Todas as alterações foram concluidas.")
                        break
             
                    else:
                        return f"Funcnionário não encontrado"

                self.Salvar_Dados()
            break
                        
    @property
    def remover_funcionario(self):
        nome = str(input("Nome do Funcionário: "))
        
        for posi,func in enumerate(self.lista_F):
            if nome == func.nome:
                del self.lista_F[posi]
                print("Funcionário Demitido.")
                break   
                
                
    @property
    def listar_funcionarios(self):
        print("++ LISTA DE FUNCIONÁRIO ++")
        for x in self.lista_F:
            print(x.mostrar_dados_funcionario())
            
    
    def gerar_folha_de_pagamento(self):
        for x in self.lista_F:
            print(x.calcular_salario())


                
            



Gerente_geral_da_Empresa = Gerente("Rian Silva", "123.321-678-45", 29, "Gerente", 6000, 600, 123)
# Gerente_geral_da_Empresa.cadastrar_funcionario("Ana", "741-852", 26, "TI", 5000, 600)






