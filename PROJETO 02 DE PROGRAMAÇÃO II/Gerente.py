import json
from Pessoa_Funcionario import *

class Gerente(Funcionario):
    def __init__(self, nome, cpf, idade, cargo, salario_base, descontos, senha):
        super().__init__(nome, cpf, idade, cargo, salario_base, descontos)
        self.senha = senha
        self.lista_funcionario = []
        self.funcionario = Funcionario(nome, cpf, idade, cargo, salario_base, descontos)
        self.lista_funcionario.append(self.funcionario)
        self.salvar()

    def mostrar_dados(self):
        return {
            "Nome": self.nome,
            "CPF": self.cpf,
            "Idade": self.idade,
            "Cargo": self.cargo,
            "Salário": self.salario,
            "Desconto": self.descontos,
            "Senha": self.senha
        }

    def salvar(self):
        lista = []
        for x in self.lista_funcionario:
            lista.append(x.mostrar_dados()) 
        with open("arquivo.json", "w", encoding="UTF-8") as dados:
            json.dump(lista, dados, indent=4, ensure_ascii=False)

        print("Dados salvos.")

        

gerente1 = Gerente("Rianlindao","123213-213",29,"Gerente",6000,600,123)

gerente1.salvar() 


    # def salvar_json(self,arquivo):
    #     lista = []
    #     for x in self.lista_funcionario:
    #         lista.append(x.mostrar_dados())

    #     with open(arquivo,"w",encoding="UTF-8") as dados:
    #         json.dump(lista,dados,indent=4,ensure_ascii=False)

    #     print(f"Dados salvos com sucesso em {arquivo}")



        # def cadastrar_funcionaio(self, nome, cpf, idade, cargo, salario_base, descontos):
        # novo_funcionario = Funcionario(nome,cpf,idade,cargo,salario_base,descontos)
        # self.lista_funcionario.append(novo_funcionario)

        # lista = []
        # for x in self.lista_funcionario:
        #     lista.append(x.mostrar_dados())

        # with open("arquivo.json","w",encoding="UTF-8") as dados:
        #     json.dump(lista,dados,indent=4,ensure_ascii=False)

        # print(f"Dados salvos.")


        #parti pronta daqui pra baixo


#     def editar_informaces(self):
#         print("""
#         [1] Editar Nome    
#         [2] Editar Cargo
#         [3] Editar Salário
#         [4] Sair
# """)
#         while True:
#             opcao = input("Opçao aqui --> ")


#             if opcao == "1":
#                 novo_nome = input("Novo Nome: ")
#                 self.nome = novo_nome
#                 return f"Nome alterado."

#             if opcao == "2":
#                 novo_cargo  = input("Novo Cargo: ")
#                 self.cargo = novo_cargo
#                 return f"Cargo alterado."
            
#             if opcao == "3":
#                 novo_salario = float(input("Novo salário: "))
#                 self.salario = novo_salario
#                 return "Salário alterado."
            
#             if opcao == "4":
#                 return "Todas as alterações foram concluidas."
#                 break










