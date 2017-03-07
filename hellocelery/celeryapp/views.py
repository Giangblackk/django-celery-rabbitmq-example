from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from tasks import fft_random
def index(request):
    x = fft_random.delay(1000000)
    print(x.status)
    # print(x.get())
    return HttpResponse("Hello, world. You're at the polls index.")
