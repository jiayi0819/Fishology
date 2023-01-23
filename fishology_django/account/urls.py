from django.urls import path
from account import views

urlpatterns = [
    # path('users/', views.UserList.as_view()),
    path('users/<slug:username>/', views.UserInfo.as_view()),
    path('update-user/', views.updateUser),
    path('search-user/<slug:username>/', views.searchUser)
]
