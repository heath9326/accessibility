from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView


# Create your views here.


from django.shortcuts import render
from .forms import InputForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        return HttpResponse("Request Method is POST")
        print("Request method is post")
    else:
        context = {}
        context['form'] = InputForm()
        return render(request, "processing/index.html", context)

