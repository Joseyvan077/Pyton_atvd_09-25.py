numeroExtras = float(input('Qual o numero de horas extras?'))
numeroDeFaltas = float(input("Qual o numero de horas faltadas?"))

if numeroExtras > (numeroDeFaltas / 2):
    print('500R$ bonus')
else:
    print('Sem bonus')