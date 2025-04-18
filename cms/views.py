from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Entry

# 🔹 API JSON per TouchDesigner
def entry_list(request):
    data = []
    for entry in Entry.objects.all().order_by('-created_at'):
        images = [
            request.build_absolute_uri(image.image.url)
            for image in entry.images.all()
        ]
        videos = []
        for video in entry.videos.all():
            if video.type == 'file' and video.video_file:
                url = request.build_absolute_uri(video.video_file.url)
            elif video.type == 'youtube' and video.youtube_url:
                url = video.youtube_url
            else:
                url = ''
            videos.append(url)

        data.append({
            'id': entry.id,
            'title': entry.title,
            'body': entry.body,
            'images': images,
            'videos': videos,
            'created_at': entry.created_at,
        })

    return JsonResponse(data, safe=False)

# 🔹 Homepage con lista pubblica
def public_entry_list(request):
    entries = Entry.objects.all().order_by('-created_at')
    return render(request, 'cms/entry_list.html', {'entries': entries})

# 🔹 Dettaglio singola voce
def public_entry_detail(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    return render(request, 'cms/entry_detail.html', {'entry': entry})
