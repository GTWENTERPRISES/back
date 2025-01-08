# serializers.py
from rest_framework import serializers
from .models import Categoria, Icono, RedSocial, CaracteristicaProducto, Producto, Empresa, EmpresaRedSocial, Servicio, Testimonio
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class IconoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Icono
        fields = '__all__'

class RedSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedSocial
        fields = '__all__'

class CaracteristicaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaracteristicaProducto
        fields = ['nombre', 'valor']

class ProductoSerializer(serializers.ModelSerializer):
    caracteristicas = CaracteristicaProductoSerializer(many=True, read_only=True)
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)

    class Meta:
        model = Producto
        fields = '__all__'

class EmpresaRedSocialSerializer(serializers.ModelSerializer):
    red_social_nombre = serializers.CharField(source='red_social.nombre', read_only=True)

    class Meta:
        model = EmpresaRedSocial
        fields = '__all__'

class EmpresaSerializer(serializers.ModelSerializer):
    productos = ProductoSerializer(many=True, read_only=True)
    redes_sociales = EmpresaRedSocialSerializer(many=True, read_only=True)
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)

    class Meta:
        model = Empresa
        fields = '__all__'

class ServicioSerializer(serializers.ModelSerializer):
    icono_nombre = serializers.CharField(source='icono.nombre', read_only=True)
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)

    class Meta:
        model = Servicio
        fields = '__all__'

class TestimonioSerializer(serializers.ModelSerializer):
    empresa_nombre = serializers.CharField(source='empresa.nombre', read_only=True)

    class Meta:
        model = Testimonio
        fields = '__all__'