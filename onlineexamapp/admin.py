from django.contrib import admin
from .models import Contact, User

# Register your models here.
admin.site.register(User)
admin.site.register(Contact)
