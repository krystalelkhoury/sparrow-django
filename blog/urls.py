from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='blog'),
    path('introducing-sparrow', views.introducingsparrow, name='blog-introducing-sparrow'),
    path('ideo-collab', views.ideocollab, name='blog-ideo-collab'),
    # path('mothers-room', views.mothersroom, name='blog-mothers-room')
]
