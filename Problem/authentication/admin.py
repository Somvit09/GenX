from django.contrib import admin
from .models import RegisterTeacher, RegisterStudent, Aadhaar, Details, TimeSheet
# Register your models here.

admin.site.register(RegisterTeacher)
admin.site.register(RegisterStudent)
admin.site.register(Aadhaar)
admin.site.register(Details)
admin.site.register(TimeSheet)