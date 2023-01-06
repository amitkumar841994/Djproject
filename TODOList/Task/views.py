from django.shortcuts import render,redirect
from.models import Task

def Home(request):
    return render(request,'Home.html')

def Task_details(request):
    Tsk=Task()
    Tsk1=Task.objects.all()
    print(Tsk)
    if request.method=='POST':
        Tsk.Task_name=request.POST.get('task_name')
        Tsk.save()
        return redirect('Task_details')
    else:
        Tsk=Task.objects.all()
        print(Tsk)
    return render(request,'Task_details.html',{'tskdt':Tsk1})
def task_status(request,pid,str='complete'):
    tsk_sts=Task.objects.get(id=pid)
    if tsk_sts is not None:
         Task.objects.filter(pk=pid).update(Task_status='Completed')
    return redirect('Task_details')

def task_delete(request,pid):
    tsk_del=Task.objects.get(id=pid)
    tsk_del.delete()
    return redirect('Task_details')

