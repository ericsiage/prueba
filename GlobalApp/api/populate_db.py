import csv
import datetime

from GlobalApp.models import Empresa, Transaccion


def populate_empresas():
    Empresa.objects.all().delete()
    with open('test_database.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        companies = set()
        for row in csv_reader:
            companies.add(row['company'])
    for e in companies:
        empresa = Empresa(nombre=e, status=True)
        empresa.save()


def populate_transacciones():
    Transaccion.objects.all().delete()
    with open('test_database.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        transacciones = []
        for row in csv_reader:
            print(row['date'])
            try:
                date = datetime.datetime.strptime(row['date'].split('.')[0], "%Y-%m-%d %H:%M:%S")
            except :
                date = datetime.datetime.strptime(row['date'][:-3], "%Y-%m-%d %H:%M:%S")
            empresa = Empresa.objects.get(nombre=row['company'])
            cobro_final = True if row['status_transaction'] == 'closed' and row['status_approved'] else False
            transacciones.append(
                dict(empresa=empresa, price=row['price'], date=date,
                     status_transaction=row['status_transaction'] == 'reversed',
                     status_approved=row['status_approved'], cobroFinal=cobro_final))
    for t in transacciones:
        transaccion = Transaccion(empresa=empresa, price=t['price'], fecha=datetime.datetime.now(),
                                  estatus_Transaccion=t['status_transaction'],
                                  estatus_Aprobacion=t['status_approved'] == 'false', cobroFinal=t['cobroFinal'])
        transaccion.save()