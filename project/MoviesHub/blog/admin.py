from django.contrib import admin

from .models import post,Comment,Category,profile

admin.site.register(post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(profile)


