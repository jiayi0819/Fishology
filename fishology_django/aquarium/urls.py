from django.urls import path
from aquarium import views

urlpatterns = [
    path('create-aquarium/', views.createAquarium),
    path('update-aquarium/<slug:aquarium_id>/', views.updateAquarium),
    path('update-aquarium-sky/<slug:aquarium_id>/<slug:sky_name>/',
         views.updateAquariumSky),
    path('update-aquarium-scene/<slug:aquarium_id>/<slug:scene_name>/',
         views.updateAquariumScene),
    path('aquariums/', views.AquariumList.as_view()),
    # path('aquariums/<slug:user_name>', views.AquariumList.as_view()),
    path('aquarium/<slug:aquarium_id>/', views.AquariumInfo.as_view()),
]
