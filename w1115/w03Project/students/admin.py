from django.contrib import admin
from students.models import Student

## admin 관리자페이지에서 보여지는 컬럼 부분 설정
class StudentAdmin(admin.ModelAdmin):
  list_display = ['s_name','s_major','s_age']

### admin 사이트에 추가
admin.site.register(Student,StudentAdmin)

