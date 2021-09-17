from django.shortcuts import render
from django.http import HttpResponse

from backups_operator.servers.models import Server
# Create your views here.

def home(request):
    servers = Server.objects.all()

    data = {
        'servers': servers
    }
    return render(request, 'sources/home.html', data)

def test(request):
    return HttpResponse('test')

def manage(request, id):
    return HttpResponse('test')

def authHome(request):
    return HttpResponse('test')