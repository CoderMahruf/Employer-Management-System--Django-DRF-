from django.urls import path
from .views import EmployerListCreate, EmployerDetail

urlpatterns = [
    path('', EmployerListCreate.as_view()),
    path('<int:pk>/', EmployerDetail.as_view()),
]
