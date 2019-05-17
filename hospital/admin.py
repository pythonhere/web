from django.contrib import admin
from .models import Profile, Appointment, Contact

# Register your models here.

admin.site.register(Profile)
# admin.site.register(UserRole)
# admin.site.register(StaffProfile)
admin.site.register(Appointment)
# admin.site.register(DoctorProfile)
admin.site.register(Contact)
