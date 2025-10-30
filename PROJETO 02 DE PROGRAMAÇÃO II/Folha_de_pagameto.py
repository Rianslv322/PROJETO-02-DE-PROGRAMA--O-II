from Gerente import *
class Folha_de_Pagamento:
    def __init__(self,gerente):
        self.gerente = gerente


    def gerar_relatorio(self):
        for x in self.gerente.lista_F:
            salario_liquido = x.calcular_salario()
            print(f"""
Nome: {x.nome}
Cargo: {x.cargo}
Salário: {x.salario}
{salario_liquido}
Descontos: {x.descontos}
""")

    
    def gerar_relatorio_individual(self):
        cpf = str(input("Digite o CPF --> "))
        for x in self.gerente.lista_F:
            if x.cpf == cpf:
                print(x.mostrar_dados_funcionario())

    

Gerente_geral_da_Empresa = Gerente("Rian Silva", "123.321-678-45", 29, "Gerente", 6000, 600, 123)
# Gerente_geral_da_Empresa.cadastrar_funcionario("Ana", "741-852", 26, "TI", 5000, 600)
folhadepagar = Folha_de_Pagamento(Gerente_geral_da_Empresa)
