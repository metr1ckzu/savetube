from django.shortcuts import render, redirect
from .models import Saver

from youtube_dl import YoutubeDL


def submit(request):
    template_name = 'downloader/index.html'

    if request.method == 'POST':

        source = request.POST['source_url']
        source_log = Saver(source_link=source)
        source_log.save()

        with YoutubeDL(dict(forceurl=True)) as ydl:
            video_info = ydl.extract_info(source, download=False)
            video_url = video_info['formats'][-1]['url']
            return redirect(video_url)


    return render(request, template_name)
