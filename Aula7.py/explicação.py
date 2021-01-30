#nome = input ('Qual é o seu nome? ' )
#print('Prazer em te conhecer {:10}!'.format(nome))          :10 espaço
#print('Prazer em te conhecer {:^10}!'.format(nome))   :^ centralizou
#print('Praze em te conhecer {:>10}!'.format(nome))
#print('Prazer em te conhecer {:=^20}!'.format(nome))   
#nome = input('Qual é o seu nome?')
#print('Prazer em te conhecer{:=^20}'.format(nome))
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('O Primeiro valor somado ao segundo valor resultará em {}, \n a multiplicação {}, \n a divisão {:.2f} , divisão inteira {} \n e potência {}'.format(s,m,d,di,e))



