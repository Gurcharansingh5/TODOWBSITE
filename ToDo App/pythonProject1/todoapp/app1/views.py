from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect,reverse
from . models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    alltasks = todotitle.objects.all()
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        saveallvalues = todotitle(
            title = title,
            description = description
        )
        saveallvalues.save()
        return render(request,'index.html', {'alltasks':alltasks})
    else:
        return render(request,'index.html', {'alltasks':alltasks})
def todoitems(request,id):
    # listdata = todolist.objects.get(todo_list=id)
    title_id = todotitle.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        allitems = todotitle(
            title = title,
            description = description,
            todo_list = title_id
        )
        allitems.save()

        return redirect('alldata',id =id)

    else:
        return render(request,'items.html',{'id':id })

def task_delete(request, id):
    if request.method == 'POST':
        title_delete = todotitle.objects.filter(id=id)
        title_delete.delete()
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request,'confirmation.html',{'id':id})
def alldata(request,id):

    alldata = todotitle.objects.get(id=id)
    return render(request,'alldata.html',{'alldata':alldata})

def updatetask(request,id):
    update_id = todotitle.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        update_id.title = title
        update_id.description = description

        update_id.save()

        return redirect('alldata',id =id)
        # return redirect('alldata')
    else:
        return render(request,'update.html',{'id':id,'update':update_id })

