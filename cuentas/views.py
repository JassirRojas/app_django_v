from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# El decorador obliga a iniciar sesión para ver esta vista
@login_required
def dashboard(request):
    """
    Vista del panel principal. 
    Verifica a qué grupo pertenece el usuario autenticado
    para enviarle esa información a la plantilla HTML.
    """
    # Comprobamos los roles del usuario actual
    es_admin = request.user.groups.filter(name='Administrador').exists() or request.user.is_superuser
    es_gestor = request.user.groups.filter(name='Gestor').exists()
    es_usuario = request.user.groups.filter(name='Usuario').exists()
    
    # Pasamos los permisos como contexto a la plantilla
    contexto = {
        'es_admin': es_admin,
        'es_gestor': es_gestor,
        'es_usuario': es_usuario,
    }
    
    return render(request, 'dashboard.html', contexto)