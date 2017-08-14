from django.shortcuts import redirect, render, get_object_or_404

import requests
from bs4 import BeautifulSoup


def submit(request):
    template_name = 'downloader/index.html'
    result_template_name = 'downloader/saver_page.html'
    if request.method == 'POST':

        source = request.POST['source_url']
        result_url = requests.get('http://www.youtubeinmp3.com/widget/button/?id={}'.format(source))
        result_url.encoding = 'utf-8'
        result_url_parsed = BeautifulSoup(result_url.content)
        old_download_link = result_url_parsed.html.body.a['href']
        result_url_parsed.html.body.a['href'] = 'http://www.youtubeinmp3.com/' + old_download_link
        result_url_body = result_url_parsed.html.body
        return render(request, result_template_name, {'result_url_body': result_url_body})


    return render(request, template_name, {})
