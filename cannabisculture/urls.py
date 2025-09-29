from django.urls import path
from .views import subscribe, salvar_email
from . import views

urlpatterns = [
    path('', subscribe, name='subscribe'),
    path("salvar-email/", views.salvar_email, name="salvar_email"),
]
