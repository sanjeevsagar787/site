from django.contrib import admin 
from Blogs.models import Post

# Register your models here.
#admin.site.register(BlogComment)
@admin.register(Post)


class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tiny.js',)