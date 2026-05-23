from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.3



def cadastro(request):
    return render(request,'cadastro.html')
