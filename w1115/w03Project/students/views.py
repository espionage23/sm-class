from django.shortcuts import render
from students.models import Student
from django.http import HttpResponseRedirect
from django.urls import reverse

def write(request):
  print("학생등록페이지")
  return render(request,'stu_write.html')

def save(request):
  if request.POST:
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']
    print("이름 :",name)
    print("전공 :",major)
    print("학년 :",grade)
    print("나이 :",age)
    print("성별 :",gender)
    qs = Student(s_name = name, s_major = major, s_grade = grade, s_age = age, s_gender = gender)
    qs.save()
  return HttpResponseRedirect(reverse('index'))


