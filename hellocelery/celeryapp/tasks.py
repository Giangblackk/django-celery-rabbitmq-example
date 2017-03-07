from celery import shared_task, current_task
from numpy import random
from scipy.fftpack import fft
from skimage import io
@shared_task
def fft_random(n):
    for i in range(n):
        x = random.normal(0, 0.1, 2000)
        y = fft(x)
        if(i%30 == 0):
            process_percent = int(100 * float(i)/float(n))
            current_task.update_state(state='PROGRESS',
                meta={'process_percent': process_percent})
    return random.random()
@shared_task
def say_hello(n):
    return n
@shared_task
def simple_image_process(file_name):
    random_number = random.randint(1,100)
    image = io.imread(file_name,as_grey=True)
    io.imsave(file_name + str(random_number) +'.png',image)
    return random_number