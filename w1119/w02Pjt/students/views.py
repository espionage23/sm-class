from django.shortcuts import render, redirect
from students.models import Student
from django.urls import reverse
# 1. 학생정보등록, 2. 학생정보 저장
def write(request):
  if request.method == "POST":
    name =request.POST.get("name")
    major =request.POST.get("major")
    grade =request.POST.get("grade")
    age =request.POST.get("age")
    gender =request.POST.get("gender")
    hobbys =request.POST.getlist("hobby")

    # qs.save()
    qs = Student(name=name, major=major, grade=grade, age=age, gender=gender, hobby=hobbys)
    qs.save()

    return redirect('/students/list')

  return render(request, 'write.html')

# 3. 학생리스트
def list(request):
  # 학생 정보 가져오기
  qs = Student.objects.all()
  context = {"slist":qs}
  return render(request, 'list.html',context)

# 4 상세보기
def view(request,name):
  qs = Student.objects.get(name=name)
  context = {"stu":qs}
  return render(request, 'view.html',context)

# 5. 정보수정 및 업데이트
def update(request):
  if request.method == "GET":
    name = request.GET['name']
    qs = Student.objects.get(name=name)
    context = {"stu":qs}
    return render(request, 'update.html',context)
  else:
    name =request.POST.get("name")
    major =request.POST.get("major")
    grade =request.POST.get("grade")
    age =request.POST.get("age")
    gender =request.POST.get("gender")
    hobby =request.POST.getlist("hobby")

    # Student 검색
    qs = Student.objects.get(name=name)
    qs.major = major
    qs.grade = grade
    qs.age = age
    qs.gender = gender
    qs.hobby = hobby
    qs.save()

    return redirect('students:view',name)


# 6. 데이터 삭제
def delete(request,name):
  print("삭제정보 이름 : ",name)
  qs = Student.objects.get(name=name).delete()
  return redirect('/students/list')