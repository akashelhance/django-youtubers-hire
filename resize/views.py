from django.shortcuts import render
from .forms import UploadForm
from django.http import HttpResponse
from .models import Upload

# Create your views here.
def index(request):
    context ={}
    context['form']= UploadForm()
    return render(request, 'resize/index.html', context)


def submitted(request):
    if(request.POST):
        data = request.POST.dict()
       
        height = data.get("height")
        width = data.get("width")

        image = data.get("img")
        # Check if you get the value
        
        uploaddata = Upload(height=height, width=width, img=image)
        uploaddata.save()
        return HttpResponse("hellos")
    else:
        return render(request, "resize/index.html")