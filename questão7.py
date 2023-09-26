valueBuy = float(input('Valor da compra: '))

if valueBuy > 100: 
    print(f"O valor da compra é de: {valueBuy * 0.90}")
elif valueBuy >= 50 and valueBuy <= 100:
    print(f'O valor da compra é de: {valueBuy * 0.95}')
elif valueBuy  < 50:
    print(f'A compra não terá desconto. \n Valor total: {valueBuy}')