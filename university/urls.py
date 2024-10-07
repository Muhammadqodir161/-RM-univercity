from django.urls import path
from .views import (
    faculty_list, faculty_create, faculty_update, faculty_delete,
    department_list, department_create, department_update, department_delete,
    group_list, group_create, group_update, group_delete,
    student_list, student_create, student_update, student_delete,
    subject_list, subject_create, subject_update, subject_delete,
    teacher_list, teacher_create, teacher_update, teacher_delete,dashboard,
)

urlpatterns = [
     path('', dashboard, name='dashboard'),
    
    path('faculties/', faculty_list, name='faculty_list'),
    path('faculties/create/', faculty_create, name='faculty_create'),
    path('faculties/update/<int:pk>/', faculty_update, name='faculty_update'),
    path('faculties/delete/<int:pk>/', faculty_delete, name='faculty_delete'),

    path('departments/', department_list, name='department_list'),
    path('departments/create/', department_create, name='department_create'),
    path('departments/update/<int:pk>/', department_update, name='department_update'),
    path('departments/delete/<int:pk>/', department_delete, name='department_delete'),

    path('groups/', group_list, name='group_list'),
    path('groups/create/', group_create, name='group_create'),
    path('groups/update/<int:pk>/', group_update, name='group_update'),
    path('groups/delete/<int:pk>/', group_delete, name='group_delete'),

    path('students/', student_list, name='student_list'),
    path('students/create/', student_create, name='student_create'),
    path('students/update/<int:pk>/', student_update, name='student_update'),
    path('students/delete/<int:pk>/', student_delete, name='student_delete'),

    path('subjects/', subject_list, name='subject_list'),
    path('subjects/create/', subject_create, name='subject_create'),
    path('subjects/update/<int:pk>/', subject_update, name='subject_update'),
    path('subjects/delete/<int:pk>/', subject_delete, name='subject_delete'),

    path('teachers/', teacher_list, name='teacher_list'),
    path('teachers/create/', teacher_create, name='teacher_create'),
    path('teachers/update/<int:pk>/', teacher_update, name='teacher_update'),
    path('teachers/delete/<int:pk>/', teacher_delete, name='teacher_delete'),
]