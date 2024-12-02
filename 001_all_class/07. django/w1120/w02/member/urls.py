from django.urls import path
from.import views

app_name='member'
urlpatterns = [
    path('mlist/',views.mlist, name='mlist'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('cookWrite/',views.cookWrite, name='cookWrite'),
    path('cookDelete/',views.cookDelete, name='cookDelete'),
]