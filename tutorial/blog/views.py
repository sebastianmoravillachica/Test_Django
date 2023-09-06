from django.shortcuts import render,HttpResponse


def home(request):
    return HttpResponse("<h1>Bienvenido a mi blog</<h1>")
