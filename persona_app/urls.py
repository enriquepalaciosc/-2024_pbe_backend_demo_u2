from django.urls import path
from persona_app import views
urlpatterns = [
    path('personas/', views.obtenerPersonas),
    path('personas/perfil/<int:id>', views.obtenerPerfil),
    path('personas/perfil/modificar/<int:id>', views.modificarPersona),
]