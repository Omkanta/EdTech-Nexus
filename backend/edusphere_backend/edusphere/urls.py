from django.urls import path
from .views import InstructorListCreateView, InstructorDetailView

urlpatterns = [
    path('instructors/', InstructorListCreateView.as_view(), name='instructor-list'),
    path('instructors/<int:pk>/', InstructorDetailView.as_view(), name='instructor-detail'),
]
