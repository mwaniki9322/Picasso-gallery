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

def search_results(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print(searched_images)
        return render(request, 'all-images/search.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'all-images/search.html', {"message": message})


