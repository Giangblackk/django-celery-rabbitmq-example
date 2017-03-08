from celery import shared_task, current_task, Task
from numpy import random
from scipy.fftpack import fft
from skimage import io
from hellocelery.celery import app
import requests
from celery.signals import task_success


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

@shared_task
def test(tid, n):
    for i in range(n):
        x = random.normal(0, 0.1, 2000)
        y = fft(x)
        if(i%30 == 0):
            process_percent = int(100 * float(i)/float(n))
            current_task.update_state(state='PROGRESS',
                meta={'process_percent': process_percent})
    return random.random()


# @task_success.connect(sender='celeryapp.tasks.fft_random')
@task_success.connect(sender=fft_random)
def task_id_sent_handler(sender=None, headers=None, body=None, **kwargs):
    # information about task are located in headers for task messages
    # using the task protocol version 2.
    print(sender)
    print('\n ***Task Success***')
    url = 'http://localhost:8000'
    requests.post(url)