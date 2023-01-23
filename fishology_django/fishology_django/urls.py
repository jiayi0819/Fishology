from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('account.urls')),
    path('api/v1/', include('aquarium.urls')),
    path('api/v1/', include('diary.urls')),
    path('api/v1/', include('fish.urls')),
    path('api/v1/', include('scene.urls')),

    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
