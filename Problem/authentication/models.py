from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class MyAccountManager(BaseUserManager):  # BaseUserManager for creating object in the model
    def create_account(self, first_name, last_name, username, password=None):
        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class RegisterTeacher(AbstractBaseUser):
    username = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    classes_taught = models.CharField(max_length=250)
    contact_number = models.CharField(max_length=250)
    teacher_id = models.CharField(max_length=250)
    is_teacher = models.BooleanField(default=True)
    # teacher_adhar_card = models.CharField(max_length=12, blank=True)
    # teacher_aadhaar_file = models.FileField(upload_to='teacher/aadhaar/', blank=True)

    objects = MyAccountManager()

    def __str__(self):
        return self.username


class RegisterStudent(AbstractBaseUser):  # BaseUserManager for creating object in the model
    username = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    standard = models.CharField(max_length=250)
    section = models.CharField(max_length=250)
    stream = models.CharField(max_length=250)
    roll_no = models.CharField(max_length=250)
    student_id = models.CharField(max_length=250)
    is_student = models.BooleanField(default=True)
    # student_adhar_card = models.CharField(max_length=12, blank=True)
    # student_aadhaar_file = models.FileField(upload_to='student/aadhaar/', blank=True)

    objects = MyAccountManager()

    def __str__(self):
        return self.username


class Aadhaar(models.Model):
    aadhaar_number = models.CharField(max_length=12)
    aadhaar_file = models.FileField(upload_to='aadhaar/')


    def __str__(self):
        return self.aadhaar_number
    
class Details(models.Model):
    company_name = models.CharField(max_length=250)
    joining_date = models.DateField()
    last_working_date = models.DateTimeField()
    upload_document = models.FileField(upload_to='details/')

    def __str__(self):
        return self.company_name
