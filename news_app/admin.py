from django.contrib import admin
from news_app.models import Post,Category,Tag,Contact,Comment,UserProfile,Newsletter

from django_summernote.admin import SummernoteModelAdmin
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)
# Register your models here.
# admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(Newsletter)