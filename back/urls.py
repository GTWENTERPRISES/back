"""
URL configuration for back project.

The `urlpatterns` list routes URLs to  For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cc.views import CategoriaViewSet, IconoViewSet, RedSocialViewSet, ProductoViewSet, EmpresaViewSet, ServicioViewSet, TestimonioViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'iconos', IconoViewSet)
router.register(r'redes-sociales', RedSocialViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'empresas', EmpresaViewSet)
router.register(r'servicios', ServicioViewSet)
router.register(r'testimonios', TestimonioViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
