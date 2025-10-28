import json
from datetime import datetime
from Gerente import *
class Folha_de_Pagamento:
    def __init__(self,arquivo_dados = "arquivo.json",relatorio = "arquivo_relatorio.json"):
        self.arquivo_dados = arquivo_dados
        self.relatorio =relatorio
        
        
    
    def carregar_dados(self):
        try:
            with open(self.arquivo_dados, "r",encoding="UTF-8") as f:
                dados = json.load(f)
                
        except(FileNotFoundError, json.JSONDecodeError):
            dados = []
        return dados
    
    def calcular_total(self):
        dados = self.carregar_dados()
        total = 0
        
        for x in dados:
            salario_liquido = x["salario"] - x["desconto"]
            total += salario_liquido
            
        return total
    
    
    def gerar_relatori(self):
        dados = self.carregar_dados()
        total_folha = self.calcular_total_folha()
        
        relatorio = {
                "data_geracao": datetime.now().strftime("%d/%m/%y %H:%M:%S"),
                "total_funcionarios": len(dados),
                "total_folha": total_folha,
                "funcionarios":[]            
        }
        
        for x in dados:
            salario_liquido = x["salario"] - x["desconto"]
            relatorio["funcionarios"].append({
                "Nome": x["nome"],
                "Cargo": x["cargo"],
                "Salário Bruto": x["salario"],
                "Desconto": x["desconto"],
                "Salário Líquido": salario_liquido
                  })
            
        try:
            with open(self.arquivo_relatorio, "w", encoding="utf-8") as f:
                json.dump(relatorio, f, indent=4, ensure_ascii=False)
            print(f"✅ Relatório gerado com sucesso em '{self.arquivo_relatorio}'!")
        except Exception as e:
            print(f"❌ Erro ao gerar relatório: {e}")

