from django.urls import path
from.import views

app_name='students'
urlpatterns = [
    path('write/',views.write, name='write'),
    path('list/',views.list, name='list'),
    path('<str:name>/view/',views.view, name='view'),
    path('update/',views.update, name='update'),
    path('delete/<str:name>/',views.delete, name='delete'),
]
