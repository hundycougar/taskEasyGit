from django.shortcuts import render
from datetime import datetime
from .models import tasks
#from models import tasks

# Create your views here.
#def index(request):
#    context = {
#        'current_date':datetime.now(),
#        'title':'Home'
#    }
#    return render(request, 'taskEasyApp/index.html', context)
#def about(request):
#    context = {
#        'current_date':datetime.now(),
#        'title':'Home'
#    }
#    return render(request, 'taskEasyApp/about.html', context)
#def news(request):
#    context = {
#        'current_date':datetime.now(),
#        'title':'Home'
#    }
#    return render(request, 'taskEasyApp/news.html', context)
def index(request):
    data11 = tasks.objects.filter#(taskID=2)
    #for item in data:
    #    print(item)
    context = {
        #'length': len(data11),
        'taskTables': data11,
    }
    return render(request, 'taskEasyApp/index.html', context)
    