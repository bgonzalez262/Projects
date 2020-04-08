from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact

# Create your views here.
def index(request):
    return render(request,'vba/index.html')