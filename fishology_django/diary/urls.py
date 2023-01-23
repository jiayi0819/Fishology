from django.urls import path
from diary import views


urlpatterns = [
    path('diaries/<slug:aquarium_id>/', views.AquariumDiary.as_view()),
    path('diaries/filter/<slug:aquarium_id>/', views.FilterDiary),
    path('moods/', views.MoodList.as_view()),
    path('weathers/', views.WeatherList.as_view()),
    path('submit-diary/', views.submitDiary),

    path('diary-count-list/<slug:aquarium_id>/<slug:range_type>/<int:index>',
         views.DiaryCountList.as_view()),
    path('diary-mood-list/<slug:aquarium_id>/<slug:range_type>/<int:index>',
         views.DiaryMoodList.as_view())

]
