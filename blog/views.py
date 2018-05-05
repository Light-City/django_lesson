from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import time
def show_time(request):
    t=time.ctime()
    return render(request,'index.html',{'time':t})
# 无命名分组 y可随意
def article_year(request,y):
    return HttpResponse("year:%s"%(y))

# 有命名分组 year month 是定死的，根据前面urls中来定
def article_year_month(request,year,month):
    return HttpResponse("year:%s month:%s"%(year,month))

def register(request):
    if request.method=='POST':
        print(request.POST.get('user'))
        return HttpResponse('success!')
    return render(request,'register.html')