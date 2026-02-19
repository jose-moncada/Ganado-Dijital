from django.urls import path
from . import views

urlpatterns = [
    path('', views.bienvenido, name='bienvenido'),
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('productos/', views.listar_productos, name='listar_productos'),
    path('productos/añadir/', views.anadir_producto, name='anadir_producto'),
    path('productos/eliminar/<str:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('productos/editar/<str:producto_id>/', views.editar_producto, name='editar_producto')
]