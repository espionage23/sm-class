from django.urls import path
from.import views

app_name='board'
urlpatterns = [
    path('board', views.board, name='board'),
]
