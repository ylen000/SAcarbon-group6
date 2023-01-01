from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from myapp.models import userdata
from myapp.models import QA
from django.http import Http404
from django.contrib import auth
from django.db.models import F, Func, Value
from django.db.models import Max


# Create your views here.

def signin(request):
    return render(request, 'signin.html')
def signup(request):
    return render(request, 'signup.html')
def login(request):
    uName = request.POST.get('uName')
    uPass = request.POST.get('psw')
    try:
        user=userdata.objects.get(PHONE=uName)

        if uPass==user.PASSWORD:
                #userlogin = request.session.get(uName)
            username=str(user.NAME)
            request.session["username"]=username
            return render(request, 'welcome.html',locals())
        else:
            wrong="帳號或密碼錯誤!!"
            return render(request,'passwordwrong.html',locals())
    except userdata.DoesNotExist:
            wrong="尚未註冊"
            return render(request,'passwordwrong.html',locals())

def home(request):
    username=request.session.get('username')
    return render(request,'index.html',locals())
def rank(request):
    username=request.session.get('username')
    ranking_list=userdata.objects.all().order_by('-POINT')
    rank = ranking_list.filter(POINT__gt=ranking_list.get(NAME=username).POINT).count() + 1
    return render(request,'leaderboard.html',locals())

     

#def rerank(request):


    
    
            


def QAQ (request):
    return render(request, 'QA.html')
def QAw(request):
    q = request.POST.get('question')
    if q =="":
        wrong="未填入任何有效字符"
        a="http://127.0.0.1:8000/123"
        back="問題回報"
        return render(request,'QAsuccess.html',locals())
    else:
        username=request.session.get('username')
        problem = QA(USERNAME=username,QUESTIONS=q)
        problem.save()
        wrong="回報成功，感謝您的寶貴意見"
        a="http://127.0.0.1:8000/login/index"
        back="首頁"
        return render(request,'QAsuccess.html',locals())
    
    
# Create your views here.
def member(request):
         # membername==request.session.get('username')
          username=request.session.get('username')
          user=userdata.objects.get(NAME=username)
          userphone=str(user.PHONE)


          #user = User.objects.get(username='username')
          #mypoint= str(request.GET.get('POINT'))
          #mylevel= str(request.GET.get('IMAGE_NUMBER'))
          return render(request,'member.html',locals())

