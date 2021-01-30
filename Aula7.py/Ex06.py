#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
N = int(input('Número:'))
#print('O número é {} \nDobro {}\nTriplo {} \nRaiz quadrada {}'.format(N,(2*N),(3*N),(N*(1/2))))
D = N*2
T = N*3
R = pow(N,(1/2))
print('O dobro de {} vale {}.'.format(N,D))
#print('O triplo de {} vale {}. A raiz quadrada de {} é igual a {:.2f}.'.format(N,T,N,R))
print('O triplo de {} vale {}. A raiz quadrada de {} é igual a {:.2f}.'.format(N,T,N,R))