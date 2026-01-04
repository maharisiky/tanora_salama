from django.contrib import admin

from .models import User, Messages, QuickReply

admin.site.register(User)
admin.site.register(Messages)
admin.site.register(QuickReply)