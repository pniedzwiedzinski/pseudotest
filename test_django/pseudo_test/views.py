from django.shortcuts import render
from django.http import HttpResponse

def send_answer(request):
    return HttpResponse("Forma do wysyłania")