from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from tasks import fft_random, simple_image_process
def index(request):
    # x = fft_random.delay(1000000)
    # print(x.status)
    # print(x.get())
    x = simple_image_process.delay('/home/giangblackk/Desktop/eyes.jpg')
    # x = simple_image_process.delay('./eyes.jpg')
    print(x.status)
    return HttpResponse("Hello, world. You're at the polls index.")
