from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def add_relationships(request):
    student_1 = Student.objects.get(id=1)
    student_2 = Student.objects.get(id=2)
    student_3 = Student.objects.get(id=3)
    teacher_1 = Teacher.objects.get(id=1)
    teacher_2 = Teacher.objects.get(id=2)
    teacher_3 = Teacher.objects.get(id=3)
    student_1.teachers.add(teacher_1)
    student_1.teachers.add(teacher_2)
    student_1.teachers.add(teacher_3)
    student_2.teachers.add(teacher_1)
    student_2.teachers.add(teacher_2)
    student_3.teachers.add(teacher_2)
    student_3.teachers.add(teacher_3)

    return HttpResponse('Связи добавлены')
def students_list(request):
    template = 'school/students_list.html'

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'name'

    object_list = Student.objects.all().order_by(ordering).prefetch_related('teachers')
    context = {'object_list': object_list}
    return render(request, template, context)
