#Faça um algoritmo que leia o preço de um pruduto e mostre seu novo preço de um produto e mostre seu novo preço, com 5% de desconto.
preço = float(input('Qual é o preço do produto? R$' ))
novo = preço - (preço * 5 / 100)
print('O produto que custava R${}, na promoção com o desconto de 5% vai custar R${}'.format(preço,novo))