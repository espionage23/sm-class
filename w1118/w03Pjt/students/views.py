from django.shortcuts import render

# 학생정보리스트
def list(request):
  return render(request,'list.html')

# 학생정보입력
def write(request):
  return render(request, 'write.html')