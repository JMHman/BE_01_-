from django.contrib import admin
from .models import Board
# Register your models here.

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
  list_display = ('title', 'writer','date','likes','updated_at','created_at',)
  list_filter = ('date','likes',)
  search_fields = ('title', 'content',)
  ordering = ('-date',) #'likes',) date 는 시간순(오래된 순), -date 는 시간역순(최신 순)
  readonly_fields = ('writer',) # readonly 수정 불가
  fieldsets = (
    (None, {'fields': ('title', 'content',)}), # None 은 내용 없음 이라 표시가 없고 다른걸로 하면 표시가 나옴
    ('Advanced options(TEXT 변경 가능)', {'fields': ('writer', 'likes', 'reviews'), 'classes': ('collapse',)}),
  ) # fieldsets 는 상세페이지에서 데이터 관리를 쉽게 해주는 옵션 게시글 안에서 구역을 나눠서 관리하게 해줌
  # fieldsets > 'classes':('collapse',) 는 아마도 숨김 기능, 튜플임을 명심하고 마지막에 ,따옴표 꼭 확인

  list_per_page = 10 # 페이지에 표시할 게시글의 갯수
  
  actions = ('increment_likes',) # 함수를 만들어서 여기 담으면 사용할수 있다

  def increment_likes(self, request, queryset):
    # 선택된 게시글들에 대해 'likes' 수를 1씩 증가
    for board in queryset: # 이 함수의 기능을 정한 거
      board.likes += 1
      board.save()
  increment_likes.short_description = "선택된 게시글의 좋아요 수 증가" # 이 옵션을 뭐라 부를지 정한거