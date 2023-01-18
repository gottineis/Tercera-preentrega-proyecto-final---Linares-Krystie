from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppHospitalV.models import Staff, Especialidades


def inicio(request):

      return render(request, "AppHospitalV/inicio.html")

def especialidades(request):

      return render(request, "AppHospitalV/especialidades.html")

def staff(request):

      return render(request, "AppHospitalV/staff.html")

def laboratorio(request):

      return render(request, "AppHospitalV/laboratorio.html")

def imagenes(request):

      return render(request, "AppHospitalV/imagenes.html")


from AppHospitalV.forms import EspecialidadesFormulario, StaffFormulario

def especialidadesform(request):

      if request.method == "POST":
         
          miFormulario = EspecialidadesFormulario(request.POST) 
          print(miFormulario)
 
          if miFormulario.is_valid:
                 informacion = miFormulario.cleaned_data
                 especialidad = Especialidades (nombre=informacion["especialidad"], adulto=informacion["adulto"], pediatrico=informacion["pediatrico"])
                 especialidad.save()
                 return render(request, "AppHospitalV/inicio.html")
      else:
          miFormulario = EspecialidadesFormulario()
    
      return render(request, "AppHospitalV/especialidadesform.html", {"miFormulario": miFormulario})

def profesionales(request):

      if request.method == "POST":

            miFormulario = StaffFormulario(request.POST) 
            print(miFormulario)
 
            if miFormulario.is_valid:
                 informacion = miFormulario.cleaned_data
                 
                 staff = Staff(nombre=informacion["nombre"], apellido=informacion["apellido"],
                 email=informacion['email'], profesion=informacion['profesion'])
                 staff.save()

                 return render(request, "AppHospitalV/inicio.html")
      else:
           miFormulario = StaffFormulario()
    
      return render(request, "AppHospitalV/profesionales.html", {"miFormulario": miFormulario})


def busquedaProfesion(request):
      
      return render(request, "AppHospitalV/busquedaProfesion.html")

def buscar(request):

      if request.GET["profesion"]:
             profesion = request.GET['profesion']
             profesionales = Staff.objects.filter(profesion__icontains=profesion)
      
             return render(request, "AppHospitalV/inicio.html",{"profesionales":profesionales, "profesion": profesion})
      else:
             respuesta = "No enviaste datos"
      return HttpResponse(respuesta)



def leerProfesionales(request):
        staff = Staff.objects.all() 
        contexto= {"staff":staff}
        return render(request, "AppHospitalV/leerProfesionales.html",contexto)
        
