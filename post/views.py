from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.



def rick(request):
    return render(request,'post/Главная.html')

def adout(request):
    return HttpResponse('хуй')