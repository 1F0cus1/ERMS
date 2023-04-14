from django.shortcuts import render,HttpResponse,redirect
from web import models
# Create your views here.

def depart_list(request):
    """部门列表"""
    # 读数据
    # if request.method == "POST":
    #     nid = request.POST.get("nid")
    #     delete = models.Department.objects.filter(id=nid).delete()
    #     return render(request,'depart_list.html')
    data = models.Department.objects.values()
    print(data)
    return render(request,'depart_list.html', {"data":data})

def depart_add(request):
    """添加部门"""
    if request.method == 'GET':
        return render(request,'depart_add.html')
    else:
        title = request.POST.get("title")
        models.Department.objects.create(title=title)
        return redirect('/depart/list/')  # 重定向
        # return depart_list(request)

def depart_delete(request):
    """删除部门"""
    nid = request.GET.get("nid")
    models.Department.objects.filter(id=nid).delete()
    return redirect('/depart/list/')

def depart_revise(request):
    nid = request.GET.get("nid")

    return render(request,{"ntitle":nid})