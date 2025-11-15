from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .mongo import emails_collection


def subscribe(request):
    return render(request, 'subscribe.html')


@csrf_exempt  # remove se for enviar com CSRF token
def salvar_email(request):

    if request.method != "POST":
        return JsonResponse({
            "status": "erro",
            "mensagem": "Método inválido"
        }, status=405)

    # Suporte para JSON body ou x-www-form-urlencoded
    email = request.POST.get("email")

    if not email:
        try:
            import json
            body = json.loads(request.body.decode("utf-8"))
            email = body.get("email")
        except:
            email = None

    # Validação
    if not email:
        return JsonResponse({
            "status": "erro",
            "mensagem": "Nenhum e-mail recebido"
        }, status=400)

    # Verificar duplicado
    existente = emails_collection.find_one({"email": email})

    if existente:
        return JsonResponse({
            "status": "erro",
            "mensagem": "E-mail já cadastrado"
        }, status=409)

    # Salvar no MongoDB
    emails_collection.insert_one({
        "email": email
    })

    return JsonResponse({
        "status": "ok",
        "mensagem": "Inscrição realizada com sucesso!"
    }, status=200)
