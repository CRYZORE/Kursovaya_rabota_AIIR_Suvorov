from django.http import HttpResponse
from django.shortcuts import render
from django import forms
import summary.sum

# Create your views here.


def index(request, s):
    return HttpResponse(f'<h1>Произведена замена текста: {summary.sum.summary(s)}</h1>')