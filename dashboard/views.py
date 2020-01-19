from django.shortcuts import render, redirect
from .models import QREvent as QRevent
import pyqrcode
from pyqrcode import QRCode
import os
# Create your views here.


def index(request):
    return render(request, 'dashboard/index.html')


def qreventmanager(request):
    qrevents = QRevent.objects.all()
    return render(request, 'dashboard/qreventmanager.html', {'qrevents': qrevents})


def qreventmanager_manger(request):
    return render(request, 'dashboard/qreventmanager_manger.html')


def qreventmanager_edit(request, id):
    if request.method == 'POST':
        qr = QRevent.objects.get(pk=id)
        qr.title = request.POST['title']
        qr.description = request.POST['description']
        qr.status = request.POST['status']
        qr.disabledesc = request.POST['disableddesc']
        qr.save()
        return redirect('qreventmanager')
    else:
        qrevent = QRevent.objects.get(pk=id)
        return render(request, 'dashboard/qreventmanager_edit.html', {'qrevent': qrevent})


def qreventmanager_delete(request, id):
    if request.method == 'POST':
        qr = QRevent.objects.get(pk=id)
        qr.delete()
        return redirect('qreventmanager')
    else:
        qrevent = QRevent.objects.get(pk=id)
        return render(request, 'dashboard/qreventmanager_delete.html', {'qrevent': qrevent})


def qreventmanager_dwn(request, id):
    qr = QRevent.objects.get(pk=id)
    s = 'http://127.0.0.1:8000/dashboard/qreventmanager/' + str(qr.id)
    url = pyqrcode.create(s)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    url.svg(os.path.join(BASE_DIR, 'static') +
            "/qrcode/"+str(qr.id)+".svg", scale=8)
    return render(request, 'dashboard/qreventmanager_dwn.html', {'QR': qr})


def qreventmanager_create(request):
    if request.method == 'POST':
        qr = QRevent()
        qr.title = request.POST['title']
        qr.description = request.POST['description']
        qr.status = request.POST['status']
        qr.disabledesc = request.POST['disableddesc']
        qr.save()
        return redirect('qreventmanager')

    else:
        return render(request, 'dashboard/qreventmanager_create.html')


def qrevent_createform(request, id):
    if request.method == 'POST':
        if 'setenablepayment' in request.POST:
            QR = QRevent.objects.get(pk=id)
            QR.enablepayment = request.POST['enablepayment']
            QR.save()
            return redirect('qrevent_createform', id=id)
        if 'setfee' in request.POST:
            QR = QRevent.objects.get(pk=id)
            QR.feeamount = request.POST['feeamount']
            QR.save()
            return redirect('qrevent_createform', id=id)
        if 'disablefee' in request.POST:
            QR = QRevent.objects.get(pk=id)
            QR.enablepayment = '0'
            QR.save()
            return redirect('qrevent_createform', id=id)
    else:
        QR = QRevent.objects.get(pk=id)
        return render(request, 'dashboard/qrevent_createform.html', {'QR': QR})

def qrevent_client(request,id):
    QRE = QRevent.objects.get(pk=id)
    return render(request,'dashboard/client.html',{'QRE':QRE})