
import json
from Pessoa_Funcionario import *

class Gerente(Funcionario):
    def __init__(self, nome, cpf, idade, cargo, salario_base, descontos,senha):
        super().__init__(nome, cpf, idade, cargo, salario_base, descontos)
        self.senha = senha
        self.lista_funcionario = []

    
    def mostrar_dados(self):
        print(f"""
        Nome: {self.nome}
        CPF: {self.cpf}
        Idade: {self.idade}
        Cargo: {self.cargo}
        Salário: {self.salario}
        Desconto: {self.descontos}
        Senha: {self.senha}""")

    def cadastrar_funcionaio(self, nome, cpf, idade, cargo, salario_base, descontos):
        novo_funcionario = Funcionario(nome,cpf,idade,cargo,salario_base,descontos)
        self.lista_funcionario.append(novo_funcionario)
        return "Novo funcionário Cadastrado"


    def editar_informaces(self):
        print("""
        [1] Editar Nome    
        [2] Editar Cargo
        [3] Editar Salário
""")
        
        opcao = input("Opçao aqui --> ")


        if opcao == "1":
            novo_nome = input("Novo Nome: ")
            self.nome = novo_nome
            return f"Nome alterado."

        if opcao == "2":
            novo_cargo  = input("Novo Cargo: ")
            self.cargo = novo_cargo
            return f"Cargo alterado."
        
        if opcao == "3":
            novo_salario = float(input("Novo salário: "))
            self.salario = novo_salario
            return "Salário alterado."

    

    def salvar_json(self,arquivo):
        lista = []
        for x in self.lista_funcionario:
            lista.append(x.mostrar_dados())

        with open(arquivo,"w",encoding="UTF-8") as dados:
            json.dump(lista,dados,indent=4,ensure_ascii=False)

        print(f"Dados salvos com sucesso em {arquivo}")

    
gerente1 = Gerente("Rian","123213-213",29,"Gerente",6000,600,123)
gerente1.cadastrar_funcionaio("Rian","13213-321321-321321",22,"Gestor",6000,200)
gerente1.editar_informaces()
gerente1.mostrar_dados()




