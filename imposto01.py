#5) Imposto de Renda
#Em um país imaginário denominado Lisarb, todos os habitantes ficam felizes em pagar seus impostos, pois sabem que nele não existem políticos
# corruptos e os recursos arrecadados são utilizados em benefício da população, sem qualquer desvio. 
# A moeda deste país é o Rombus, cujo símbolo é o R$.
#Leia um valor, equivalente ao salário de uma pessoa de Lisarb. Em seguida, calcule e mostre o valor que esta pessoa deve pagar de 
# Imposto de Renda, segundo a tabela abaixo.

#Lembre que, se o salário for 3.002,00, a taxa que incide é de 8% apenas sobre 1.000,00, pois a faixa de salário que fica de 0,00 até 2.000,00
# é isenta de Imposto de Renda. Solicite os dados (Nome, Salário) de N pessoas.
# Calcule o IR para cada pessoa. Ao final exiba uma listagem em ordem decrescente por IR a pagar de cada pessoa.


def cadastro(N, L):
    for i in range(N):
        nome = input('Digite o nome: ')
        sal = float(input('Digite o salario: '))
        if sal <= 2000:
            IR = 0
        elif sal <= 3000:
            IR = (sal - 2000) * 0.08
        elif sal <= 4500:
            IR = (sal - 3000) * 0.18 + 3000/0.08
        else:
            IR = (sal - 4500) * 0.28 + 2500/0.18  + 1000*0.08
        pessoa= {'nome': nome, 'salario': sal, 'Imposto': IR}
        L.append(pessoa)
        
        
        
L= []
N =  int(input('Insira a quantidade de pessoas: '))
cadastro(N, L)
print(L)