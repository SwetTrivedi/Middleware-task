from django.contrib import admin
from .models import Post
from .models import Userinfo

# Register your models here.
@admin.register(Post)
class PostAdmin (admin.ModelAdmin):
    list_display=('id','title','desc')


@admin.register(Userinfo)
class UserinfoAdmin(admin.ModelAdmin):
    list_display=('id','clientip','clientcount','clientname','clienttime','clienturl','clientview')
