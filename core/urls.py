from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Incluimos las rutas de nuestra app "cuentas" en la raíz del sitio
    path('', include('cuentas.urls')),
]
