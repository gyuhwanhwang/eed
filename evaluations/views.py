from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("eval main")


def eval_home(requset):
    return render(request, 'eval_home.html')
