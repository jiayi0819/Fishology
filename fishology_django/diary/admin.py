from django.contrib import admin
from diary.models import Diary, Mood, Weather

admin.site.register(Diary)
admin.site.register(Mood)
admin.site.register(Weather)
