from django.shortcuts import render,HttpResponseRedirect
from . forms import Signupform,Loginform,Postform
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . models import Post
from .models import Userinfo
from django.contrib.auth .models import Group
from django.core.cache import cache
# from django.utils import timezone
# Create your views here.
import datetime
def home(request):
    posts=Post.objects.all()
    return render (request,'home.html',{'posts':posts})

def about(request):
    return render (request,'about.html')


def contact(request):
    return render (request,'contact.html')

def dashboard(request):
    if request.user.is_authenticated:
        posts=Post.objects.all()
        user=request.user
        full_name=user.get_full_name()
        ct=cache.get('count',version=user.pk)
        print("Login Count : ",ct)
        now=datetime.datetime.now()
        print(now)
        return render (request,'dashboard.html',{'post':posts, 'full_name':full_name})
    else:
        return HttpResponseRedirect('/login/')


def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/')



def signup(request):
    if request.method=="POST":
       form=Signupform(request.POST)
       if form.is_valid():
           messages.success(request,"Your account Created Sucessfully You Are Author!!")
           form.save()
           form=Signupform()
    else:
        form=Signupform()   
    return render (request,'signup.html',{'form':form})




def userlogin(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form=Loginform(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                # print(uname)
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,"Login Sucessfully !!")
                    return HttpResponseRedirect('/dashboard/')
        else:
            form=Loginform()
        return render (request,'login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')
    


def addpost(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=Postform(request.POST)
            if form.is_valid():
                form.save()
                form=Postform()
        else:
            form=Postform()
        return render(request,'addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')



def updatepost(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Post.objects.get(pk=id)
            form=Postform(request.POST,instance=pi)
            if form.is_valid():
                form.save()
                form=Postform
        else:
            pi=Post.objects.get(pk=id)
            form=Postform(instance=pi)
        return render(request,'updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')
    

def deletepost(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')




