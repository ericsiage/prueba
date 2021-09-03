import re
from django.db.models.aggregates import Max
from django.http import response
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import filters, generics
from rest_framework.generics import ListAPIView
from GlobalApp.models import Empresa, Transaccion
from .serializers import EmpresaSerializer, TransaccionSerializer
from django.db.models import Count, Sum
from .populate_db import populate_empresas, populate_transacciones

"""
@api_view(['GET'])
def empresa_api_view(request):
    if request.method == 'GET':
        empresas = Empresa.objects.all()        
        empresas_serializer = EmpresaSerializer(empresas, many=True)
        return Response(empresas_serializer.data)
@api_view(['GET'])
def transaccion_api_view(request):
    transaccion = Transaccion.objects.all()
    transaccion_serializer = TransaccionSerializer(transaccion, many=True)
    filter_backend = (filters.SearchFilter)
    search_field = ('empresa')
    return Response( transaccion_serializer.data)
"""
class resumenAPIView(APIView):
    def get(self,request):
                #precio total de transacciones por empresa
                totalPrecio = Empresa.objects.values('nombre','transaccion').annotate(transacciones=Count('transaccion')).order_by('-transacciones')
                return Response(totalPrecio)

                      

class EmpresaDeMayorVentas(APIView):
        def get(self, request):
            empresaMas = Transaccion.objects.values('empresa_id','price','empresa').annotate(total_precio=Sum('price')).annotate(aprobacion=Count('estatus_Aprobacion')).order_by('-price')
            #total_serializer = TransaccionSerializer(total, many=True)
            return Response(empresaMas)






class Populate_db(APIView):
    def get(self, request):
        populate_empresas()
        populate_transacciones()
        return Response(len(Empresa.objects.all()))
