from django.shortcuts import render, redirect
from board.models import Board
from member.models import Member
from django.db.models import F
from datetime import datetime

# 게시판 리스트
def blist(request):
  qs = Board.objects.all().order_by("-bgroup","bstep")
  context = {"blist":qs}
  return render(request, 'blist.html', context)

# 글쓰기페이지, 글쓰기 저장
def bwrite(request):
  if request.method == "GET":
    return render(request, 'bwrite.html')
  else:
    # id = request.POST.get('id')
    # bgroup, bstep, bindent, bhit, bdate 자동입력
    id = request.session.get('session_id') #session_id의 id값을 가져옴.
    member = Member.objects.get(id=id)
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    bfile = request.FILES.get('bfile','')
    print("파일이름 : ",request.FILES)
    print("파일이름2 : ",bfile)

    # DB 저장 - AutoField: 번호생성
    qs = Board.objects.create(member=member, btitle=btitle, bcontent=bcontent, bfile=bfile)
    qs.bgroup = qs.bno
    qs.save()

    context = {"wmsg":"1"}
    return render(request, 'bwrite.html', context)

### 글 상세보기 - 조회수 증가 방지, 이전글, 다음글
def bview(request,bno):
  # get 형태
  # qs = Board.objects.get(bno=bno)
  # qs.bhit += 1
  # qs.save()
  # context = {"board":qs}

  # 쿠키 사용 기간 - 1일동안 유지
  ## 11월 25일 23시 59분 0초 
  tomorrow = datetime.replace(datetime.now(),hour=23,minute=59,second=0)
  # 쿠키설정포맷  strftime: 시간포맷형태
  expires = datetime.strftime(tomorrow,"%a,%d-%b-%Y %H:%M:%S GMT")


  # filter() 형태 update()명령어가 존재함.
  # F함수 - 필드 값을 참조
  qs = Board.objects.filter(bno=bno)
  # 이전글
  # prev_qs = Board.objects.filter().order_by("-bgroup","bsetp").first()
  # 다음글
  # next_qs = Board.objects.filter().order_by("bgroup","-bsetp").first()

  context = {"board":qs[0]}
  # 조회수를 증가하면, cookie_name 증가한 게시글 번호를 추가
  response = render(request, 'bview.html', context)

  # cookie_name가 존재하면 
  print("cookie_name :", request.COOKIES.get('cookie_name'))
  if request.COOKIES.get('cookie_name') is not None:
    ## 쿠키를 읽어와서 안에 1|3|4 -> 2이면 1 증가, 3이면 증가X
    cookies = request.COOKIES.get('cookie_name')
    cookies_list = cookies.split("|")

    if str(bno) not in cookies_list:
      # 1|3|4 번중에 -> 2 선택시, 1|3|4|2 순으로 저장
      # 번호가 없으면 번호를 추가
      response.set_cookie('cookie_name',cookies+f'|{bno}',expires=expires)
      qs.update(bhit = F('bhit')+1)
      
  else:   # cookie_name가 존재하지 않으면, 처음으로 게시글 조회
    print("없으면")
    response.set_cookie('cookie_name',bno, expires=expires)
    qs.update(bhit = F('bhit')+1)

  return response

# 게시글 삭제
def bdelete(request,bno):
  qs = Board.objects.get(bno=bno)
  qs.delete()
  context = {"dmsg":bno}
  return render(request, 'blist.html', context)


# 게시글 수정
def bupdate(request,bno):
  if request.method == "GET":
    qs = Board.objects.get(bno=bno)
    context = {"board":qs}
    return render(request, 'bupdate.html',context)
  else:
    bno = request.POST.get("bno")
    btitle = request.POST.get("btitle")
    bcontent = request.POST.get("bcontent")
    qs = Board.objects.get(bno=bno)
    qs.btitle=btitle
    qs.bcontent=bcontent
    qs.save()
    return redirect('board:bview',bno)


def breply(request,bno):
  if request.method == "GET":
    qs = Board.objects.get(bno=bno)
    context = {"board":qs}
    return render(request, 'breply.html',context)
  else:
    id = request.POST.get("id")
    member = Member.objects.get(id=id)
    bgroup = int(request.POST.get("bgroup"))  # 답글 그룹핑
    bstep = int(request.POST.get("bstep"))   # 답글 순서
    bindent = int(request.POST.get("bindent"))   # 들여쓰기
    btitle = request.POST.get("btitle") 
    bcontent = request.POST.get("bcontent") 

    # 같은 bgroup에서 bstep 더 큰것만 검색해서, 데이터 1씩 증가
    qs = Board.objects.filter(bgroup=bgroup, bstep__gt=bstep)
    qs.update(bstep = F('bstep')+1)

    qs = Board(member=member, btitle=btitle, bcontent=bcontent, bgroup=bgroup, bstep=bstep+1, bindent=bindent+1)
    qs.save()
    context = {'rmsg':"1"}
    return render(request, 'breply.html',context)
