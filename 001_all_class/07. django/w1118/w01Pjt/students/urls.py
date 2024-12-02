from django.urls import path, include
from . import views

app_name = 'students'       ## name : url 연결시 사용
urlpatterns = [
    # 리스트
    path('list/', views.list, name='list'), # 학생성적리스트
    # 저장
    path('write/', views.write, name='write'), # 학생입력페이지
    # 상세
    path('<str:name>view/', views.view, name='view'), # 학생 상세 페이지 <int:no>
    # 수정 1,2,3 -수정1
    path('<str:name>/modify/', views.modify, name='modify'), # 학생수정페이지
    path('modify2/', views.modify2, name='modify2'), # 학생수정페이지2
    path('<str:name>/modify3/', views.modify3, name='modify3'), # 학생수정페이지3

    # 삭제
    path('<str:name>/delete/', views.delete, name='delete'), # 학생삭제
    


    # path('dowrite/', views.dowrite, name='dowrite'), # 학생입력페이지
]
