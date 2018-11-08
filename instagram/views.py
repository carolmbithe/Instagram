from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image
from django.core.exceptions import ObjectDoesNotExist
from .forms import NewImageForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    photos=Image.get_photos()
    return render(request,'index.html',{"photos":photos})

def imagedetails(request,image_id):
    try:
        image = Image.objects.get(id=image_id)
    except ObjectDoesNotExist:
         raise Http404()
    return render(request,"image.html",{"image":image})

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user=request.user
    if request.method == 'POST':
        form =NewImageForm(request.POST,request.FILES)
        if form.is_valid():
            image=form.save(commit=False)
            image.profile = current_user
            image.save()
        return redirect('index')
    else:
        form=NewImageForm()
    return render(request,'new_image.html',{"form":form})
