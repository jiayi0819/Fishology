from django.contrib import admin
from scene.models import Scene
from scene.models import Prop
from scene.models import Sky

admin.site.register(Scene)
admin.site.register(Sky)
admin.site.register(Prop)
