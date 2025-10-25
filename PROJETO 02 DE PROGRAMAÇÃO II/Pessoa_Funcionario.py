class Pessoa:
    def __init__(self,nome,cpf,idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
    

    def __str__(self):
        print("DADOS DA PESSOA")
        print(f"""
        Nome: {self.nome}
        Idade: {self.idade}
        CPF: {self.cpf}
""")
        

    def salvar(self):

        return {"Nome": self.nome,
                 "CPF":self.cpf,
                 "Idade":self.idade}
        


class Funcionario(Pessoa):
    def __init__(self, nome, cpf, idade,cargo,salario_base,descontos):
        super().__init__(nome, cpf, idade)
        self.cargo = cargo
        self.salario = salario_base
        self.descontos = descontos

        

    def calcar_salario(self):
        salario_liquido = (self.salario - self.descontos)
        return f"Salário líquido do funcionário: {salario_liquido}"
    

    def salvar(self):
        dados = super().salvar()
        dados.update({
            "Cargo": self.cargo,
            "Salario": self.salario,
            "Desconto": self.descontos}
            )
        
        return dados
    

    def listar_dados(self):
        return {
            "nome": self.nome,
            "cpf": self.cpf,
            "idade": self.idade,
            "cargo": self.cargo,
            "salário": self.salario,
            "desconto": self.descontos

        }







