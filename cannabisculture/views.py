from django.shortcuts import render
from django.http import JsonResponse
from .mongo import emails_collection

def subscribe(request):
    return render(request, 'subscribe.html')

def salvar_email(request):
    if request.method == "POST":
        email = request.POST.get("email")

        if not email:
            return JsonResponse({"status": "erro", "mensagem": "Nenhum e-mail recebido"})

        # Verifica se já existe no banco
        existente = emails_collection.find_one({"email": email})

        if existente:
            return JsonResponse({"status": "erro", "mensagem": "Este e-mail já está cadastrado"})

        # Insere novo e-mail
        emails_collection.insert_one({"email": email})
        return JsonResponse({"status": "ok", "mensagem": "E-mail salvo com sucesso!"})

    return JsonResponse({"status": "erro", "mensagem": "Método inválido"})