from pymongo import MongoClient

# URI de conexão com o MongoDB (usando autenticação)
MONGO_URI = "mongodb://CANNABISCULTURE_ADMIN:VprJ3Vi9@skrG3JT@191.252.203.234:27017/?authSource=admin"

# Conectando ao cliente MongoDB
client = MongoClient(MONGO_URI)

# Selecionando o banco de dados cannabis_culture
db = client["cannabis_culture"]

# Selecionando a coleção emails
emails_collection = db["emails"]

def salvar_email(email):
    # Verifica se o e-mail já existe na coleção
    existente = emails_collection.find_one({"email": email})

    if existente:
        return {"status": "erro", "mensagem": "E-mail já cadastrado"}
    
    # Se não existir, insere o e-mail na coleção
    emails_collection.insert_one({"email": email})
    return {"status": "ok", "mensagem": "Inscrição realizada com sucesso!"}

def listar_emails():
    # Retorna todos os e-mails da coleção
    return list(emails_collection.find())
