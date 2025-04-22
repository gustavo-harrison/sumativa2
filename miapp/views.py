from django.shortcuts import render, redirect, get_object_or_404
from .models import Socio
from .forms import SocioForm


def inicio(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')

def formulario(request):
    return render(request, 'formulario.html')



def listar_socios(request):
    socios = Socio.objects.all()
    return render(request, template_name='listar_socios.html', context={'sociosss': socios} )



def crear_socio(request):
    if request.method == 'POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_socios')
    else:
        form = SocioForm()
    return render(request, template_name='form_socio.html', context={'form': form})



def editar_socio(request, pk):
    socio = get_object_or_404(Socio, pk=pk)

    if request.method == 'POST':
        form = SocioForm(request.POST, instance=socio)
        if form.is_valid():
            form.save()
            return redirect('listar_socios')
    else:
        form = SocioForm(instance=socio) 

    return render(request, 'form_socio.html', {'form': form})


def eliminar_socio(request, pk):
    socio = get_object_or_404(Socio, pk=pk)

    if request.method == 'POST':
        socio.delete()
        return redirect('listar_socios')
    return render(request, 'confirmar_eliminar.html', context={'socio': socio})




def nosotros(request):
    return render(request, 'nosotros.html')

def ns(request):
    return render(request, 'ns.html')

def ofertas(request):
    return render(request, 'ofertas.html')

def perfil(request):
    return render(request, 'perfil.html')

def ps4(request):
    return render(request, 'ps4.html')

def ps5(request):
    return render(request, 'ps5.html')

def xb360(request):
    return render(request, 'xb360.html')

def xbxs(request):
    return render(request, 'xbxs.html')

def inicio(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')

def formulario(request):
    return render(request, 'formulario.html')

