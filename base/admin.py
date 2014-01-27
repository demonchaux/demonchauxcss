from django.contrib import admin
from base.models import Post, PostImage, Event
from mce_filebrowser.admin import MCEFilebrowserAdmin

class PostImageInline(admin.TabularInline):
    model = PostImage

class PostAdmin(MCEFilebrowserAdmin):
    inlines = (PostImageInline,)

class EventAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Event, EventAdmin)
