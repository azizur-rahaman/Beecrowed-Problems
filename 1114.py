password=2002

while True:
    chechPass=int(input())

    if chechPass == password:
        print('Acesso Permitido')
        break
    else:
        print('Senha Invalida')