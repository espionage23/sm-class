from django.shortcuts import render, redirect
from board.models import Board
from member.models import Member

# 게시판 리스트
def blist(request):
  qs = Board.objects.all().order_by("-bgroup","bstep")
  context = {"blist":qs}
  return render(request, 'blist.html', context)

## 글쓰기 및 저장
def bwrite(request):
  if request.method=="GET":
    return render(request, 'bwrite.html')
  else:
    id = request.session['session_id']
    member = Member.objects.get(id=id)
    btitle = request.POST.get("btitle")
    bcontent = request.POST.get("bcontent")
    bfile = request.FILES.get("bfile","")

    qs = Board.objects.create(member=member, btitle=btitle, bcontent=bcontent, bfile=bfile)
    qs.bgroup = qs.bno
    qs.save()

    context = {'wmsg':"1"}
    return render(request, 'blist.html', context)

def bview(request,bno):
  print("게시글 번호 : ",bno)
  return render(request, 'bview.html')