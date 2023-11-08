from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def milk(request):
    return HttpResponse('i am talking about amul milk')