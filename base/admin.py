from django.contrib import admin
from base.models import Post, PostImage
from mce_filebrowser.admin import MCEFilebrowserAdmin

class PostImageInline(admin.TabularInline):
    model = PostImage

class PostAdmin(MCEFilebrowserAdmin):
    inlines = (PostImageInline,)


admin.site.register(Post, PostAdmin)
