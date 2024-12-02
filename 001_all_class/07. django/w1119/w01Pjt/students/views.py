from django.shortcuts import render, redirect
from django.urls import reverse
from students.models import Student

# 1. 학생입력페이지 열기, 2. 학생정보저장
def write(request):
  if request.method == "POST":
    name = request.POST.get('name')   # 데이터가 없을때 None
    major = request.POST.get('major')
    grade = request.POST['grade']   # 데이터가 없을때 error
    age = request.POST['age']   
    gender = request.POST['gender'] 
    # hobby = request.POST['hobby']   # 1개만 가져옴.
    hobbys = request.POST.getlist('hobby')    # checkbox 데이터 가져오기
    # hobby = ','.join(hobbys)      # list -> str 타입으로 변경
    # hobby_list = hobby.split(",") # str -> list 타입으로 변경

    print(name)
    # print("hobby 단수:",hobby)
    print("hobbys 복수:",hobbys)
    
    ## qs.save()
    qs =Student(name=name, major=major, grade=grade, age=age, gender=gender, hobby=hobbys)
    qs.save()

    # ## create()  # 이 방법은 save()가 필요없다.
    # Student.objects.create(name=name, major=major, grade=grade, age=age, gender=gender, hobby=hobbys)

    return redirect('/students/list')
  else: #GET 호출
    return render(request, 'write.html')

# 3. 학생리스트
def list(request):
  # 학생전체정보 가져오기
  qs = Student.objects.order_by('-grade','name')   # 정렬
  context = {"slist":qs}
  return render(request, 'list.html',context)

# 4. 학생상세보기
def view(request,name):
  qs = Student.objects.get(name=name)
  context = {"stu":qs}
  return render(request, 'view.html',context)


# 5. 학생수정페이지, 6. 학생수정저장
def update(request):
  if request.method == "GET":
    name = request.GET['name']
    print(name)
    qs = Student.objects.get(name=name)
    context= {"stu":qs}
    return render(request, 'update.html',context)
  else:
    name = request.POST.get('name')
    major = request.POST.get('major')
    grade = request.POST.get('grade')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    hobby = request.POST.getlist('hobby')

    #Student 검색
    qs = Student.objects.get(name=name)
    qs.major = major
    qs.grade = grade
    qs.age = age
    qs.gender = gender
    qs.hobby = hobby
    qs.save()

    return redirect('students:view',name)   # 약식
    # return redirect(reverse('students:view',args=(name,)))  # 정규 표현식

# 7. 학생정보삭제
def delete(request,name):
  print("삭제정보 이름 : ",name)
  qs = Student.objects.get(name=name).delete()
  return redirect('/students/list')

# 8. 학생검색
def search(request):
  search = request.GET.get('search')
  print("검색 단어 search :",search)
  # 데이터검색부분
  qs = Student.objects.filter(name__contains=search)
  context = {"slist":qs}
  return render(request, 'list.html', context)