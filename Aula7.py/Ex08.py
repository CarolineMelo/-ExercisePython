#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
#V = float(input('Luiz Miguel de Melo, por favor, digite aqui o valor do metro: '))
#C = (V *100)
#M = (V *1000)
#print('Obrigada Luiz! o valor do metro é {}, convertido para centímetros é {} e em milímetros é {}'.format(V,C,M))
medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida,cm,mm))