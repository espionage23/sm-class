from django.shortcuts import render, redirect
from member.models import Member
# 로그인 페이지, 로그인 버튼확인
def login(request):
  if request.method == "GET":
    return render(request, 'login.html')
  else:
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    qs = Member.objects.filter(id=id,pw=pw)
    if qs:
      msg = "1"
      request.session['session_id']=id
      # request.session['session_nickname']=qs[0].nickname

      return redirect('index')
    else:
      msg = "0"
      return render(request, 'login.html', {"login_msg":msg})
    
def logout(request):
  request.session.clear()
  return redirect('/')


