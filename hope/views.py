from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from hope.models import *
from django.http import Http404
from django.template import loader

# Create your views here.

def home(request):
    drivers = Driver.objects.all()
    # template = loader.get_template('hope/home.html')
    context = {'driver_list': drivers}
    # return HttpResponse(template.render(context, request))
    return render(request, 'hope/home.html', context)


def task_list(request):
    tasks = Task.objects.order_by('departure')[:10]
    return render(request, 'hope/tasks.html', {"tasks": tasks})


def my_tasks(request, driver_id):
    try:
        driver = Driver.objects.get(pk=driver_id)
    except Driver.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'hope/task_list.html', {"driver": driver})


def publish(request):
    return render(request, 'hope/publish.html')


def test(request):
    return HttpResponse("Test "+request.GET['test'])


@csrf_exempt
def add_task(request):
    print(request)
    print(request.POST)
    driver = Driver.objects.get(pk=1)
    driver.task_set.create(start=request.POST['start_at'].encode('gb2312'), end=request.POST['end_at'].encode('gb2312'),
                           departure=request.POST['departure'], quota=request.POST['quota'],
                           remarks=request.POST['remark'])
    return HttpResponse("publish  ")


def result(request):
    return HttpResponse("Result x")
