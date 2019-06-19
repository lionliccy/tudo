from django.shortcuts import render,redirect

# Create your views here.
lit=[
    {'待办事项':'吃饭','已完成':True}
]

def home(request):
    global lit
    if request.method=='POST':
        content=request.POST.get('待办事项')
        if not content or content.strip()=='':
            return render(request,'tulist/home.html',{'清单':lit,'警告':'请输入内容'})
        else:
            lit.append({'待办事项':content,'已完成':False})
            return render(request, 'tulist/home.html', {'清单': lit})
    else:
        return render(request,'tulist/home.html',{'清单':lit})


def edit(request,forloop_counter):
    global lit
    print(type(forloop_counter))
    content=lit[forloop_counter-1]

    #提交发的话是post请求
    if request.method=='POST':
        content=request.POST.get("已修改事项")
        if not content or content.strip() == '':
            return render(request, 'tulist/edit.html', {'警告':'请输入内容'})
        else:
            lit[forloop_counter-1]['待办事项']=content
            return redirect('tulist:主页')
    else:
        content = lit[forloop_counter-1]['待办事项']
        return render(request,'tulist/edit.html',{'待修改事项':content})

def about(request):
    return render(request, 'tulist/about.html')

def delete(request,forloop_counter):
    global lit
    #只能在post请求下才能删除
    if request.method=='POST':
        #防止在urls上直接做修改就能删除
        forloop_counter = int(forloop_counter) - 1
        print(forloop_counter)
        lit.pop(forloop_counter)
    return redirect('tulist:主页')







