from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return render(request, 'blog/blog.html')

def introducingsparrow(request):
    return render(request, 'blog/introducing-sparrow.html')

def ideocollab(request):
    return render(request, 'blog/ideo-collab.html')

# def mothersroom(request):
#     return render(request, 'blog/mothers-room.html')
