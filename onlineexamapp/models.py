from django.db import models

# Create your models here.
class User(models.Model): # STUDENT
    userType = models.CharField(max_length = 100, default = "Student")
    fname = models.CharField(max_length = 100)
    lname = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    mobile = models.CharField(max_length = 100)
    course = models.CharField(max_length = 100, default="")
    gender = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    address = models.TextField()
    profilePic = models.ImageField(upload_to = 'profilePic/', default="")
    userStatus = models.CharField(max_length = 100, default = "Pending")

    def __str__(self):
        return self.userType + ' --> ' + self.fname + ' ' + self.lname + ' --> ' + self.email

class Contact(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    mobile = models.CharField(max_length = 100)
    message = models.TextField()

    def __str__(self):
        return self.name + ' --> ' + self.email

class CourseDetail(models.Model):
    facultyDetail = models.ForeignKey(User, on_delete=models.CASCADE)
    courseName = models.CharField(max_length = 100)

    def __str__(self):
        return self.facultyDetail.fname + ' --> ' + self.courseName