from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Project, Offer, Review, Comment

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Offer)
admin.site.register(Review)
admin.site.register(Comment)
