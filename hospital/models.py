from django.db import models
from django.contrib.auth.models import User

class UserRole(models.Model):
    CHOICES = (
        ('p', 'patient'),
        ('s', 'staff'),
        ('d', 'doctor'),

    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=200,choices=CHOICES,default='p')


    def __str__(self):
        return self.role


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    mobile = models.CharField(max_length=200)
    image = models.FileField(upload_to='user_image')
    fileno = models.CharField(max_length=200 , default="")
    age = models.CharField(max_length=200, default="")
    dob = models.CharField(max_length=200, default="")
    issue = models.CharField(max_length=200, default="")
    pastissue= models.CharField(max_length=200, default="")
    prescription= models.CharField(max_length=200, default="")

    bill = models.FileField(upload_to='user_image', default="")

    def __str__(self):
        return self.user.username
# class StaffProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     address = models.CharField(max_length=255)
#
#     image = models.FileField(upload_to='user_image')
#     sid = models.CharField(max_length=200, default="")
#     age = models.CharField(max_length=200, default="")
#     dob = models.CharField(max_length=200, default="")
#     department = models.CharField(max_length=200, default="")
#     qualification = models.CharField(max_length=200, default="")
#     designation = models.CharField(max_length=200, default="")
#     number = models.CharField(max_length=200, default="")
#
#     def __str__(self):
#         return self.user.username
# class DoctorProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     address = models.CharField(max_length=255)
#
#     image = models.FileField(upload_to='user_image')
#     experience1 = models.CharField(max_length=200, default="")
#     experience2 = models.CharField(max_length=200, default="")
#     experience3 = models.CharField(max_length=200, default="")
#     # experience4 = models.CharField(max_length=200, default="")
#     # experience5 = models.CharField(max_length=200, default="")
#     # age = models.CharField(max_length=200, default="")
#     # dob = models.CharField(max_length=200, default="")
#     department = models.CharField(max_length=200, default="")
#     qualification1 = models.CharField(max_length=500, default="")
#     qualification2 = models.CharField(max_length=500, default="")
#     qualification3 = models.CharField(max_length=500, default="")
#     # qualification4 = models.CharField(max_length=500, default="")
#     designation = models.CharField(max_length=200, default="")
#     number = models.CharField(max_length=200, default="")
#
#     def __str__(self):
#         return self.user.username

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=200, default="")
    number = models.CharField(max_length=200, default="")
    fileno = models.CharField(max_length=10, default="")

    doa = models.CharField(max_length=200, default="")
    cdoctor = models.CharField(max_length=200, default="")
    timetable = models.CharField(max_length=200, default="")
    def __str__(self):
        return self.user.username


class Contact(models.Model):
    name = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=200, default="")
    subject = models.CharField(max_length=200, default="")
    message = models.CharField(max_length=10, default="")
    def __str__(self):
        return self.name