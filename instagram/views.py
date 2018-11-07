from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Image
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    photos=Image.get_photos()
    return render(request,'index.html',{"photos":photos})

def imagedetails(request,image_id):
    try:
        image = Image.objects.get(id=image_id)
    except ObjectDoesNotExist:
         raise Http404()
    return render(request,"image.html",{"image":image})
