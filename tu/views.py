from django.shortcuts import render,redirect

# Create your views here.
from tu.models import TODO

lit=[
    {'待办事项':'吃饭','已完成':True}
]

def home(request):
    result = TODO.objects.all()
    if request.method=='POST':
        content=request.POST.get('待办事项')
        if not content or content.strip()=='':
            return render(request,'tulist/home.html',{'清单':lit,'警告':'请输入内容'})
        else:
            TODO.objects.create(thing=content, done=False)
            result = TODO.objects.all()
            return render(request, 'tulist/home.html', {'清单':result})
    else:
        return render(request,'tulist/home.html',{'清单':result})


def edit(request,forloop_counter):
    #提交发的话是post请求
    if request.method=='POST':
        content=request.POST.get("已修改事项")
        if not content or content.strip() == '':
            return render(request, 'tulist/edit.html', {'警告':'请输入内容'})
        else:
            a=TODO.objects.get(pk=forloop_counter)
            a.thing=content
            a.save()
            return redirect('tulist:主页')
    else:
        content = TODO.objects.get(pk=forloop_counter)
        return render(request,'tulist/edit.html',{'待修改事项':content})

def about(request):
    return render(request, 'tulist/about.html')

def delete(request,forloop_counter):
    #只能在post请求下才能删除
    if request.method=='POST':
        #防止在urls上直接做修改就能删除
        TODO.objects.get(pk=int(forloop_counter)).delete()
    return redirect('tulist:主页')







