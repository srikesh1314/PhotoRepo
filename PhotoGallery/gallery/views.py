from django.shortcuts import render
from .models import Photo

# Create your views here.
def photo_view(request):
    query_set = Photo.objects.all()
    context = {
        "photos": query_set
    }
    return render(request,"gallery/photo.html", context)
