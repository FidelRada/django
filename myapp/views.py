from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return HttpResponse("Index page")

def hello(request):
    return HttpResponse("hola")

def about(request, username):
    print(username)
    return HttpResponse("about -%s-" % username)

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request, id):
    task = get_object_or_404(Task, id=id) #Task.objects.get(id=id)

    return JsonResponse('task: %s' %task.title, safe=False)

