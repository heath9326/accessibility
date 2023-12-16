from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView


# Create your views here.


from django.shortcuts import render
from .forms import InputForm
from .processors import ATypeProcessor
from .services import AutomaticCrawlerService, AccessibilityProcessingService
from .tasks import UrlProcessor
from .models import Url, AItem


# Create your views here.
def index(request):
    if request.method == 'POST':
        print("Request method is post")
        form = InputForm(request.POST)
        if form.is_valid():
            url_to_process = form.data['url']
            url_id = UrlProcessor(url_to_process).process_url()

            crawler_service = AutomaticCrawlerService(url_to_process, url_id)
            crawler_service()

            processing_service = AccessibilityProcessingService(url_to_process, url_id)
            context = processing_service()
            processing_service.clear_db()
            return render(request, "processing/report.html", context)
    else:
        context = {'form': InputForm()}
        return render(request, "processing/index.html", context)

