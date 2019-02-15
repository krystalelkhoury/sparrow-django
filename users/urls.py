from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('a/dashboard/', views.AdminDashboard.as_view(), name='adashboard'),
    path('e/dashboard/', views.EmployeeDashboard.as_view(), name='edashboard'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
