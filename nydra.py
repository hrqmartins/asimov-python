
import os 

os.environ['GROQ_API_KEY'] = api_key 
'''
environ -> varivavel de ambiente
'''

from langchain_groq import ChatGroq
chat = ChatGroq(model='meta-llama/llama-4-maverick-17b-128e-instruct')
resposta = chat.invoke('Ola modelo! quem é voce?')
print(resposta.content)