import pymongo
from pymongo import MongoClient
import os

uri = f"mongodb+srv://mateuscaik4:Mts2408@agendada.rhne2.mongodb.net/?retryWrites=true&w=majority&appName=Agendada"
client = MongoClient(uri)
db = client['agenda']
collection = db['contatos']


# Função para adicionar um contato
def adicionar_contato():
    try:
        nome = input("Nome completo: ")
        telefone = input("Telefone: ")
        collection.insert_one({
            "nome": nome,
            "telefone": telefone,
        })
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Contato cadastrado com sucesso!\n")
    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Erro ao cadastrar contato:", e)

# Função para listar os contatos
def listar_contatos():
    try:
        contatos = list(collection.find())  # Converte o cursor em uma lista
        if contatos:
            for contato in contatos:
                print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}")
            print("\n")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Nenhum contato cadastrado.")
    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Erro ao consultar contatos:", e)
        
# Função para editar um contato
def editar_contato():
    nome= input("Digite o nome do contato: ")
    try:
        resultado= collection .find_one({"nome": nome })
        if resultado: 
            nv_telefone= input("[atualizando...] telefone:")
            collection.update_one({"nome": nome}),(
            {
            "$set": {
                "telefone": nv_telefone,
                }
            })
            os.system ('cls' if os.name == 'nt' else 'clear')
            print ("Conta Editada!")
    except Exception as e:
            os.system ('cls' if os.name == 'nt' else 'clear')
            print("Erro!! :", e)

# Função para excluir um contato
def excluir_contato():
    nome= input("Digite o nome do contato: ")
    try:
        resultado = collection .find_one({"nome": nome })
        if resultado: 
            collection.delete_one({"nome": nome })
            os.system ('cls' if os.name == 'nt' else 'clear')
            print ("Conta Excluida!")
    except Exception as e:
            os.system ('cls' if os.name == 'nt' else 'clear')
            print("Erro!! :", e)

# Menu interativo
def menu():
    while True:
        print("\n===== AGENDA =====")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Editar Contato")
        print("4. Excluir Contato")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_contato()
        elif escolha == '2':
            listar_contatos()
        elif escolha == '3':
            editar_contato()
        elif escolha == '4':
            excluir_contato()
        elif escolha == '5':
            print("Saindo da agenda...")
            break
        else:
            print("Opção inválida! Tente novamente.")

menu()
