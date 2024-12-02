from django.contrib import admin
from django.urls import path, include

app_name='students'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('', include('home.urls')),
    path('board/', include('board.urls')),
]
