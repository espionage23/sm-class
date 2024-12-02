from django.shortcuts import render, redirect
from board.models import Board
from django.db.models import Max
from django.contrib import messages
from django.db.models import F

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
    id = request.POST.get('id')
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')

    # no = Board.objects.aggregate(max_bno = Max('bno'))
    # no['max_bno']+1
    # 오라클 sequence.nextval, sequence.currval
    # bno,bsetp,bindent,bhit,bdate: 자동
    # id,btitle,bcontent,bgroup:입력

    # db 저장
    qs = Board.objects.create(id=id, btitle=btitle, bcontent=bcontent)     
    qs.bgroup = qs.bno
    qs.save()

    # 1회 노출
    messages.success(request, message="게시글이 저장되었습니다.")
    # return redirect('board:blist')

    return render(request,'bwrite.html',{'w_msg':'1'})

# 글 상세보기
def bview(request,bno):
  print("게시글 번호 : ",bno)

  # 조회수 1 증가 get방식 : save()로 저장
  # qs = Board.objects.get(bno=bno)
  # qs.bhit = qs.bhit+1
  # qs.save()
  # context = {'board':qs}  # get

  # 조회수 1 증가 filter : update()로 저장
  qs = Board.objects.filter(bno=bno)
  qs.update(bhit=F('bhit')+1)
  context = {'board':qs[0]}  # filter

  return render(request, 'bview.html', context)

# 게시글 수정
def bmodify(request,bno):
  print("게시글 번호 : ",bno)
  if request.method == "GET":
    qs = Board.objects.filter(bno=bno)
    context = {"board":qs[0]}
    return render(request, 'bmodify.html', context)
  else: #post
    bno = request.POST.get('bno')
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')

    # db 저장
    qs = Board.objects.get(bno=bno)     
    qs.btitle = btitle
    qs.bcontent = bcontent
    qs.save()

    # return redirect('board:bview')
    return render(request, 'bmodify.html',{'u_msg':bno})

# 게시글 삭제
def bdelete(request,bno):
  print("게시글 번호 : ",bno)
  Board.objects.get(bno=bno).delete()
  return render(request, 'blist.html',{"d_msg":bno})

# 답변달기
def breply(request,bno):
  if request.method=="GET":
    print("게시글 번호 : ",bno)
    qs = Board.objects.get(bno=bno)
    context = {"board":qs}
    return render(request, 'breply.html', context)
  else:
    bgroup = int(request.POST.get('bgroup')) # str타입
    bstep = int(request.POST.get('bstep'))
    bindent = int(request.POST.get('bindent'))
    id = request.POST.get('id')
    bno = request.POST.get('bno')
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    print("bgroup 번호 :",bgroup)

    # 다른 답변달기에 bstep을 1씩 증가시켜줌.
    qs = Board.objects.filter(bgroup=bgroup, bstep__gt=bstep)
    qs.update(bstep = F('bstep')+1)

    # bgroup : 부모의 bgroup 입력
    Board.objects.create(id=id, btitle=btitle, bcontent=bcontent, bgroup=bgroup, bstep=bstep+1, bindent=bindent+1)

    # return redirect('board:blist')
    return render(request, 'blist.html',{"r_msg":"1"})
