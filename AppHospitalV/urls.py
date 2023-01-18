from django.urls import path

from AppHospitalV import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"), 
    path('especialidades', views.especialidades, name="Especialidades"),
    path('staff', views.staff, name="Staff"),
    path('laboratorio', views.laboratorio, name="Laboratorio"),
    path('imagenes', views.imagenes, name="EstudiosDeImagen"),
    path('especialidadesform', views.especialidadesform, name="EspecialidadesFormulario"),
    path('profesionales', views.profesionales, name="Profesionales"),
    path('busquedaProfesion', views.busquedaProfesion, name="BusquedaProfesion"),
    path('buscar/', views.buscar),
    path('leerProfesionales', views.leerProfesionales, name="LeerProfesionales"),
    path('resultadoBusqueda', views.buscar, name="ResultadoBusqueda" )

]