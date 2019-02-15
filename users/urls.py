from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('a/dashboard/', views.AdminDashboard.as_view(), name='adashboard'),
    path('e/dashboard/', views.EmployeeDashboard.as_view(), name='edashboard'),
]
