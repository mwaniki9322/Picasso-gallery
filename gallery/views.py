from django.shortcuts import render
from django.http import HttpResponse
from . models import Image

# Create your views here.

from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    return render(request,'index.html')

def images(request):
    images=Image.display_all_images()

    return render(request,'all-images/images.html',{"images":images},)