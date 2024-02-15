from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.


@admin.register(User)
class CustomUserAdmin(UserAdmin):
  list_display = ("username", "email", "is_business", "grade")
  fieldsets = (
    (None, {"fields": ("username", "password")}),
    (("Personal info"), {"fields": ("first_name", "last_name", "email")}),
    (("Important dates"), {"fields": ("last_login", "date_joined")}),
  )

  # fieldsets = (
  #     (None, {'fields': ('username','password','is_business')}),
  # )

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#   list_display = ['name', 'description', 'age','gender'] 
#   list_filter = ['age', 'gender'] # 마치 카테고리⭐︎
#   search_fields = ['name'] #, 'description', 'age','gender'] 
#   # 나이 성별은 카테고리화 하고, 이름은 검색되게 하고, 자기소개는 그냥 뒀다