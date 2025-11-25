# Nome : Vithor Lowis
# Disciplina : Estrutura de dados
# Atividade : Análise de sequÊncia de parêntesis e colchetes feita com a utilização
# de uma estrutura Stack

class Stack :
    def __init__(self):
        self.dados = []

    def empilhar (self,item):
        self.dados.append(item)

    def desempilhar(self) :
        return self.dados.pop()

    def esta_vazia(self) :
        return len(self.dados) == 0

def verificar_expressao(sequencia) :
    p = Stack()

    pares_corretos = { ')':'(',']':'['}

    for char in sequencia:
        if char == '(' or char == '[' :
            p.empilhar(char)

        elif char == ')' or char == ']' :
            if p.esta_vazia() :
                return False

            ultimo_aberto = p.desempilhar()
            abertura_esperada = pares_corretos[char]

            if ultimo_aberto != abertura_esperada:
                return False
    if p.esta_vazia() :
        return True
    else:
        return False
if __name__ == '__main__':
    print(" ------------------------------------")
    print("Programa para verificar sequência de expressões")
    print("")
    while True :
        entrada = input("Digite uma expressão ou digite  S para encerrar o programa:")

        if entrada.upper() == 'S':
            break

        resultado = verificar_expressao(entrada)
        if resultado == True :
            print ("Sequência bem formada")
        else:
            print ("Sequencia mal formada ")




