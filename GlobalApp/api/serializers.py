
from rest_framework import serializers
from GlobalApp.models import Empresa, Transaccion

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Empresa
        fields = '__all__'

class TransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaccion
        fields = '__all__'
