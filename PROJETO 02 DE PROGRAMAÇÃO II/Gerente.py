import json
from Funcionario import *

class Gerente(Funcionario):
    dados = "Arquivo.json"
    def __init__(self, nome, cpf, idade, cargo, salario_base, descontos, senha):
        super().__init__(nome, cpf, idade, cargo, salario_base, descontos)
        self.senha = senha
        self.lista_F= []
        self.funcionario = Funcionario(nome, cpf, idade, cargo, salario_base, descontos)
        self.lista_F.append(self.funcionario)
        
        
    def cadastrar_funcionario(self, nome, cpf, idade, cargo, salario_base, descontos):
        self.funcionario = Funcionario(nome,cpf,idade,cargo,salario_base,descontos)
        novo_func = self.funcionario
        self.lista_F.append(novo_func)
        print("Funcionário cadastrado.")
    
    
    
        
    def salvar(self):
    # Tenta ler o arquivo existente
        try:
            with open(self.dados, "r", encoding="utf-8") as f:
                lista = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError): #ocorre se o arquivo indicado por self.dados não existe. respectivamente 
            lista = []

        # Adiciona os novos funcionários
        for x in self.lista_F:
            lista.append({
                "nome": x.nome,
                "cpf": x.cpf,
                "idade": x.idade,
                "cargo": x.cargo,
                "salario": x.salario,
                "desconto": x.descontos
            })

        # Salva tudo de uma vez
        with open(self.dados, "w", encoding="utf-8") as f:
            json.dump(lista, f, indent=4, ensure_ascii=False)

        print("Dados salvos.")



    def editar_Funcionario(self):
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
            
        
    def remover_funcionario(self):
        nome = str(input("Nome do Funcionário: "))
        
        for posi,func in enumerate(self.lista_F):
            if nome in func.listar_dados().values():
                del self.lista_F[posi]
                print("Funcionário Demitido.")
                
                
                
    def listar_funcionarios(self):
        print("++ LISTA DE FUNCIONÁRIO ++")
        for x in self.lista_F:
            print(x.mostrar_dados_funcionario())

                
            


gerente1 = Gerente("Rianlindao", "123213-213", 29, "Gerente", 6000, 600, 123)

gerente1.cadastrar_funcionario("Maria Souza", "987654-321", 34, "Vendas", 5800, 550)
gerente1.cadastrar_funcionario("Carlos Silva", "456789-123", 41, "TI", 7200, 800)

# gerente1.salvar()
# gerente1.remover_funcionario()
# gerente1.salvar()





