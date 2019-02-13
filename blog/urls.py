from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='blog'),
    path('introducing-sparrow', views.introducingsparrow, name='blog-introducing-sparrow'),
]
