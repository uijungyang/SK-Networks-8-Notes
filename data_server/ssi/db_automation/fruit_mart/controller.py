from django.http import JsonResponse
import json
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')