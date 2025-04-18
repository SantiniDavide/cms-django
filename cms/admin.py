from django.contrib import admin
from .models import Entry, Image, Video

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class VideoInline(admin.TabularInline):
    model = Video
    extra = 1

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    inlines = [ImageInline, VideoInline]

admin.site.register(Image)
admin.site.register(Video)
