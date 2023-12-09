from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView


# Create your views here.


from django.shortcuts import render
from .forms import InputForm
from .services import AutomaticCrawlerService, AccessibilityProcessingService
from .tasks import AutomaticCrawler, UrlProcessor
from .models import Url


# Create your views here.
def index(request):
    if request.method == 'POST':
        print("Request method is post")
        form = InputForm(request.POST)
        if form.is_valid():
            url_to_process = form.data['url']
            url_id = UrlProcessor(url_to_process).process_url()
            print(url_id)
            # crawler_service = AutomaticCrawlerService(url_to_process, url_id)
            # crawler_service()
            processing_service = AccessibilityProcessingService(url_to_process, url_id)
            processing_service()

            # print(url_to_process)
            return HttpResponse("Request Method is POST")

    else:
        context = {'form': InputForm()}
        return render(request, "processing/index.html", context)

