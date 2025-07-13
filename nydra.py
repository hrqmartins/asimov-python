def bot_resposta(mensagens):
    return 'Resposta do Bot'

print('Bem vindo ao Nydra! (Digite X para sair)')

mensagens = []
while True:
    pergunta = input('Usuario: ')
    if pergunta.lower() == 'x':
        break
    mensagens.append({'role': 'user', 'content': pergunta})
    resposta = bot_resposta(mensagens)
    mensagens.append({'role': 'assistant', 'content': resposta})
    print(f'Bot: {resposta}')
    
print('Muito obrigado por usar o Nydra!')
print(mensagens)