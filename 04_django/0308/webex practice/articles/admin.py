from django.contrib import admin
from .models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    # 어떻게 보여 줄건데?
    list_display = (
        'pk', 'title', 'content',
        'created_at', 'updated_at'
        )
# 관리자.사이트.등록(Article)
# 아싸리(어드민 싸이트 레지스터)
admin.site.register(Article, ArticleAdmin)