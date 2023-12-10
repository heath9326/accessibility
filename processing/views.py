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
            # processing_service = AccessibilityProcessingService(url_to_process, url_id)
            # processing_service()
            a_type_processor = ATypeProcessor(url_id)
            a_type_error_element = a_type_processor.process_elements()

            context_list = []
            for element in a_type_error_element:
                context_list.append(element.element)
            context = {"content": context_list}
            # print(url_to_process)
            return render(request, "processing/report.html", context)

    else:
        context = {'form': InputForm()}
        return render(request, "processing/index.html", context)

