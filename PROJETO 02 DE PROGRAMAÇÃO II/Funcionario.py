def linha():
    print("=-"*18)
        


class Funcionario():
    def __init__(self, nome, cpf, idade,cargo,salario_base,descontos):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.cargo = cargo
        self.salario = salario_base
        self.descontos = descontos

        

    def calcular_salario(self):
        salario_liquido = (self.salario - self.descontos)
        return f"Salário líquido do funcionário {self.nome}: {salario_liquido}"
    

    def salvar(self):
        return {
            "Nome": self.nome,
            "Cpf": self.cpf,
            "Idade": self.idade,
            "Cargo": self.cargo,
            "Salario": self.salario,
            "Desconto": self.descontos}

        
    
    # def listar_dados(self):
    #     return {
    #         "nome": self.nome,
    #         "cpf": self.cpf,
    #         "idade": self.idade,
    #         "cargo": self.cargo,
    #         "salário": self.salario,
    #         "desconto": self.descontos
    #     }
        
        
        
        
    def mostrar_dados_funcionario(self):
        linha()
        return (f"""
        Nome: {self.nome}
        CPF: {self.cpf}
        Idade: {self.idade}
        Cargo: {self.cargo}
        Salário: {self.salario}:
        Desconto: {self.descontos}""")
        







