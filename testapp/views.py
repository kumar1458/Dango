from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hellow_world_view(request):
    return HttpResponse('<h1>Hellow ,This is response from django application</h1>')
