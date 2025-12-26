import time as t
#pontinhos para melhor dinâmica
def pontinhos():
    inicio = t.time()
    while t.time() - inicio < 5:
        print(".", end="", flush=True)
        t.sleep(0.9)
#---------------------

# classes
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.saude = 50

class Funcionario(Pessoa):
    def __init__(self, nome, idade, saude):
        super().__init__(nome, idade)
        self.saude = saude
        self.salario = 0
        self._energia = 100
        
        
#estrutura do funcionário

    @property
    def energia(self):
        return self._energia

    @energia.setter
    def energia(self, valor):
        if valor < 0:
            print("Está muito cansado, precisa descansar")
            self._energia = 0
        else:
            self._energia = valor
    
    def trabalhar(self):
        if self.energia > 0:
            print("Você está trabalhando")
            pontinhos()
            self.energia -= 20

            self.salario += 1512
        else:
            print("não pode trabalhar, está muito cansado")

    def gastar_dinheiro(self):
        produtos = {
            "pão": 2,
            "suco":10,
            "pastel": 15,
            "coxinha": 12,
            "refri(2L)": 20
        }

        for produto, preco in produtos.items():
            print(produto, "-", preco)

        pergunta = input("O que você quer comprar?")

        if pergunta.lower() == "pao" or pergunta.lower() == "pão":
            print("Você comprou um pão")
            self.salario -= 2
        
        elif pergunta.lower() == "suco":
            print("Você comprou um suco")
            self.saude += 5
            self.salario -= 10
        
        elif pergunta.lower() == "pastel":
            print("Você comprou pastel")
            self.saude -= 7
            self.salario -= 15
        
        elif pergunta.lower() == "coxinha":
            print("Você comprou coxinha")
            self.saude -= 10
            self.salario -= 12
        
        elif pergunta.lower() == "refri" or pergunta.lower() == "refrigerante":
            print("Você comprou refrigerante(2L)")
            self.saude -= 20
            self.salario -= 20
        
        else:
            print("Esse produto não existe")

    def descansar(self, tempo):
        if tempo > 30:
            self.energia = min(self.energia + 40, 100)
        else:
            self.energia = min(self.energia + 30, 100)
    
    def vivo(self):
        if self.saude <= 0:
            print("💀 Você morreu por falta de saúde")
            return False
        elif self.energia <= 0:
            print("💀 Você morreu de exaustão")
            return False
        return True
    
    def status(self):
        print(f"Nome: {self.nome}, Salário: {self.salario}, Estado da Saúde: {self.saude}, Energia: {self.energia}")
    
p = Pessoa("dany", 18)
f = Funcionario("pablo", 23, 40)

print("1) Trabalhar\n2) Descansar\n3) Comprar item\n4) Ver status\n0) Sair")
while True:
    acao = int(input("\nO que você quer fazer?"))
  

    if acao == 1:
        f.trabalhar()
    elif acao == 2:
        temp = int(input("quanto tempo você quer descansar: "))
        f.descansar(temp)
    elif acao == 3:
        f.gastar_dinheiro()
    elif acao == 4:
        f.status()
    elif acao == 0:
        print("Você saiu")
        break
    else:
        print("Está ação não existe")
    
    if not f.vivo():
        break