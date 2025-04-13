from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from core.models import Categoria, Juego, Usuario
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password 
from django.utils import timezone
from datetime import datetime
from core.forms import UsuarioForm


# Vistas principales
def index(request):
    categorias = Categoria.objects.all()
    return render(request, 'web/index.html', {'categorias': categorias})

def login(request):
    return render(request, 'web/login.html')


# Vista de formulario de registro
def registro(request):
    form = UsuarioForm()  # Instancia del formulario
    return render(request, 'web/registro.html', {'form': form})

# Vista para el formulario de registro (manejo completo con validación)
def formulario_registro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Cambia esto a donde quieras redirigir tras el registro
    else:
        form = UsuarioForm()
    
    return render(request, 'registro.html', {'form': form})

# Vista para manejar el formulario de registro via AJAX
def registro_ajax(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

def perfil(request):
    return render(request, 'web/perfil.html')

def recuperar(request):
    return render(request, 'web/recuperar.html')

def contacto(request):
    return render(request, 'web/contacto.html')

def carrito(request):
    return render(request, 'web/carrito.html')

# Vistas por categoría (podrías eliminarlas si usas solo `subcategoria`)
def categoria_carreras(request):
    categoria = get_object_or_404(Categoria, nombre__iexact="Carreras")
    juegos = Juego.objects.filter(categoria=categoria)
    return render(request, 'categorias/carreras.html', {"categoria": categoria, "juegos": juegos})

def categoria_cozy(request):
    categoria = get_object_or_404(Categoria, nombre__iexact="Cozy")
    juegos = Juego.objects.filter(categoria=categoria)
    return render(request, 'categorias/cozy.html', {"categoria": categoria, "juegos": juegos})

def categoria_mundoabierto(request):
    categoria = get_object_or_404(Categoria, nombre__iexact="Mundo Abierto")
    juegos = Juego.objects.filter(categoria=categoria)
    return render(request, 'categorias/mundoabierto.html', {"categoria": categoria, "juegos": juegos})

def categoria_shooters(request):
    categoria = get_object_or_404(Categoria, nombre__iexact="Shooters")
    juegos = Juego.objects.filter(categoria=categoria)
    return render(request, 'categorias/shooters.html', {"categoria": categoria, "juegos": juegos})

def categoria_terror(request):
    categoria = get_object_or_404(Categoria, nombre__iexact="Terror")
    juegos = Juego.objects.filter(categoria=categoria)
    return render(request, 'categorias/terror.html', {"categoria": categoria, "juegos": juegos})

# Vista dinámica por ID
def subcategoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    juegos = Juego.objects.filter(categoria=categoria)
    return render(request, 'web/subcategorias.html', {
        'categoria': categoria,
        'juegos': juegos
    })

# Detalle del juego
def detalle_juego(request, juego_id):
    juego = get_object_or_404(Juego, pk=juego_id)
    return render(request, 'web/detalle.html', {'juego': juego})
