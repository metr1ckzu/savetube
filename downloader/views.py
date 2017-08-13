from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from downloader.models import Saver
from youtube_dl import YoutubeDL


class IndexView(TemplateView):
    template_name = 'downloader/index.html'

    def redirect(request):
        source_link = Saver()
        source_link.source_url = request.POST['source_url']
        source_link.save()
        return render_to_response('downloader/saver_page.html')

    def saver_link(request):
        source_link = Saver()
        dest_link = YoutubeDL().extract_info(source_link, download=False)
        return dest_link
        #return HttpResponse({ % dest_link %})

class SaveView(TemplateView):
    template_name = 'downloader/saver_page.html'
