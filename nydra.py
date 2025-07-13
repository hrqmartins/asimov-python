import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

api_key = ''
os.environ['GROQ_API_KEY'] = api_key
chat = ChatGroq(model='meta-llama/llama-4-maverick-17b-128e-instruct')

def bot_resposta(mensagens):
    mensagens_modelo = [{"role": "system", "content": "Você é um assistente educado e amigavel chamado Nydra"}]
    mensagens_modelo += mensagens
    templates = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = templates | chat
    return chain.invoke({}).content
                        

print('Bem vindo ao Nydra! (Digite X para sair)')

mensagens = []
while True:
    pergunta = input('Usuario: ')
    if pergunta.lower() == 'x':
        break
    mensagens.append(('user', pergunta))
    resposta = bot_resposta(mensagens)
    mensagens.append(('assistant', resposta))
    print(f'Bot: {resposta}')
    
print('Muito obrigado por usar o Nydra!')
print(mensagens)