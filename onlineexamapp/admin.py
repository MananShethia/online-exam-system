from django.contrib import admin
from .models import Contact, User, CourseDetail, QuestionDetail

# Register your models here.
admin.site.register(User)
admin.site.register(Contact)
admin.site.register(CourseDetail)
admin.site.register(QuestionDetail)
