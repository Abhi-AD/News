from django.contrib import admin
from news_app.models import Post,Category,Tag,Contact,UserProfile,Newsletter

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Contact)
admin.site.register(UserProfile)
admin.site.register(Newsletter)