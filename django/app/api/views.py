from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# relative import of forms
from api.models import Dummy
from api.tasks import progress_task

from celery.result import AsyncResult

# pass id attribute from urls
def detail_view(request):

    task_id = progress_task.delay()

    context = {
        'task_id': task_id,
        'status': 'submitted',
    }
    return render(request, 'api/index.html', context=context)
    # from django.template import Context, Template
    # return HttpResponse(Template('Dummy count {{ data }}\nTask id {{ task_id }}').render(Context(context)))

def progress_view(request, task_id):
    result = AsyncResult(task_id)
    print('ready', result.ready())
    print('state', result.state)
    print('info', result.info)
    info = result.info or {'done': 0, 'total': 0}
    data = {
        'task_id': task_id,
        'status': result.state,
        'info': info,
    }
    return JsonResponse(data)