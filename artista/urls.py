#AUTOR:TCL JOHAN +
from django.urls import path
from . import views # para poder acceder a vistas
urlpatterns = [
    #cuando usuario aceda a app que se redireccione a: 
    path('',views.index,name='index'),
    # path('editarVista/<int:id>',views.editarVista,name='editarVista'),
    path('eliminar/<int:id>',views.eliminar,name='eliminar'),
    path('editar/<int:id>',views.editar,name='editar'),
    path('crear',views.crear,name='crear'),
     
]
