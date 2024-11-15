from django.urls import path, include
from . import views

app_name = 'students'
urlpatterns = [
    # url 주소 / views.함수명,  url 이름
    # http://127.0.0.1:8000/students/reg
    # students:reg
    path('reg/',views.regStudent,name='reg'),
]
