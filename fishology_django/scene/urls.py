from django.urls import path
from scene import views

urlpatterns = [
    path('scenes/', views.SceneList.as_view()),
    path('skies/', views.SkyList.as_view()),
    path('props/<slug:scene_name>/', views.PropList.as_view()),
]
