from django.contrib import admin
# from home.models import Member
# Register your models here.
from .models import changes, slots, featuredMatches

admin.site.register(changes)
admin.site.register(slots)
admin.site.register(featuredMatches)