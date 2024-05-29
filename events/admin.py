from django.contrib import admin

from users.models import CustomUser
from .models import Event

class EventAdmin(admin.ModelAdmin):
 model = CustomUser


admin.site.register(Event, EventAdmin)
