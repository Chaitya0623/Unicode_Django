from tkinter import Variable
from django.shortcuts import render, HttpResponse
from binary import ifBinary

# Create your views here.
def index(request):
    return HttpResponse('This is Homepage')

def bin(request,a,b):
    # context = {
    #     'variable': ifBinary(a,b)
    # }
    # return render(request, 'index.html', context)
    return HttpResponse('<h1>The Output is: %s</h1>' %ifBinary(a,b))