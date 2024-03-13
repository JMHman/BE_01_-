from django.contrib import admin
from .models import Feed
from reviews.models import Review

# Register your models here.

@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):


  def get_reviews(self, obj):
    return ", ".join([review.content for review in obj.reviews.all()]) if obj.reviews.exists() else "빈 채팅방"

  list_display = ('title', 'get_reviews')
  readonly_fields = ('get_reviews',)
  fieldsets = (
    (None, {'fields': ('title',)}),
  )