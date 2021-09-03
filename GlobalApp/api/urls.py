from django.urls import path
from GlobalApp.api.api import resumenAPIView, EmpresaDeMayorVentas, Populate_db

urlpatterns = [
    #path('resumen/', empresa_api_view,transaccion_api_view, name="resumen_api"),
    path('', resumenAPIView.as_view(), name="resumen_api"),
    path('resumen/', EmpresaDeMayorVentas.as_view(), name="resumen_api"),
    path('db/', Populate_db.as_view(), name="populate"),
]

