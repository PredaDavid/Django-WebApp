from django.contrib import admin

# Register your models here.
from .models import Room, Topic, Message

admin.site.register(Room)  # this will make the Room model visible on the admin page
admin.site.register(Topic)
admin.site.register(Message)