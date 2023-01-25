from django.contrib import admin
from .models import RegisterTeacher, RegisterStudent, Aadhaar
# Register your models here.

admin.site.register(RegisterTeacher)
admin.site.register(RegisterStudent)
admin.site.register(Aadhaar)