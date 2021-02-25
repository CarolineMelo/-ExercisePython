#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
print('Cateto Oposto é {} \nCateto Adjacente é {} \nLogo o comprimento da hipotenusa é {:.2f}'.format(ca,co,hypot(ca,co)))