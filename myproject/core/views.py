from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Hello, World! මම දැන් Django ඉගෙන ගන්නවා. 🚀")