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




    def editar_informaces(self):
        while True:
            print("""
        [1] Editar Nome    
        [2] Editar Cargo
        [3] Editar Salário
        [4] Sair
        """)
            opcao = input("Opçao aqui --> ")

            if opcao == "1":
                novo_nome = input("Novo Nome: ")
                self.nome = novo_nome
                print(f"Nome alterado.")
                self.salvar()

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

          


gerente1 = Gerente("Rianlindao", "123213-213", 29, "Gerente", 6000, 600, 123)
# gerente2 = Gerente("Maria Souza", "987654-321", 34, "Gerente de Vendas", 5800, 550, 456)
# gerente3 = Gerente("Carlos Silva", "456789-123", 41, "Gerente de TI", 7200, 800, 789)
# gerente4 = Gerente("Ana Oliveira", "321654-987", 27, "Gerente de Projetos", 6500, 500, 321)
# gerente5 = Gerente("Lucas Pereira", "654321-789", 38, "Gerente Financeiro", 7000, 700, 654)


gerente1.editar_informaces()

print(gerente1.mostrar_dados())




