from django.shortcuts import render
from .models import Categoria, Icono, RedSocial, Producto, Empresa, Servicio, Testimonio
from .serializers import CategoriaSerializer, IconoSerializer, RedSocialSerializer, ProductoSerializer, EmpresaSerializer, ServicioSerializer, TestimonioSerializer
# Create your views here.
# views.py
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre']

class IconoViewSet(viewsets.ModelViewSet):
    queryset = Icono.objects.all()
    serializer_class = IconoSerializer

class RedSocialViewSet(viewsets.ModelViewSet):
    queryset = RedSocial.objects.all()
    serializer_class = RedSocialSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.filter(activo=True)
    serializer_class = ProductoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['categoria', 'empresa']
    search_fields = ['nombre', 'descripcion']

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.filter(activa=True)
    serializer_class = EmpresaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['categoria']
    search_fields = ['nombre', 'descripcion']

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.filter(activo=True)
    serializer_class = ServicioSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['categoria']
    search_fields = ['titulo', 'descripcion']

class TestimonioViewSet(viewsets.ModelViewSet):
    queryset = Testimonio.objects.filter(aprobado=True)
    serializer_class = TestimonioSerializer