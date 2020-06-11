from django.shortcuts import render

#bir sayfa render etmek yerine bir text dönmek için kullanıldı
from django.http import HttpResponse
# Create your views here.

#ana dizin view

def homePageView(request):
    return HttpResponse('Merhaba Djangosever !')
