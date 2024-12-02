from django.shortcuts import render
from member.models import Member

def m2(request):
  if request.method == "GET":
    # 읽어오기
    m_memberId = request.COOKIES.get('m_memberId','')
    m_money = request.COOKIES.get('m_money','')
    m_option = request.COOKIES.get('m_option','')
    context = {'m_memberId':m_memberId,'m_money':m_money, 'm_option':m_option}
    return render(request, 'm2.html', context)
  else:
    # 쿠키저장
    memberId = request.POST.get('memberId')
    money = request.POST.get('money')
    option = request.POST.get('option')
    saveMember = request.POST.get('saveMember')
    print(memberId, money, option, saveMember)
    response = render(request, 'index.html')

    if saveMember is not None:
      response.set_cookie('m_memberId',memberId)
      response.set_cookie('m_money',money)
      response.set_cookie('m_option',option)
    else:
      response.delete_cookie('m_memberId',memberId)
      response.delete_cookie('money',money)
      response.delete_cookie('m_option',option)
  return response



def product(request):
  if request.method == "GET":
    # 쿠키 읽어오기
    c_pId = request.COOKIES.get('c_pId','')
    c_pName = request.COOKIES.get('c_pName','')
    context = {'c_pId':c_pId,'c_pName':c_pName}
    return render(request, 'product.html', context)
  else:
    # 쿠키저장
    pId = request.POST.get('pId')
    pName = request.POST.get('pName')
    pOption = request.POST.get('pOption')
    saveProduct = request.POST.get('saveProduct')
    print(pId,pName,pOption,saveProduct)
    response = render(request, 'index.html')

    if saveProduct is not None: # 체크가 되어 있으면
      # 쿠키저장
      response.set_cookie('c_pId',pId,max_age=60*60)
      response.set_cookie('c_pName',pName,max_age=60*60)
    else:
      response.delete_cookie('c_pId')
      response.delete_cookie('c_pName')
    return response


def login2(request):
  if request.method == "GET":
    cookId = request.COOKIES.get('cookId','')
    print("cookId : ",cookId)
    context = {'cookId':cookId}
    return render(request, 'login2.html', context)
    
  else:
    response = render(request, 'index.html')

    # 3개 정보
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    saveId = request.POST.get('saveId')
    if saveId is not None:
      response.set_cookie('cookId',id,max_age=60*60)
    else:
      response.delete_cookie('cookId')

    return response



# 회원전체 리스트 페이지
def mlist(request):
  qs = Member.objects.all()
  context = {"mlist":qs}
  return render(request, 'mlist.html', context)

# 로그인 페이지
## 쿠키정보 검색 : request.COOKIES.get('이름')
## 쿠키저장      : responese.set_cookie('key','value')
## 쿠키삭제     : responese.delete_cookie('key)
def login(request):
  if request.method == 'GET':
    print("쿠키정보 : ",request.COOKIES)
    print("cookinfo 정보 : ",request.COOKIES.get('cookinfo'))
    saveId = request.COOKIES.get('saveId','')
    print("saveId :",saveId)
    context = {"saveId":saveId}
    response = render(request, 'login.html', context)
    # 쿠키 설정(저장)
    # max_age : 60초 * 60분 후 삭제, max_age가 없으면 브라우저 종료시 삭제
    # 1달 : 60초*60분*24시간*30일
    # 쿠키정보 검색
    if not request.COOKIES.get('cookinfo'):
      response.set_cookie('cookinfo','1111',max_age=60*60)
    return response
  else:
    print("쿠키정보 : ",request.COOKIES)
    id = request.POST.get("id")
    pw = request.POST.get("pw")
    saveId = request.POST.get("saveId","값없음")
    print("전달받은 정보 : ",id,pw,saveId)
    response = render(request, 'login.html')
    # 아이디 기억하기 정보가 있으면
    if saveId is not None :
      response.set_cookie('saveId',id,max_age=60*60) # 아이디 기억하기 체크가 있으면 쿠키저장
    else:
      response.delete_cookie('saveId') # 아이디 기억하기 체크가 없으면 삭제

    return response
