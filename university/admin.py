from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Faculty, Department, Group, Student, Subject, Teacher

admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Teacher)
