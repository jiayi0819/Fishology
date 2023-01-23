from django.urls import path
from fish import views

urlpatterns = [
    path('fishes/', views.FishList.as_view()),
    # path('fishes/')
]
