import json
from Funcionario import *

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
        self.Salvar_Dados()

    #class para atualizar dados json e transformar de volta em dict\lista
    def Atualizar_dados(self, dados, novo_dado, tipo):
        try:
        # carrega os dados existentes
            with open(self.dados, "r", encoding="utf-8") as f:
                lista = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # Se o arquivo não existir ou estiver vazio, começa com uma lista vazia
            lista = []

        for i, x in enumerate(lista):
            if x[f"{tipo}"] == dados[f"{tipo}"]:
                dados[f"{tipo}"] = novo_dado                    
                lista[i] = dados 
                break

        # Salva tudo de uma vez
        with open(self.dados, "w", encoding="utf-8") as f:
            json.dump(lista, f, indent=4, ensure_ascii=False)
        print("Dados salvos.")
        
    #class para salvar dados no json
    def Salvar_Dados(self):
        try:
            with open(self.dados, "r", encoding="utf-8") as f:
                lista = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            lista = []

    
        # Adiciona os novos funcionários
        for x in self.lista_F:
            ja_existe = False
            for func in lista:
                if func["Nome"] == x.nome:
                    ja_existe = True
                    break
                
            if not ja_existe:
                lista.append(x.salvar())
        # Salva tudo de uma vez
        with open(self.dados, "w", encoding="utf-8") as f:
            json.dump(lista, f, indent=4, ensure_ascii=False)
        print("Dados salvos.")
        
    
    def carregar_dados(self):
        self.lista_F = [] 
        """Carrega os dados do arquivo JSON e recria os objetos Funcionario."""
        try:
            with open(self.dados, "r", encoding="utf-8") as f:
                lista = json.load(f)
                for func in lista:
                    funcionario = Funcionario(
                        func["Nome"],
                        func["Cpf"],
                        func["Idade"],
                        func["Cargo"],
                        func["Salario"],
                        func["Desconto"]
                    )
                    self.lista_F.append(funcionario)
    
        except (FileNotFoundError, json.JSONDecodeError):
            print("Nenhum dado anterior encontrado.")


    @property
    def editar_Funcionario(self):
        self.carregar_dados()
        linha()
        while True:
            print("""
            [1] Editar Nome    
            [2] Editar Cargo
            [3] Editar Salário
            [4] Sair
            """)
            opcao = input("Opção aqui --> ")

            if opcao == "4":
                print("Saindo da edição...")
                break
            
            encontrado = False

            for func in self.lista_F:
                nome = input("Digite o Nome do Funcionário --> ")
                if func.nome == nome:
                    encontrado = True
                    if opcao == "1":  
                        tipo_dado = "Nome"
                        novo_dado = input("Novo Nome: ")
                        print("Nome alterado.")

                    if opcao == "2":
                        novo_dado = input("Novo Cargo: ")
                        tipo_dado = "Cargo"

                        print("Cargo alterado.")

                    if opcao == "3":
                        novo_dado = float(input("Novo salário: "))
                        tipo_dado = "Salario"

                        print("Salário alterado.")

                    dicio = func.salvar()
                    self.Atualizar_dados(dicio, novo_dado, tipo_dado)
                    
                    break
            linha()
            if not encontrado:
                print("Funcionário não encontrado.")
        linha()

                        

    def remover_funcionario(self):
        self.carregar_dados()
        linha()
        nome = str(input("Nome do Funcionário: "))
        encontrado = False
        for func in self.lista_F:
            if func.nome == nome:
                self.lista_F.remove(func)
                encontrado = True
                print("Funcionário Demitido.")
                break   
                
        linha()  
        if encontrado:
            nova_lista = []
            for i in self.lista_F:
                dados_func = i.salvar()
                nova_lista.append(dados_func)
                
                
            with open(self.dados,"w", encoding="UTF-8") as arquivo:
                json.dump(nova_lista,arquivo,indent=4, ensure_ascii= False)
                
        else:
            print("Funcionário não encontrado")

    def listar_funcionarios(self):
        self.carregar_dados()
        linha()
        print("++ LISTA DE FUNCIONÁRIO ++")
        for x in self.lista_F:
            print(x.mostrar_dados_funcionario())
        linha()
            
            


