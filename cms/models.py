from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class Entry(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextUploadingField()  # <-- invece di models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='uploads/images/')
    caption = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Image for {self.entry.title}"

class Video(models.Model):
    VIDEO_TYPE_CHOICES = (
        ('file', 'File'),
        ('youtube', 'YouTube'),
    )

    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name='videos')
    type = models.CharField(max_length=10, choices=VIDEO_TYPE_CHOICES, default='file')
    video_file = models.FileField(upload_to='uploads/videos/', blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    caption = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Video for {self.entry.title}"
