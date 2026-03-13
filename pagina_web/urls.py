from django.urls import path
from . import views

urlpatterns = [
    path('', views.bienvenido, name='bienvenido'),
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('opciones/', views.listar_animales, name='listar_animales'),
    path('opciones/añadir/', views.anadir_animal, name='anadir_animal'),
    path('opciones/eliminar/<str:producto_id>/', views.eliminar_animal, name='eliminar_animal'),
    path('opciones/editar/<str:producto_id>/', views.editar_animal, name='editar_animal')
]