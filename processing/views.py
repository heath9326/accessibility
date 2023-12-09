from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView


# Create your views here.


from django.shortcuts import render
from .forms import InputForm
from .tasks import AutomaticCrawler
from .models import Url


# Create your views here.
def index(request):
    if request.method == 'POST':
        print("Request method is post")
        form = InputForm(request.POST)
        if form.is_valid():
            url_to_process = form.data['url']
            Url.objects.create(url=url_to_process).save()

            try:
                automatic_crawler = AutomaticCrawler(url_to_process)
                automatic_crawler.scrape_page()
            except Exception as exc:
                print(f"Exeption occurred while running automated crawler, error {exc}")

            print(url_to_process)
            return HttpResponse("Request Method is POST")


    else:
        context = {'form': InputForm()}
        return render(request, "processing/index.html", context)

