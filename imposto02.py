def cadastro():
        nome = input('Digite o nome: ')
        sal = float(input('Digite o salario: '))
        if sal <= 2000:
            IR = 0
        elif sal <= 3000:
            IR = (sal - 2000) * 0.08
        elif sal <= 4500:
            IR = (sal - 3000) * 0.18 + 3000*0.08
        else:
            IR = (sal - 4500) * 0.28 + 1500*0.18  + 1000*0.08
        pessoa= {'nome': nome, 'salario': sal, 'imposto': IR}
        return pessoa
        
def exibir_pessoas(l):
    for i in range(len(L)):
      print('nome: ', L[i]['nome'])     
      print('salario: ' "%.2f" % L[i]['salario'])
      print('imposto: ' "%.2f" %  L[i]['imposto'])
      
L= []
N =  int(input('Insira a quantidade de pessoas: '))
for i in range(N):
    p = cadastro()
    L.append(p)
    
exibir_pessoas(L)
