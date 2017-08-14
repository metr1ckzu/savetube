from django.shortcuts import redirect, render
from downloader.models import Saver

import requests
from bs4 import BeautifulSoup


def submit(request):
    template_name = 'downloader/index.html'
    if request.method == 'POST':
        source_link = Saver(data.request.POST)
        source_link.save()
        return redirect('downloader/saver_page/%s/' % source_link_id)
    return render(request, template_name, {})

def result(request, source_link_id):
    result_url = requests.get('http://www.youtubeinmp3.com/widget/button/?id={}'.format(source_link_id))
    result_url.encoding = 'utf-8'
    result_url_body = BeautifulSoup(result_url.text)

    return render(request, template_name, {'result_url_body': result_url_body})
