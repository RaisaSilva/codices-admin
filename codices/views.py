from django.http import HttpResponse
from django.shortcuts import render, render_to_response


def inicio(request):
    return render_to_response("codices/inicio.html")


# Create your views here.
