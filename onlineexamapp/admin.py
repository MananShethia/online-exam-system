from django.contrib import admin
from .models import Contact, FacultyCourses, TestResult, User, CourseDetail, QuestionDetail

# Register your models here.
admin.site.register(User)
admin.site.register(Contact)
admin.site.register(CourseDetail)
admin.site.register(QuestionDetail)
admin.site.register(TestResult)
admin.site.register(FacultyCourses)
