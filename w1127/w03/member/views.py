from django.shortcuts import render
from django.views.decorators.csrf import  csrf_exempt
from django.http import HttpResponse, JsonResponse
from member.models import Member
from django.core import serializers   # json타입 변경할때 사용

### 로그인
def login(request):
  return render(request, 'login.html')


### ajax 통신
# csrf_token
# @csrf_exempt #csrf _token 예외처리
def loginChk(request):
  # {"name":"kim","age":20}
  id = request.POST.get('id','')
  pw = request.POST.get('pw','')
  print("html에서 넘어온 데이터 : ",id, pw)

  # # 변수 보내는 방법
  # qs = Member.objects.filter(id=id, pw=pw)
  # if qs:
  #   context = {"id":qs[0].id, "nicName":qs[0].nicName, "pw":pw, "result":"success"}
  # else:
  #   context = {"result":"fail"}
  # return JsonResponse(context)

  # filter검색 객체 보내는 방법 - list 타입으로 보내야 함. (타입에러 발생)
  # qs = list(Member.objects.filter(id=id, pw=pw).values())
  # if qs:
  #   context = {"member":qs, "result":"success"}
  # else:
  #   context = {"result":"fail"}
  # return JsonResponse(context)

  # get검색 객체 보내는 방법 (타입에러 발생)
  # qs = Member.objects.filter(id=id, pw=pw)
  # json_qs = serializers.serialize('json',qs)
  # if qs:
  #   context = {"member":json_qs, "result":"success"}
  # else:
  #   context = {"result":"fail"}
  # return JsonResponse(context)
  
def join01(request):
  return render(request, 'join01.html')

def join02(request):
  return render(request, 'join02.html')

# ajax 통신
def idchk(request):
  id = request.POST.get('id')
  print("ID : ",id)
  context = {"id":id, "result":"success"}
  return JsonResponse(context)


