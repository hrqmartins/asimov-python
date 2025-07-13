mensagens = []

print('Bem-vindo ao Nydra! (Aperte X para sair)\n')

while True:
    pergunta = input('Qual é a sua pergunta? ')
    print('Bot: ')
    mensagens.append(pergunta)
    if pergunta == 'x':
        print('Voce escolheu sair!')
        print(f'Mensagens que vc enviou ate agora foram: \n {mensagens}')
        break
