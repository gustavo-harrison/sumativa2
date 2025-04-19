from django.shortcuts import render


def inicio(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')

def formulario(request):
    return render(request, 'formulario.html')

def inicio_sesion(request):
    return render(request, 'inicio_sesion.html')

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
