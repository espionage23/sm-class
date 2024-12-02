from django.urls import path, include
from.import views

app_name = ''
urlpatterns = [
        #url 링크,  views 함수호출, name링크
    path('', views.index, name='index'),
]
