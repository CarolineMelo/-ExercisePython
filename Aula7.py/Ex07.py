#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunta nota: '))
M = (nota1 + nota2) /2
print('A média entre {:.1f} e {:.1f}  é igual a {:.1f}'.format(nota1,nota2,M))
