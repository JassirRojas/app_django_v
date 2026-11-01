from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Vista basada en clases de Django para el login, usando nuestro template
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    # Vista para cerrar sesión y redirigir al login
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    # Vista del dashboard que varía según los roles
    path('dashboard/', views.dashboard, name='dashboard'),
]