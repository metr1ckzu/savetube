from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'downloader/index.html'


class SaveView(TemplateView):
    template_name = 'downloader/saver_page.html'
